from __future__ import annotations

import json
import logging
import os
import platform
import subprocess
import time
import tracemalloc
from dataclasses import asdict, dataclass
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as package_version
from pathlib import Path
from statistics import median
from typing import Any, Literal

import numpy as np
import pandas as pd

from bottrade.backtest import (
    BacktestResult,
    CalibrationEligibilityError,
    select_entry_threshold,
    simulate_long_flat,
)
from bottrade.config import AppConfig
from bottrade.dataset import DatasetBundle
from bottrade.domain import DataArm, ModelFamily, RunStage
from bottrade.explainability import explain_model, write_explanations
from bottrade.metrics import (
    PerformanceMetrics,
    PredictiveMetrics,
    calculate_performance,
    calculate_predictive,
)
from bottrade.models.base import ResearchRegressor
from bottrade.models.random_forest import RandomForestRegressorModel, RidgeRegressorModel
from bottrade.models.registry import ModelMetadata, ModelRegistry
from bottrade.regimes import aggregate_regime_analyses, analyze_regimes
from bottrade.selection import SelectionLock
from bottrade.utils import deterministic_id, set_global_seed, sha256_file, utc_now
from bottrade.validation import WalkForwardFold, walk_forward_folds

LOGGER = logging.getLogger(__name__)
ExperimentPhase = Literal["development", "holdout"]


class CandidateRejectedError(ValueError):
    def __init__(self, message: str, rejection_path: Path) -> None:
        super().__init__(message)
        self.rejection_path = rejection_path


class HyperparameterSearchRejectedError(ValueError):
    """Raised when every pre-registered search trial fails the calibration gates."""


@dataclass(frozen=True, slots=True)
class FoldEvaluation:
    fold: str
    threshold_return: float
    metrics: dict[str, float | int]
    stress_metrics: dict[str, float | int]
    predictive_metrics: dict[str, float | int]
    regime_metrics: dict[str, dict[str, float | int]]
    seed_metrics: dict[str, dict[str, float | int]]
    seed_stress_metrics: dict[str, dict[str, float | int]]


@dataclass(frozen=True, slots=True)
class EvaluatedFold:
    normal: BacktestResult
    stress: BacktestResult
    threshold: float
    predictive: PredictiveMetrics
    predictions: np.ndarray
    actual: np.ndarray
    regimes: dict[str, dict[str, float | int]]


@dataclass(frozen=True, slots=True)
class ExperimentResult:
    run_id: str
    version: str
    phase: str
    asset: str
    family: str
    arm: str
    parameters: dict[str, Any]
    selection_metrics: dict[str, float | int]
    holdout_metrics: dict[str, float | int]
    stress_metrics: dict[str, float | int]
    benchmark_metrics: dict[str, dict[str, float | int]]
    predictive_metrics: dict[str, float | int]
    folds: list[FoldEvaluation]
    bundle_path: Path
    registry_path: Path


def _aggregate_backtests(
    results: list[BacktestResult], annualization_days: int
) -> PerformanceMetrics:
    if not results:
        raise ValueError("cannot aggregate an empty backtest list")
    timelines = pd.concat([result.timeline for result in results], ignore_index=True)
    timelines = timelines.sort_values("as_of").reset_index(drop=True)
    trade_returns: list[float] = []
    for result in results:
        if not result.trades.empty:
            trade_returns.extend(result.trades["return"].astype(float).tolist())
    return calculate_performance(
        hourly_returns=timelines["strategy_return"],
        timestamps=timelines["as_of"],
        positions=timelines["position"],
        turnover=float(sum(result.metrics.turnover for result in results)),
        transaction_cost=float(sum(result.metrics.transaction_cost for result in results)),
        trade_returns=trade_returns,
        annualization_days=annualization_days,
    )


def _aggregate_predictive(results: list[EvaluatedFold]) -> PredictiveMetrics:
    if not results:
        return calculate_predictive([], [])
    return calculate_predictive(
        np.concatenate([item.actual for item in results]),
        np.concatenate([item.predictions for item in results]),
    )


def _median_performance(metrics: list[PerformanceMetrics]) -> dict[str, float | int]:
    if not metrics:
        raise ValueError("cannot aggregate an empty metric list")
    records = [item.to_dict() for item in metrics]
    output: dict[str, float | int] = {}
    for key in records[0]:
        value = float(median(float(record[key]) for record in records))
        output[key] = int(round(value)) if key == "closed_trades" else value
    return output


def _dependency_versions() -> dict[str, str]:
    output = {"python": platform.python_version()}
    for dependency in ("numpy", "pandas", "scikit-learn", "torch", "onnxruntime"):
        try:
            output[dependency] = package_version(dependency)
        except PackageNotFoundError:
            output[dependency] = "not-installed"
    return output


