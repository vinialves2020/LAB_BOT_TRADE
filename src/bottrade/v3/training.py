from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.v3.backtest import signal_ceiling_backtest
from bottrade.v3.config import V3Config
from bottrade.v3.meta_models import MetaModelBundle, fit_meta_model
from bottrade.v3.statistics import summarize_returns
from bottrade.validation import require_minimum_folds, walk_forward_folds

FUTURE_COLUMNS = {
    "entry_price",
    "exit_price",
    "gross_return",
    "bars_to_exit",
    "label_valid",
    "future_close",
    "future_close_3h",
    "future_close_6h",
    "future_close_12h",
    "target_raw_return",
    "target_normalized_return",
    "mfe",
    "mae",
    "net_return_1x",
    "net_return_2x",
    "net_return_3x",
}


@dataclass(frozen=True, slots=True)
class Policy:
    probability_threshold: float
    margin_bps: int


@dataclass(frozen=True, slots=True)
class MetaFoldResult:
    fold_name: str
    policy: Policy
    metrics: dict[str, float | int]
    trades: pd.DataFrame


@dataclass(frozen=True, slots=True)
class MetaExperimentResult:
    family: str
    asset: Asset
    folds: tuple[MetaFoldResult, ...]
    trades: pd.DataFrame
    metrics: dict[str, float | int]
    bundle: MetaModelBundle | None = None


def _safe_numeric(value: pd.Series) -> pd.Series:
    return pd.to_numeric(value, errors="coerce").replace([np.inf, -np.inf], np.nan)