def _source_control() -> dict[str, str | bool]:
    environment_commit = os.getenv("GITHUB_SHA", "").strip()
    try:
        commit = (
            environment_commit
            or subprocess.run(
                ["git", "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
                timeout=5,
            ).stdout.strip()
        )
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout
        generated_prefixes = ("artifacts/", "data/", "reports/generated/")
        relevant_changes = []
        for line in status.splitlines():
            path = line[3:].strip().strip('"').replace("\\", "/")
            if " -> " in path:
                path = path.split(" -> ", 1)[1]
            if not path.startswith(generated_prefixes):
                relevant_changes.append(path)
        return {"commit": commit, "dirty": bool(relevant_changes)}
    except (FileNotFoundError, subprocess.SubprocessError):
        return {
            "commit": environment_commit or "unavailable",
            "dirty": "unknown",
        }


def _onnx_runtime_metrics(
    path: Path,
    model: ResearchRegressor,
    x: np.ndarray,
    indices: np.ndarray,
) -> tuple[float, float]:
    import onnxruntime as ort

    load_started = time.perf_counter()
    session = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
    load_ms = 1000 * (time.perf_counter() - load_started)
    if model.family == ModelFamily.TRANSFORMER.value:
        transformer: Any = model
        sequence_length = int(transformer.sequence_length)
        normalized = transformer.standardizer.transform(x)
        values = np.stack(
            [normalized[index - sequence_length + 1 : index + 1] for index in indices]
        ).astype(np.float32)
        feed = {"sequence": values}
    else:
        feed = {"features": x[indices].astype(np.float32)}
    started = time.perf_counter()
    session.run(None, feed)
    latency_ms = 1000 * (time.perf_counter() - started) / max(1, len(indices))
    return load_ms, latency_ms


class ExperimentRunner:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.registry = ModelRegistry(config)

    def _record_seed_rejection(
        self,
        *,
        dataset: DatasetBundle,
        family: ModelFamily,
        phase: ExperimentPhase,
        params: dict[str, Any],
        seed: int,
        fold: WalkForwardFold,
        reason: str,
        source_control: dict[str, str | bool],
    ) -> Path:
        created_at = utc_now()
        rejection_id = deterministic_id(
            "rejected",
            dataset.asset.value,
            family.value,
            dataset.arm.value,
            dataset.data_version,
            params,
            seed,
            fold.name,
            created_at.isoformat(),
            length=16,
        )
        directory = (
            self.config.project.artifact_dir
            / "experiments"
            / dataset.asset.value
            / dataset.arm.value
            / family.value
            / "rejections"
        )
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{rejection_id}.json"
        payload = {
            "status": "rejected",
            "rejection_id": rejection_id,
            "created_at": created_at.isoformat(),
            "phase": phase,
            "asset": dataset.asset.value,
            "family": family.value,
            "data_arm": dataset.arm.value,
            "data_version": dataset.data_version,
            "feature_schema_version": dataset.schema_version,
            "parameters": params,
            "failed_seed": seed,
            "failed_fold": fold.name,
            "reason": reason,
            "source_control": source_control,
        }
        temporary = path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        temporary.replace(path)
        return path

    def _default_params(self, family: ModelFamily) -> dict[str, Any]:
        if family == ModelFamily.RANDOM_FOREST:
            return self.config.training.random_forest.model_dump()
        if family == ModelFamily.TRANSFORMER:
            return self.config.training.transformer.model_dump()
        if family == ModelFamily.RIDGE:
            return {"alpha": 1.0}
        raise ValueError(f"unsupported family: {family}")

    def _model(
        self,
        family: ModelFamily,
        params: dict[str, Any],
        *,
        n_features: int,
        seed: int,
        feature_names: tuple[str, ...] | list[str] | None = None,
    ) -> ResearchRegressor:
        if family == ModelFamily.RANDOM_FOREST:
            return RandomForestRegressorModel(params=params, seed=seed)
        if family == ModelFamily.RIDGE:
            return RidgeRegressorModel(alpha=float(params.get("alpha", 1.0)))
        if family == ModelFamily.TRANSFORMER:
            from bottrade.models.transformer import TransformerRegressorModel

            names = list(feature_names or [])
            return TransformerRegressorModel(
                n_features=n_features,
                sequence_length=self.config.features.lookback_hours,
                params=params,
                seed=seed,
                calendar_hour_index=(
                    names.index("calendar_hour_index") if "calendar_hour_index" in names else None
                ),
                calendar_day_index=(
                    names.index("calendar_day_index") if "calendar_day_index" in names else None
                ),
            )
        raise ValueError(f"unsupported family: {family}")

    @staticmethod
    def _normalized_dataset(dataset: DatasetBundle) -> DatasetBundle:
        frame = dataset.frame.sort_values("as_of").reset_index(drop=True)
        return DatasetBundle(
            asset=dataset.asset,
            arm=dataset.arm,
            frame=frame,
            feature_columns=dataset.feature_columns,
            data_version=dataset.data_version,
            schema_version=dataset.schema_version,
            path=dataset.path,
        )

    @staticmethod
    def _arrays(dataset: DatasetBundle) -> tuple[np.ndarray, np.ndarray]:
        x = dataset.frame.loc[:, dataset.feature_columns].to_numpy(dtype=np.float64)
        x[~np.isfinite(x)] = np.nan
        y = dataset.frame["target_normalized_return"].to_numpy(dtype=np.float64)
        return x, y

    def _evaluate_fold(
        self,
        *,
        dataset: DatasetBundle,
        family: ModelFamily,
        params: dict[str, Any],
        fold: WalkForwardFold,
        seeds: list[int],
    ) -> EvaluatedFold:
        x, y = self._arrays(dataset)
        calibration_predictions: list[np.ndarray] = []
        test_predictions: list[np.ndarray] = []
        for seed in seeds:
            set_global_seed(seed)
            model = self._model(
                family,
                params,
                n_features=x.shape[1],
                seed=seed,
                feature_names=dataset.feature_columns,
            )
            model.fit(x, y, fold.train_indices)
            calibration_predictions.append(model.predict(x, fold.calibration_indices))
            test_predictions.append(model.predict(x, fold.test_indices))
        calibration = np.mean(np.stack(calibration_predictions), axis=0)
        test = np.mean(np.stack(test_predictions), axis=0)
        calibration_raw = calibration * dataset.frame.iloc[fold.calibration_indices][
            "target_volatility"
        ].to_numpy(dtype=float)
        test_raw = test * dataset.frame.iloc[fold.test_indices]["target_volatility"].to_numpy(
            dtype=float
        )
        threshold, _ = select_entry_threshold(
            dataset.frame.iloc[fold.calibration_indices].reset_index(drop=True),
            calibration_raw,
            self.config.backtest,
            position_size=self.config.paper.max_asset_weight,
            daily_loss_limit=self.config.paper.daily_loss_limit,
            position_loss_limit=self.config.paper.position_loss_limit,
            drawdown_circuit_breaker=self.config.paper.drawdown_circuit_breaker,
        )
        test_frame = dataset.frame.iloc[fold.test_indices].reset_index(drop=True)
        normal = simulate_long_flat(
            test_frame,
            test_raw,
            threshold_return=threshold,
            cost_per_leg=self.config.backtest.cost_per_leg,
            max_holding_hours=self.config.backtest.max_holding_hours,
            annualization_days=self.config.backtest.annualization_days,
            position_size=self.config.paper.max_asset_weight,
            daily_loss_limit=self.config.paper.daily_loss_limit,
            position_loss_limit=self.config.paper.position_loss_limit,
            drawdown_circuit_breaker=self.config.paper.drawdown_circuit_breaker,
        )
        stress = simulate_long_flat(
            test_frame,
            test_raw,
            threshold_return=threshold,
            cost_per_leg=self.config.backtest.cost_per_leg,
            max_holding_hours=self.config.backtest.max_holding_hours,
            annualization_days=self.config.backtest.annualization_days,
            cost_multiplier=self.config.backtest.stress_multiplier,
            position_size=self.config.paper.max_asset_weight,
            daily_loss_limit=self.config.paper.daily_loss_limit,
            position_loss_limit=self.config.paper.position_loss_limit,
            drawdown_circuit_breaker=self.config.paper.drawdown_circuit_breaker,
        )
        return EvaluatedFold(
            normal=normal,
            stress=stress,
            threshold=threshold,
            predictive=calculate_predictive(y[fold.test_indices], test),
            predictions=test,
            actual=y[fold.test_indices],
            regimes=analyze_regimes(
                test_frame, normal.timeline["strategy_return"], normal.timeline["position"]
            ),
        )

    def _score_params(
        self,
        dataset: DatasetBundle,
        family: ModelFamily,
        params: dict[str, Any],
        folds: list[WalkForwardFold],
        seed: int,
    ) -> float:
        scores: list[float] = []
        for fold in folds:
            try:
                evaluated = self._evaluate_fold(
                    dataset=dataset,
                    family=family,
                    params=params,
                    fold=fold,
                    seeds=[seed],
                )
                scores.append(evaluated.normal.metrics.sortino)
            except (ValueError, RuntimeError) as exc:
                LOGGER.warning("Trial failed on fold %s: %s", fold.name, exc)
                return -1_000_000.0
        return float(median(scores)) if scores else -1_000_000.0

    def search(
        self,
        dataset: DatasetBundle,
        family: ModelFamily,
        folds: list[WalkForwardFold],
        *,
        trials: int,
    ) -> dict[str, Any]:
        defaults = self._default_params(family)
        if trials <= 1 or family == ModelFamily.RIDGE:
            return defaults
        try:
            import optuna
        except ImportError as exc:
            raise RuntimeError("optuna is required for hyperparameter search") from exc
        optuna.logging.set_verbosity(optuna.logging.WARNING)

        def objective(trial: Any) -> float:
            if family == ModelFamily.RANDOM_FOREST:
                params = {
                    "n_estimators": trial.suggest_int("n_estimators", 250, 800, step=50),
                    "max_depth": trial.suggest_int("max_depth", 6, 20),
                    "min_samples_leaf": trial.suggest_int("min_samples_leaf", 3, 20),
                    "max_features": trial.suggest_float("max_features", 0.4, 1.0),
                    "n_jobs": defaults.get("n_jobs", -1),
                }
            else:
                d_model = trial.suggest_categorical("d_model", [32, 64, 96])
                valid_heads = [head for head in [2, 4, 8] if d_model % head == 0]
                params = {
                    **defaults,
                    "d_model": d_model,
                    "nhead": trial.suggest_categorical("nhead", valid_heads),
                    "num_layers": trial.suggest_int("num_layers", 2, 3),
                    "dim_feedforward": trial.suggest_categorical(
                        "dim_feedforward", [64, 128, 192, 256]
                    ),
                    "dropout": trial.suggest_float("dropout", 0.05, 0.25),
                    "learning_rate": trial.suggest_float("learning_rate", 1e-4, 1e-3, log=True),
                    "weight_decay": trial.suggest_float("weight_decay", 1e-6, 1e-3, log=True),
                }
            return self._score_params(dataset, family, params, folds, self.config.training.seeds[0])

        study = optuna.create_study(
            direction="maximize",
            sampler=optuna.samplers.TPESampler(seed=self.config.training.seeds[0]),
        )
        study.optimize(objective, n_trials=min(trials, self.config.training.max_trials))
        if study.best_value <= -1_000_000.0:
            raise HyperparameterSearchRejectedError(
                "no hyperparameter trial produced an eligible calibration strategy"
            )
        return {**defaults, **study.best_params}

    def _simple_benchmarks(
        self,
        dataset: DatasetBundle,
        folds: list[WalkForwardFold],
        target_daily_volatility: float,
    ) -> dict[str, dict[str, float | int]]:
        collections: dict[str, list[BacktestResult]] = {
            "cash": [],
            "buy_hold": [],
            "moving_average": [],
        }
        cost = self.config.backtest.cost_per_leg
        full_close = dataset.frame["reference_close"].astype(float)
        full_moving_average_signal = np.where(
            full_close.rolling(24, min_periods=24).mean()
            > full_close.rolling(72, min_periods=72).mean(),
            1.0,
            -1.0,
        )
        for fold in folds:
            frame = dataset.frame.iloc[fold.test_indices].reset_index(drop=True)
            if frame.empty:
                continue
            collections["cash"].append(
                simulate_long_flat(
                    frame,
                    -np.ones(len(frame)),
                    threshold_return=0.0,
                    cost_per_leg=cost,
                    max_holding_hours=self.config.backtest.max_holding_hours,
                    annualization_days=self.config.backtest.annualization_days,
                )
            )
            collections["buy_hold"].append(
                simulate_long_flat(
                    frame,
                    np.ones(len(frame)),
                    threshold_return=0.0,
                    cost_per_leg=cost,
                    max_holding_hours=len(frame) + 1,
                    annualization_days=self.config.backtest.annualization_days,
                )
            )
            moving_average_signal = full_moving_average_signal[fold.test_indices]
            collections["moving_average"].append(
                simulate_long_flat(
                    frame,
                    moving_average_signal,
                    threshold_return=0.0,
                    cost_per_leg=cost,
                    max_holding_hours=self.config.backtest.max_holding_hours,
                    annualization_days=self.config.backtest.annualization_days,
                )
            )
        output = {
            name: _aggregate_backtests(results, self.config.backtest.annualization_days).to_dict()
            for name, results in collections.items()
            if results
        }
        full_volatility = float(output.get("buy_hold", {}).get("daily_volatility", 0.0))
        risk_weight = (
            min(1.0, target_daily_volatility / full_volatility)
            if target_daily_volatility > 0 and full_volatility > 0
            else 1.0
        )
        risk_equivalent = [
            simulate_long_flat(
                dataset.frame.iloc[fold.test_indices].reset_index(drop=True),
                np.ones(len(fold.test_indices)),
                threshold_return=0.0,
                cost_per_leg=cost,
                max_holding_hours=len(fold.test_indices) + 1,
                annualization_days=self.config.backtest.annualization_days,
                position_size=risk_weight,
            )
            for fold in folds
        ]
        output["buy_hold_risk_equivalent"] = _aggregate_backtests(
            risk_equivalent, self.config.backtest.annualization_days
        ).to_dict()
        output["buy_hold_risk_equivalent"]["position_size"] = risk_weight
        return output

    def _benchmarks(
        self,
        dataset: DatasetBundle,
        folds: list[WalkForwardFold],
        target_daily_volatility: float,
    ) -> dict[str, dict[str, float | int]]:
        output = self._simple_benchmarks(dataset, folds, target_daily_volatility)
        ridge_results = [
            self._evaluate_fold(
                dataset=dataset,
                family=ModelFamily.RIDGE,
                params={"alpha": 1.0},
                fold=fold,
                seeds=[self.config.training.seeds[0]],
            ).normal
            for fold in folds
        ]
        output["ridge"] = _aggregate_backtests(
            ridge_results, self.config.backtest.annualization_days
        ).to_dict()
        return output

    def _load_frozen_market_params(
        self, dataset: DatasetBundle, family: ModelFamily
    ) -> dict[str, Any]:
        path = (
            self.config.project.artifact_dir
            / "experiments"
            / dataset.asset.value
            / DataArm.MARKET.value
            / family.value
            / "best_params.json"
        )
        if not path.exists():
            raise FileNotFoundError(
                f"market-arm parameters must be frozen before ablation training: {path}"
            )
        return json.loads(path.read_text(encoding="utf-8"))

    def _development_params(
        self,
        dataset: DatasetBundle,
        family: ModelFamily,
        folds: list[WalkForwardFold],
        *,
        trials: int,
        params_override: dict[str, Any] | None,
    ) -> dict[str, Any]:
        if params_override is not None:
            return params_override
        if dataset.arm != DataArm.MARKET:
            return self._load_frozen_market_params(dataset, family)
        params = self.search(dataset, family, folds, trials=trials)
        params_path = (
            self.config.project.artifact_dir
            / "experiments"
            / dataset.asset.value
            / dataset.arm.value
            / family.value
            / "best_params.json"
        )
        params_path.parent.mkdir(parents=True, exist_ok=True)
        params_path.write_text(json.dumps(params, indent=2, sort_keys=True), encoding="utf-8")
        return params

    def _folds(
        self,
        frame: pd.DataFrame,
        *,
        phase: ExperimentPhase,
        max_folds: int | None,
    ) -> list[WalkForwardFold]:
        holdout_start = pd.Timestamp(self.config.training.holdout_start)
        holdout_end = pd.Timestamp(self.config.training.holdout_end)
        if phase == "development":
            folds = walk_forward_folds(
                frame["as_of"],
                train_months=self.config.training.train_months,
                calibration_months=self.config.training.calibration_months,
                test_months=self.config.training.test_months,
                purge_hours=self.config.training.purge_hours,
                test_end=holdout_start - pd.Timedelta(seconds=1),
            )
        else:
            folds = walk_forward_folds(
                frame["as_of"],
                train_months=self.config.training.train_months,
                calibration_months=self.config.training.calibration_months,
                test_months=self.config.training.test_months,
                purge_hours=self.config.training.purge_hours,
                test_start=holdout_start,
                test_end=holdout_end,
            )
        if max_folds:
            folds = folds[-max_folds:]
        if not folds:
            label = "pre-holdout" if phase == "development" else "holdout"
            raise ValueError(f"dataset does not contain enough {label} history")
        return folds

    def _verify_selection(
        self,
        dataset: DatasetBundle,
        family: ModelFamily,
        selection_lock: SelectionLock | None,
        selection_role: str,
    ) -> dict[str, Any]:
        if selection_lock is None:
            raise ValueError("opening holdout requires an immutable pre-holdout selection lock")
        if selection_lock.asset != dataset.asset:
            raise ValueError("selection asset does not match dataset")
        selected = selection_lock.roles.get(selection_role, {})
        if not selected:
            raise ValueError(f"selection lock has no frozen role: {selection_role}")
        if (
            ModelFamily(selected["family"]) != family
            or DataArm(selected["data_arm"]) != dataset.arm
        ):
            raise ValueError("family/data arm differs from the frozen selection")
        if selected["data_version"] != dataset.data_version:
            raise ValueError("dataset version differs from the frozen selection")
        if selected["feature_schema_version"] != dataset.schema_version:
            raise ValueError("feature schema differs from the frozen selection")
        selected_path = Path(selected["experiment_path"])
        if (
            not selected_path.exists()
            or sha256_file(selected_path) != selected["experiment_sha256"]
        ):
            raise ValueError("selected experiment checksum mismatch")
        record = json.loads(selected_path.read_text(encoding="utf-8"))
        if record["parameters"] != selected["parameters"]:
            raise ValueError("selected parameters changed after lock")
        return record

    def run(
        self,
        dataset: DatasetBundle,
        family: ModelFamily,
        *,
        trials: int | None = None,
        max_search_folds: int | None = None,
        seeds: list[int] | None = None,
        params_override: dict[str, Any] | None = None,
        phase: ExperimentPhase = "development",
        selection_lock: SelectionLock | None = None,
        selection_role: str = "champion",
    ) -> ExperimentResult:
        if family not in {ModelFamily.RANDOM_FOREST, ModelFamily.TRANSFORMER}:
            raise ValueError("the primary experiment supports RF or Transformer")
        dataset = self._normalized_dataset(dataset)
        evaluation_seeds = seeds or self.config.training.seeds
        requested_trials = trials or self.config.training.max_trials
        folds = self._folds(dataset.frame, phase=phase, max_folds=max_search_folds)
        selected_record: dict[str, Any] = {}
        if phase == "holdout":
            selected_record = self._verify_selection(
                dataset, family, selection_lock, selection_role
            )
            params = dict(selected_record["parameters"])
        else:
            params = self._development_params(
                dataset,
                family,
                folds,
                trials=requested_trials,
                params_override=params_override,
            )
        source_control = _source_control()
        clean_source = (
            source_control.get("commit") not in {"", "unavailable"}
            and source_control.get("dirty") is False
        )

        evaluated_by_seed: dict[int, list[EvaluatedFold]] = {}
        for seed in evaluation_seeds:
            evaluated_by_seed[seed] = []
            for fold in folds:
                try:
                    evaluated_by_seed[seed].append(
                        self._evaluate_fold(
                            dataset=dataset,
                            family=family,
                            params=params,
                            fold=fold,
                            seeds=[seed],
                        )
                    )
                except CalibrationEligibilityError as exc:
                    rejection_path = self._record_seed_rejection(
                        dataset=dataset,
                        family=family,
                        phase=phase,
                        params=params,
                        seed=seed,
                        fold=fold,
                        reason=str(exc),
                        source_control=source_control,
                    )
                    raise CandidateRejectedError(
                        f"candidate rejected at seed={seed}, fold={fold.name}: {exc}",
                        rejection_path,
                    ) from exc
        seed_metrics = {
            str(seed): _aggregate_backtests(
                [item.normal for item in items],
                self.config.backtest.annualization_days,
            ).to_dict()
            for seed, items in evaluated_by_seed.items()
        }
        seed_stress_metrics = {
            str(seed): _aggregate_backtests(
                [item.stress for item in items],
                self.config.backtest.annualization_days,
            ).to_dict()
            for seed, items in evaluated_by_seed.items()
        }
        aggregate = _median_performance(
            [
                _aggregate_backtests(
                    [item.normal for item in items],
                    self.config.backtest.annualization_days,
                )
                for items in evaluated_by_seed.values()
            ]
        )
        aggregate_stress = _median_performance(
            [
                _aggregate_backtests(
                    [item.stress for item in items],
                    self.config.backtest.annualization_days,
                )
                for items in evaluated_by_seed.values()
            ]
        )
        evaluated = [item for items in evaluated_by_seed.values() for item in items]
        predictive = _aggregate_predictive(evaluated)
        regimes = aggregate_regime_analyses([item.regimes for item in evaluated])
        benchmark_metrics = self._benchmarks(dataset, folds, float(aggregate["daily_volatility"]))
        fold_evaluations: list[FoldEvaluation] = []
        for fold_index, fold in enumerate(folds):
            items = [evaluated_by_seed[seed][fold_index] for seed in evaluation_seeds]
            fold_evaluations.append(
                FoldEvaluation(
                    fold=fold.name,
                    threshold_return=float(median(item.threshold for item in items)),
                    metrics=_median_performance([item.normal.metrics for item in items]),
                    stress_metrics=_median_performance([item.stress.metrics for item in items]),
                    predictive_metrics=_aggregate_predictive(items).to_dict(),
                    regime_metrics=aggregate_regime_analyses([item.regimes for item in items]),
                    seed_metrics={
                        str(seed): evaluated_by_seed[seed][fold_index].normal.metrics.to_dict()
                        for seed in evaluation_seeds
                    },
                    seed_stress_metrics={
                        str(seed): evaluated_by_seed[seed][fold_index].stress.metrics.to_dict()
                        for seed in evaluation_seeds
                    },
                )
            )
        median_fold_sortino = float(median(item.normal.metrics.sortino for item in evaluated))

        full_protocol_seeds = evaluation_seeds == self.config.training.seeds
        if phase == "development":
            market_search_complete = dataset.arm != DataArm.MARKET or (
                params_override is None and requested_trials >= self.config.training.max_trials
            )
            protocol_eligible = (
                full_protocol_seeds
                and max_search_folds is None
                and params_override is None
                and market_search_complete
                and clean_source
            )
            selection_metrics = aggregate
            selection_stress_metrics = aggregate_stress
            holdout_metrics: dict[str, float | int] = {}
            holdout_stress_metrics: dict[str, float | int] = {}
            selection_id = ""
        else:
            protocol_eligible = (
                full_protocol_seeds
                and max_search_folds is None
                and selection_lock is not None
                and clean_source
            )
            selection_metrics = dict(selected_record.get("selection_metrics", {}))
            selection_stress_metrics = dict(selected_record.get("selection_stress_metrics", {}))
            holdout_metrics = aggregate
            holdout_stress_metrics = aggregate_stress
            selection_id = selection_lock.selection_id if selection_lock else ""

        created_at = utc_now()
        run_id = deterministic_id(
            phase,
            dataset.asset.value,
            family.value,
            dataset.arm.value,
            dataset.data_version,
            params,
            created_at.isoformat(),
            length=16,
        )
        version = (
            f"{dataset.asset.value.lower()}-{family.value}-{dataset.arm.value}-{phase}-"
            f"{created_at.strftime('%Y%m%dT%H%M%SZ')}-{dataset.data_version[:8]}-{run_id[:6]}"
        )
        run_directory = (
            self.config.project.artifact_dir
            / "experiments"
            / dataset.asset.value
            / dataset.arm.value
            / family.value
            / run_id
        )
        bundle_directory = run_directory / "bundle"
        bundle_directory.mkdir(parents=True, exist_ok=True)

        x, y = self._arrays(dataset)
        holdout_start = pd.Timestamp(self.config.training.holdout_start)
        holdout_end = pd.Timestamp(self.config.training.holdout_end)
        fit_end = (
            holdout_start - pd.Timedelta(hours=self.config.training.purge_hours)
            if phase == "development"
            else min(dataset.frame["as_of"].max(), holdout_end)
        )
        fit_start = fit_end - pd.DateOffset(
            months=self.config.training.train_months + self.config.training.calibration_months
        )
        final_indices = np.flatnonzero(
            ((dataset.frame["as_of"] >= fit_start) & (dataset.frame["as_of"] < fit_end)).to_numpy()
        )
        if not len(final_indices):
            raise ValueError("no samples available for the final frozen fit window")
        deploy_seed = evaluation_seeds[0]
        final_model = self._model(
            family,
            params,
            n_features=x.shape[1],
            seed=deploy_seed,
            feature_names=dataset.feature_columns,
        )
        tracemalloc.start()
        fit_started = time.perf_counter()
        fit_details = final_model.fit(x, y, final_indices)
        fit_seconds = time.perf_counter() - fit_started
        _, peak_python_bytes = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        onnx_path = bundle_directory / "model.onnx"
        export_started = time.perf_counter()
        final_model.export_onnx(onnx_path)
        export_seconds = time.perf_counter() - export_started
        verification_indices = final_indices[-min(128, len(final_indices)) :]
        verification_started = time.perf_counter()
        max_error = final_model.verify_onnx(onnx_path, x, verification_indices)
        verification_seconds = time.perf_counter() - verification_started
        onnx_load_ms, onnx_latency_ms = _onnx_runtime_metrics(
            onnx_path, final_model, x, verification_indices
        )
        prediction_started = time.perf_counter()
        final_model.predict(x, verification_indices)
        prediction_seconds = time.perf_counter() - prediction_started
        tolerance = self.config.training.onnx_tolerance
        native_suffix = ".pt" if family == ModelFamily.TRANSFORMER else ".joblib"
        native_path = run_directory / f"native_model{native_suffix}"
        final_model.save_native(native_path)

        explanation_indices = folds[-1].test_indices
        try:
            explanations = explain_model(
                model=final_model,
                family=family,
                x=x,
                y=y,
                indices=explanation_indices,
                feature_names=list(dataset.feature_columns),
                repeats=self.config.training.permutation_repeats,
                max_samples=self.config.training.explainability_samples,
                integrated_gradient_steps=self.config.training.integrated_gradient_steps,
                seed=deploy_seed,
            )
            explainability_complete = True
        except (RuntimeError, TypeError, ValueError) as exc:
            LOGGER.warning("Explainability artifact is incomplete: %s", exc)
            explanations = {"error": str(exc)}
            explainability_complete = False
        write_explanations(explanations, bundle_directory / "explainability.json")

        operational_metrics: dict[str, float | int | str] = {
            "fit_seconds": fit_seconds,
            "export_seconds": export_seconds,
            "onnx_verification_seconds": verification_seconds,
            "native_inference_ms_per_sample": (
                1000 * prediction_seconds / max(1, len(verification_indices))
            ),
            "onnx_session_load_ms": onnx_load_ms,
            "onnx_inference_ms_per_sample": onnx_latency_ms,
            "peak_python_memory_bytes": int(peak_python_bytes),
            "gpu_peak_memory_bytes": int(fit_details.get("gpu_peak_memory_bytes", 0)),
            "onnx_size_bytes": onnx_path.stat().st_size,
            "native_size_bytes": native_path.stat().st_size,
            "runtime_device": str(fit_details.get("device", "cpu")),
        }
        metadata = ModelMetadata(
            version=version,
            asset=dataset.asset,
            family=family,
            data_arm=dataset.arm,
            stage=RunStage.DEVELOPMENT,
            trained_at=created_at,
            training_end=pd.Timestamp(fit_end).to_pydatetime(),
            horizon_hours=self.config.features.horizon_hours,
            sequence_length=(
                self.config.features.lookback_hours if family == ModelFamily.TRANSFORMER else 1
            ),
            feature_names=list(dataset.feature_columns),
            feature_schema_version=dataset.schema_version,
            data_version=dataset.data_version,
            threshold_return=evaluated_by_seed[deploy_seed][-1].threshold,
            seed=deploy_seed,
            parameters=params,
            protocol_phase=phase,
            protocol_eligible=protocol_eligible,
            selection_id=selection_id,
            selection_role=selection_role if phase == "holdout" else "",
            selection_metrics=selection_metrics,
            selection_stress_metrics=selection_stress_metrics,
            holdout_metrics=holdout_metrics,
            stress_metrics=holdout_stress_metrics,
            benchmark_metrics=benchmark_metrics,
            predictive_metrics=predictive.to_dict(),
            regime_metrics=regimes,
            operational_metrics=operational_metrics,
            explainability_complete=explainability_complete,
            onnx_verified=max_error <= tolerance,
            onnx_max_abs_error=max_error,
            source_control=source_control,
        )
        (bundle_directory / "metadata.json").write_text(
            json.dumps(metadata.model_dump(mode="json"), indent=2, sort_keys=True),
            encoding="utf-8",
        )
        summary = {
            "run_id": run_id,
            "version": version,
            "created_at": created_at.isoformat(),
            "phase": phase,
            "protocol_eligible": protocol_eligible,
            "selection_id": selection_id,
            "selection_role": selection_role if phase == "holdout" else "",
            "asset": dataset.asset.value,
            "family": family.value,
            "arm": dataset.arm.value,
            "data_version": dataset.data_version,
            "feature_schema_version": dataset.schema_version,
            "parameters": params,
            "search_trials": requested_trials if dataset.arm == DataArm.MARKET else 0,
            "seeds": evaluation_seeds,
            "seed_metrics": seed_metrics,
            "seed_stress_metrics": seed_stress_metrics,
            "seed_sortino_std": float(
                np.std([float(item["sortino"]) for item in seed_metrics.values()], ddof=0)
            ),
            "fit_details": fit_details,
            "selection_metrics": selection_metrics,
            "selection_stress_metrics": selection_stress_metrics,
            "holdout_metrics": holdout_metrics,
            "stress_metrics": holdout_stress_metrics,
            "benchmark_metrics": benchmark_metrics,
            "predictive_metrics": predictive.to_dict(),
            "regime_metrics": regimes,
            "operational_metrics": operational_metrics,
            "explainability_complete": explainability_complete,
            "folds": [asdict(item) for item in fold_evaluations],
            "median_fold_sortino": median_fold_sortino,
            "onnx_max_abs_error": max_error,
            "onnx_tolerance": tolerance,
            "dependencies": _dependency_versions(),
            "source_control": source_control,
            "native_model_sha256": sha256_file(native_path),
        }
        (run_directory / "experiment.json").write_text(
            json.dumps(summary, indent=2, sort_keys=True, default=str), encoding="utf-8"
        )
        registry_path = self.registry.register(bundle_directory, metadata)
        return ExperimentResult(
            run_id=run_id,
            version=version,
            phase=phase,
            asset=dataset.asset.value,
            family=family.value,
            arm=dataset.arm.value,
            parameters=params,
            selection_metrics=selection_metrics,
            holdout_metrics=holdout_metrics,
            stress_metrics=(
                selection_stress_metrics if phase == "development" else holdout_stress_metrics
            ),
            benchmark_metrics=benchmark_metrics,
            predictive_metrics=predictive.to_dict(),
            folds=fold_evaluations,
            bundle_path=bundle_directory,
            registry_path=registry_path,
        )

    def refit(
        self,
        dataset: DatasetBundle,
        *,
        parent_directory: Path,
        parent: ModelMetadata,
        slot: str,
    ) -> ExperimentResult:
        """Create a monthly artifact without changing family, arm or hyperparameters."""

        if parent.stage != RunStage.PAPER:
            raise ValueError("monthly refit requires an active paper-stage parent")
        if parent.asset != dataset.asset or parent.data_arm != dataset.arm:
            raise ValueError("refit dataset differs from the active model identity")
        if parent.family not in {ModelFamily.RANDOM_FOREST, ModelFamily.TRANSFORMER}:
            raise ValueError("unsupported refit family")
        dataset = self._normalized_dataset(dataset)
        if list(dataset.feature_columns) != parent.feature_names:
            raise ValueError("feature names/order changed; frozen monthly refit aborted")
        if dataset.schema_version != parent.feature_schema_version:
            raise ValueError("feature schema changed; frozen monthly refit aborted")
        if sha256_file(parent_directory / "model.onnx") != parent.artifact_sha256:
            raise ValueError("active parent checksum mismatch")

        x, y = self._arrays(dataset)
        timestamps = dataset.frame["as_of"]
        latest = timestamps.max()
        calibration_start = latest - pd.DateOffset(months=self.config.training.calibration_months)
        train_start = calibration_start - pd.DateOffset(months=self.config.training.train_months)
        train_end = calibration_start - pd.Timedelta(hours=self.config.training.purge_hours)
        train_indices = np.flatnonzero(
            ((timestamps >= train_start) & (timestamps < train_end)).to_numpy()
        )
        calibration_indices = np.flatnonzero(
            ((timestamps >= calibration_start) & (timestamps <= latest)).to_numpy()
        )
        if not len(train_indices) or not len(calibration_indices):
            raise ValueError("insufficient rolling history for monthly refit")

        seed = parent.seed
        calibrator = self._model(
            parent.family,
            dict(parent.parameters),
            n_features=x.shape[1],
            seed=seed,
            feature_names=dataset.feature_columns,
        )
        calibrator.fit(x, y, train_indices)
        calibration_prediction = calibrator.predict(x, calibration_indices)
        calibration_raw = calibration_prediction * dataset.frame.iloc[calibration_indices][
            "target_volatility"
        ].to_numpy(dtype=float)
        threshold, calibration_backtest = select_entry_threshold(
            dataset.frame.iloc[calibration_indices].reset_index(drop=True),
            calibration_raw,
            self.config.backtest,
            position_size=self.config.paper.max_asset_weight,
            daily_loss_limit=self.config.paper.daily_loss_limit,
            position_loss_limit=self.config.paper.position_loss_limit,
            drawdown_circuit_breaker=self.config.paper.drawdown_circuit_breaker,
        )

        final_start = latest - pd.DateOffset(
            months=self.config.training.train_months + self.config.training.calibration_months
        )
        final_indices = np.flatnonzero(
            ((timestamps >= final_start) & (timestamps <= latest)).to_numpy()
        )
        model = self._model(
            parent.family,
            dict(parent.parameters),
            n_features=x.shape[1],
            seed=seed,
            feature_names=dataset.feature_columns,
        )
        created_at = utc_now()
        run_id = deterministic_id(
            "refit",
            dataset.asset.value,
            slot,
            parent.version,
            dataset.data_version,
            created_at.isoformat(),
            length=16,
        )
        version = (
            f"{dataset.asset.value.lower()}-{parent.family.value}-{dataset.arm.value}-refit-"
            f"{created_at.strftime('%Y%m%dT%H%M%SZ')}-{dataset.data_version[:8]}-{run_id[:6]}"
        )
        run_directory = (
            self.config.project.artifact_dir / "refits" / dataset.asset.value / slot / run_id
        )
        bundle_directory = run_directory / "bundle"
        bundle_directory.mkdir(parents=True, exist_ok=True)

        tracemalloc.start()
        fit_started = time.perf_counter()
        fit_details = model.fit(x, y, final_indices)
        fit_seconds = time.perf_counter() - fit_started
        _, peak_python_bytes = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        onnx_path = bundle_directory / "model.onnx"
        export_started = time.perf_counter()
        model.export_onnx(onnx_path)
        export_seconds = time.perf_counter() - export_started
        verification_indices = final_indices[-min(128, len(final_indices)) :]
        verification_started = time.perf_counter()
        max_error = model.verify_onnx(onnx_path, x, verification_indices)
        verification_seconds = time.perf_counter() - verification_started
        onnx_load_ms, onnx_latency_ms = _onnx_runtime_metrics(
            onnx_path, model, x, verification_indices
        )
        prediction_started = time.perf_counter()
        model.predict(x, verification_indices)
        prediction_seconds = time.perf_counter() - prediction_started
        native_suffix = ".pt" if parent.family == ModelFamily.TRANSFORMER else ".joblib"
        native_path = run_directory / f"native_model{native_suffix}"
        model.save_native(native_path)

        try:
            explanations = explain_model(
                model=model,
                family=parent.family,
                x=x,
                y=y,
                indices=calibration_indices,
                feature_names=list(dataset.feature_columns),
                repeats=self.config.training.permutation_repeats,
                max_samples=self.config.training.explainability_samples,
                integrated_gradient_steps=self.config.training.integrated_gradient_steps,
                seed=seed,
            )
            explainability_complete = True
        except (RuntimeError, TypeError, ValueError) as exc:
            LOGGER.warning("Refit explainability artifact is incomplete: %s", exc)
            explanations = {"error": str(exc)}
            explainability_complete = False
        write_explanations(explanations, bundle_directory / "explainability.json")

        operational_metrics: dict[str, float | int | str] = {
            "fit_seconds": fit_seconds,
            "export_seconds": export_seconds,
            "onnx_verification_seconds": verification_seconds,
            "native_inference_ms_per_sample": (
                1000 * prediction_seconds / max(1, len(verification_indices))
            ),
            "onnx_session_load_ms": onnx_load_ms,
            "onnx_inference_ms_per_sample": onnx_latency_ms,
            "peak_python_memory_bytes": int(peak_python_bytes),
            "gpu_peak_memory_bytes": int(fit_details.get("gpu_peak_memory_bytes", 0)),
            "onnx_size_bytes": onnx_path.stat().st_size,
            "native_size_bytes": native_path.stat().st_size,
            "runtime_device": str(fit_details.get("device", "cpu")),
        }
        predictive = calculate_predictive(y[calibration_indices], calibration_prediction)
        source_control = _source_control()
        clean_source = (
            source_control.get("commit") not in {"", "unavailable"}
            and source_control.get("dirty") is False
        )
        metadata = ModelMetadata(
            version=version,
            asset=parent.asset,
            family=parent.family,
            data_arm=parent.data_arm,
            stage=RunStage.DEVELOPMENT,
            trained_at=created_at,
            training_end=latest.to_pydatetime(),
            horizon_hours=parent.horizon_hours,
            sequence_length=parent.sequence_length,
            feature_names=parent.feature_names,
            feature_schema_version=parent.feature_schema_version,
            data_version=dataset.data_version,
            threshold_return=threshold,
            seed=seed,
            parameters=parent.parameters,
            protocol_phase="refit",
            protocol_eligible=clean_source,
            selection_id=parent.selection_id,
            selection_role=slot,
            parent_version=parent.version,
            selection_metrics=parent.selection_metrics,
            selection_stress_metrics=parent.selection_stress_metrics,
            holdout_metrics=parent.holdout_metrics,
            stress_metrics=parent.stress_metrics,
            benchmark_metrics=parent.benchmark_metrics,
            predictive_metrics=parent.predictive_metrics,
            regime_metrics=parent.regime_metrics,
            operational_metrics=operational_metrics,
            explainability_complete=explainability_complete,
            onnx_verified=max_error <= self.config.training.onnx_tolerance,
            onnx_max_abs_error=max_error,
            source_control=source_control,
        )
        (bundle_directory / "metadata.json").write_text(
            json.dumps(metadata.model_dump(mode="json"), indent=2, sort_keys=True),
            encoding="utf-8",
        )
        summary = {
            "run_id": run_id,
            "version": version,
            "created_at": created_at.isoformat(),
            "phase": "refit",
            "asset": dataset.asset.value,
            "slot": slot,
            "family": parent.family.value,
            "arm": dataset.arm.value,
            "parent_version": parent.version,
            "selection_id": parent.selection_id,
            "data_version": dataset.data_version,
            "parameters": parent.parameters,
            "threshold_return": threshold,
            "calibration_metrics": calibration_backtest.metrics.to_dict(),
            "calibration_predictive_metrics": predictive.to_dict(),
            "holdout_metrics_frozen": parent.holdout_metrics,
            "stress_metrics_frozen": parent.stress_metrics,
            "fit_details": fit_details,
            "operational_metrics": operational_metrics,
            "explainability_complete": explainability_complete,
            "onnx_max_abs_error": max_error,
            "dependencies": _dependency_versions(),
            "source_control": source_control,
            "native_model_sha256": sha256_file(native_path),
        }
        (run_directory / "experiment.json").write_text(
            json.dumps(summary, indent=2, sort_keys=True, default=str), encoding="utf-8"
        )
        registry_path = self.registry.register(bundle_directory, metadata)
        return ExperimentResult(
            run_id=run_id,
            version=version,
            phase="refit",
            asset=dataset.asset.value,
            family=parent.family.value,
            arm=dataset.arm.value,
            parameters=dict(parent.parameters),
            selection_metrics=dict(parent.selection_metrics),
            holdout_metrics=dict(parent.holdout_metrics),
            stress_metrics=dict(parent.stress_metrics),
            benchmark_metrics=dict(parent.benchmark_metrics),
            predictive_metrics=dict(parent.predictive_metrics),
            folds=[],
            bundle_path=bundle_directory,
            registry_path=registry_path,
        )