def build_meta_table(features: pd.DataFrame, candidates: pd.DataFrame, labels: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    """Join point-in-time features to candidates and event labels."""

    if candidates.empty or labels.empty:
        return pd.DataFrame(), []
    if FUTURE_COLUMNS.intersection(features.columns):
        raise AssertionError("features contain future/label columns")
    feature_data = features.copy()
    feature_data["as_of"] = pd.to_datetime(feature_data["as_of"], utc=True)
    feature_data = feature_data.drop(columns=["asset"], errors="ignore")
    feature_numeric = [
        column
        for column in feature_data.columns
        if column not in {"as_of", "continuity_segment_id"}
        and pd.api.types.is_numeric_dtype(feature_data[column])
    ]
    feature_data = feature_data[["as_of", *feature_numeric]]
    candidate_data = candidates.copy()
    candidate_data["as_of"] = pd.to_datetime(candidate_data["as_of"], utc=True)
    candidate_data["strategy_family"] = candidate_data["strategy_family"].astype(str)
    candidate_data["variant_id"] = candidate_data["variant_id"].astype(str)
    candidate_numeric = [
        column
        for column in candidate_data.columns
        if column not in {"candidate_id", "asset", "as_of", "strategy_family", "variant_id", "continuity_segment_id"}
        and pd.api.types.is_numeric_dtype(candidate_data[column])
    ]
    one_hot = pd.get_dummies(
        candidate_data[["candidate_id", "strategy_family", "variant_id"]],
        columns=["strategy_family", "variant_id"],
        dtype=float,
    )
    candidate_data = pd.concat(
        [candidate_data[["candidate_id", "asset", "as_of", *candidate_numeric]], one_hot.drop(columns=["candidate_id"])],
        axis=1,
    )
    table = candidate_data.merge(feature_data, on="as_of", how="left", validate="many_to_one")
    label_data = labels.copy()
    label_data["candidate_id"] = label_data["candidate_id"].astype(str)
    label_columns = [
        column
        for column in label_data.columns
        if column
        not in {
            "asset",
            "as_of",
            "strategy_family",
            "variant_id",
            "horizon_hours",
            "signal_strength",
            "take_profit_return",
            "stop_loss_return",
        }
    ]
    label_data = label_data[label_columns]
    table = table.merge(label_data, on="candidate_id", how="inner", validate="one_to_one")
    table = table[table["label_valid"].astype(bool)].copy()
    numeric_columns = [
        column
        for column in table.columns
        if column not in FUTURE_COLUMNS
        and column not in {"candidate_id", "asset", "as_of", "entry_time", "exit_time", "outcome", "invalid_reason", "label_valid"}
        and pd.api.types.is_numeric_dtype(table[column])
    ]
    table[numeric_columns] = table[numeric_columns].apply(_safe_numeric)
    table = table.dropna(subset=numeric_columns + ["net_return_1x"])
    if table.empty:
        return table, numeric_columns
    table = table.sort_values("as_of").reset_index(drop=True)
    if FUTURE_COLUMNS.intersection(numeric_columns):
        raise AssertionError("future columns entered meta feature matrix")
    return table, numeric_columns


def build_transformer_sequences(
    table: pd.DataFrame,
    features: pd.DataFrame,
    feature_columns: list[str],
    *,
    lookback: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Materialize causal ``lookback`` sequences aligned to meta-table rows.

    Candidate-specific columns (strategy, horizon and signal strength) are
    known at the decision timestamp and are held constant across the history;
    market columns are taken from the corresponding historical feature rows.
    Rows without a complete hourly segment are marked invalid and must be
    removed before fitting the temporal model.
    """

    if table.empty or features.empty:
        return np.empty((0, lookback, len(feature_columns)), dtype=np.float32), np.zeros(0, dtype=bool)
    history = features.copy().sort_values("as_of").reset_index(drop=True)
    history["as_of"] = pd.to_datetime(history["as_of"], utc=True)
    history_times = history["as_of"].array.asi8
    history_segments = history.get("continuity_segment_id", pd.Series("", index=history.index)).astype(str).to_numpy()
    shared = [column for column in feature_columns if column in history.columns]
    shared_positions = [feature_columns.index(column) for column in shared]
    values = np.zeros((len(table), lookback, len(feature_columns)), dtype=np.float32)
    valid = np.zeros(len(table), dtype=bool)
    for row_number, row in enumerate(table.itertuples(index=False)):
        as_of = pd.Timestamp(row.as_of)
        timestamp_ns = as_of.value
        position = int(np.searchsorted(history_times, timestamp_ns, side="left"))
        if position >= len(history_times) or history_times[position] != timestamp_ns:
            continue
        start = position - lookback + 1
        if start < 0:
            continue
        window_times = history_times[start : position + 1]
        if len(window_times) != lookback or np.any(np.diff(window_times) != pd.Timedelta(hours=1).value):
            continue
        window_segments = history_segments[start : position + 1]
        if len(set(window_segments)) != 1:
            continue
        matrix = np.zeros((lookback, len(feature_columns)), dtype=np.float32)
        if shared:
            matrix[:, shared_positions] = history.iloc[start : position + 1][shared].to_numpy(dtype=np.float32)
        for column_number, column in enumerate(feature_columns):
            if column not in shared:
                matrix[:, column_number] = float(getattr(row, column, 0.0) or 0.0)
        values[row_number] = np.nan_to_num(matrix, nan=0.0, posinf=0.0, neginf=0.0)
        valid[row_number] = True
    return values, valid


def select_policy(
    calibration: pd.DataFrame,
    probabilities: np.ndarray,
    expected_returns: np.ndarray,
    *,
    config: V3Config,
) -> Policy:
    if len(calibration) != len(probabilities) or len(calibration) != len(expected_returns):
        raise ValueError("calibration predictions and rows differ")
    candidates: list[tuple[tuple[float, int, int], Policy]] = []
    for threshold in config.probability_thresholds:
        for margin in config.margin_bps:
            selected = calibration.copy()
            selected["approved"] = (
                np.asarray(probabilities) >= threshold
            ) & (np.asarray(expected_returns) >= margin / 10_000.0)
            selected = selected[selected["approved"]].copy()
            if selected.empty:
                score = (-np.inf, 0, 0)
            else:
                metrics = summarize_returns(
                    selected["net_return_1x"],
                    selected["exit_time"],
                    selected["net_return_1x"],
                )
                score = (
                    float(metrics.get("sortino", -np.inf)),
                    int(metrics.get("closed_trades", 0)),
                    -margin,
                )
            candidates.append((score, Policy(float(threshold), int(margin))))
    if not candidates:
        raise ValueError("no policy candidates configured")
    return max(candidates, key=lambda item: item[0])[1]


def _approved_labels(
    labels: pd.DataFrame,
    probabilities: np.ndarray,
    expected_returns: np.ndarray,
    policy: Policy,
) -> pd.DataFrame:
    result = labels.copy()
    result["probability_net_positive"] = probabilities
    result["expected_net_return"] = expected_returns
    result["approved"] = (
        result["probability_net_positive"] >= policy.probability_threshold
    ) & (result["expected_net_return"] >= policy.margin_bps / 10_000.0)
    return result[result["approved"]].copy()


def walk_forward_meta_experiment(
    table: pd.DataFrame,
    feature_columns: list[str],
    *,
    family: str,
    asset: Asset,
    config: V3Config,
    seed: int = 11,
    params: dict[str, Any] | None = None,
    development_end: str | None = None,
    sequence_values: np.ndarray | None = None,
) -> MetaExperimentResult:
    if table.empty:
        return MetaExperimentResult(family, asset, (), pd.DataFrame(), summarize_returns([], [], []))
    order = table.sort_values(["as_of", "candidate_id"], kind="mergesort").index
    data = table.loc[order].reset_index(drop=True)
    if sequence_values is not None:
        sequence_values = sequence_values[np.asarray(order, dtype=int)]
    data["as_of"] = pd.to_datetime(data["as_of"], utc=True)
    if development_end is not None:
        data = data[data["as_of"] < pd.Timestamp(development_end, tz="UTC")].reset_index(drop=True)
    folds = walk_forward_folds(
        data["as_of"],
        train_months=config.train_months,
        calibration_months=config.calibration_months,
        test_months=config.test_months,
        purge_hours=config.purge_hours,
        minimum_coverage=0.0,
    )
    require_minimum_folds(folds, config.minimum_pre_holdout_folds)
    fold_results: list[MetaFoldResult] = []
    all_trades: list[pd.DataFrame] = []
    for fold in folds:
        train = data.iloc[fold.train_indices]
        calibration = data.iloc[fold.calibration_indices]
        test = data.iloc[fold.test_indices]
        if len(train) < 50 or train["y_class"].nunique() < 2:
            continue
        train_values = (
            sequence_values[fold.train_indices]
            if sequence_values is not None
            else train[feature_columns].to_numpy(dtype=np.float32)
        )
        calibration_values = (
            sequence_values[fold.calibration_indices]
            if sequence_values is not None
            else calibration[feature_columns].to_numpy(dtype=np.float32)
        )
        test_values = (
            sequence_values[fold.test_indices]
            if sequence_values is not None
            else test[feature_columns].to_numpy(dtype=np.float32)
        )
        model = fit_meta_model(
            family,
            train_values,
            train["y_class"].to_numpy(dtype=int),
            train["net_return_1x"].to_numpy(dtype=float),
            train["mae"].to_numpy(dtype=float) if "mae" in train else None,
            seed=seed,
            params=params,
        )
        calibration_probability, calibration_return, _ = model.predict(
            calibration_values
        )
        policy = select_policy(calibration, calibration_probability, calibration_return, config=config)
        test_probability, test_return, test_mae = model.predict(
            test_values
        )
        approved = _approved_labels(test, test_probability, test_return, policy)
        if test_mae is not None:
            positions = test.index.get_indexer(approved.index)
            approved["expected_mae"] = test_mae[positions]
        result = signal_ceiling_backtest(
            approved,
            config=config,
            cost_multiplier=1.0,
        )
        fold_results.append(MetaFoldResult(fold.name, policy, result.metrics, result.trades))
        if not result.trades.empty:
            all_trades.append(result.trades.assign(fold=fold.name))
    trades = pd.concat(all_trades, ignore_index=True) if all_trades else pd.DataFrame()
    if trades.empty:
        metrics = summarize_returns([], [], [])
    else:
        metrics = summarize_returns(trades["net_return"], trades["exit_time"], trades["net_return"])
    return MetaExperimentResult(family, asset, tuple(fold_results), trades, metrics)


def prepare_targets(table: pd.DataFrame) -> pd.DataFrame:
    result = table.copy()
    result["y_class"] = (pd.to_numeric(result["net_return_1x"], errors="coerce") > 0).astype(int)
    if "mae" not in result:
        result["mae"] = 0.0
    else:
        result["mae"] = pd.to_numeric(result["mae"], errors="coerce").fillna(0.0)
    return result
