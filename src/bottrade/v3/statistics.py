from __future__ import annotations

import math
from itertools import combinations
from statistics import NormalDist

import numpy as np
import pandas as pd

from bottrade.v3.config import V3Config
from bottrade.v3.domain import V3GateResult


def daily_compounded_returns(
    returns: pd.Series | np.ndarray,
    timestamps: pd.Series | pd.DatetimeIndex,
) -> pd.Series:
    times = pd.DatetimeIndex(pd.to_datetime(timestamps, utc=True))
    values = pd.Series(np.asarray(returns, dtype=float), index=times)
    return (1.0 + values.fillna(0.0)).resample("1D").prod() - 1.0


def _long_run_variance(values: np.ndarray, max_lag: int | None = None) -> float:
    clean = np.asarray(values, dtype=float)
    clean = clean[np.isfinite(clean)]
    if len(clean) < 2:
        return 0.0
    centered = clean - clean.mean()
    gamma0 = float(np.mean(centered * centered))
    lag_limit = min(len(clean) - 1, max_lag or int(np.sqrt(len(clean))))
    variance = gamma0
    for lag in range(1, lag_limit + 1):
        gamma = float(np.mean(centered[lag:] * centered[:-lag]))
        weight = 1.0 - lag / (lag_limit + 1.0)
        variance += 2.0 * weight * gamma
    return max(variance, 0.0)


def autocorrelation_adjusted_sharpe(
    returns: pd.Series | np.ndarray,
    *,
    annualization_days: int = 365,
    max_lag: int | None = None,
) -> float:
    values = np.asarray(returns, dtype=float)
    values = values[np.isfinite(values)]
    if len(values) < 2:
        return 0.0
    long_run_std = math.sqrt(_long_run_variance(values, max_lag=max_lag))
    if long_run_std <= 0:
        return 0.0
    return float(math.sqrt(annualization_days) * values.mean() / long_run_std)


def block_bootstrap_sharpe_ci(
    returns: pd.Series | np.ndarray,
    *,
    annualization_days: int = 365,
    block_size: int | None = None,
    samples: int = 2000,
    seed: int = 11,
) -> tuple[float, float]:
    values = np.asarray(returns, dtype=float)
    values = values[np.isfinite(values)]
    if len(values) < 2:
        return (0.0, 0.0)
    block = max(1, int(block_size or round(math.sqrt(len(values)))))
    rng = np.random.default_rng(seed)
    starts = np.arange(max(1, len(values) - block + 1))
    estimates: list[float] = []
    for _ in range(samples):
        pieces: list[np.ndarray] = []
        while sum(len(piece) for piece in pieces) < len(values):
            start = int(rng.choice(starts))
            pieces.append(values[start : start + block])
        boot = np.concatenate(pieces)[: len(values)]
        estimates.append(autocorrelation_adjusted_sharpe(boot, annualization_days=annualization_days))
    return (float(np.quantile(estimates, 0.025)), float(np.quantile(estimates, 0.975)))


def _profit_factor(trades: pd.Series | np.ndarray) -> float:
    values = np.asarray(trades, dtype=float)
    values = values[np.isfinite(values)]
    gains = float(values[values > 0].sum())
    losses = abs(float(values[values < 0].sum()))
    if losses == 0:
        return gains / 1e-12 if gains > 0 else 0.0
    return gains / losses


def _max_drawdown(returns: pd.Series | np.ndarray) -> float:
    values = np.asarray(returns, dtype=float)
    equity = np.cumprod(1.0 + np.nan_to_num(values, nan=0.0))
    if len(equity) == 0:
        return 0.0
    drawdown = equity / np.maximum.accumulate(equity) - 1.0
    return abs(float(np.min(drawdown)))


def summarize_returns(
    returns: pd.Series | np.ndarray,
    timestamps: pd.Series | pd.DatetimeIndex,
    trades: pd.Series | np.ndarray,
    *,
    annualization_days: int = 365,
) -> dict[str, float | int]:
    daily = daily_compounded_returns(returns, timestamps)
    values = np.asarray(daily, dtype=float)
    total = float(np.prod(1.0 + values) - 1.0) if len(values) else 0.0
    annualized = float((1.0 + total) ** (annualization_days / max(len(values), 1)) - 1.0) if total > -1 else -1.0
    sharpe = autocorrelation_adjusted_sharpe(values, annualization_days=annualization_days)
    downside = values[values < 0]
    sortino = float(math.sqrt(annualization_days) * values.mean() / math.sqrt(np.mean(downside**2))) if len(downside) else 0.0
    trade_values = np.asarray(trades, dtype=float)
    return {
        "total_return": total,
        "annualized_return": annualized,
        "sharpe_hac": sharpe,
        "sortino": sortino,
        "max_drawdown": _max_drawdown(values),
        "profit_factor": _profit_factor(trade_values),
        "closed_trades": int(np.isfinite(trade_values).sum()),
        "positive_days": int(np.sum(values > 0)),
        "negative_days": int(np.sum(values < 0)),
    }


def _normal_cdf(value: float) -> float:
    return NormalDist().cdf(value)


def deflated_sharpe_probability(
    returns: pd.Series | np.ndarray,
    *,
    trials: int,
    annualization_days: int = 365,
) -> float:
    """Approximate DSR probability using HAC Sharpe and an effective trial count."""

    values = np.asarray(returns, dtype=float)
    values = values[np.isfinite(values)]
    if len(values) < 3 or trials < 1:
        return 0.0
    sharpe = autocorrelation_adjusted_sharpe(values, annualization_days=annualization_days)
    skew = float(pd.Series(values).skew()) if len(values) > 2 else 0.0
    kurtosis = float(pd.Series(values).kurt()) if len(values) > 3 else 0.0
    expected_max = math.sqrt(max(0.0, 2.0 * math.log(max(trials, 2))))
    variance = max(
        1e-12,
        (1.0 - skew * sharpe + ((kurtosis + 3.0) / 4.0) * sharpe * sharpe) / len(values),
    )
    return _normal_cdf((sharpe - expected_max) / math.sqrt(variance))


def probability_of_backtest_overfitting(strategy_matrix: np.ndarray) -> float:
    values = np.asarray(strategy_matrix, dtype=float)
    if values.ndim != 2 or values.shape[0] < 2 or values.shape[1] < 2:
        return 0.0
    values = np.nan_to_num(values, nan=0.0)
    periods = values.shape[1]
    half = periods // 2
    if half < 1:
        return 0.0
    failures = 0
    total = 0
    seen: set[tuple[int, ...]] = set()
    total_combinations = math.comb(periods, half)
    if total_combinations <= 256:
        candidate_splits = combinations(range(periods), half)
    else:
        # Exhaustive CSCV becomes combinatorially impossible for daily data.
        # Use a deterministic subset while retaining complementary splits.
        rng = np.random.default_rng(11)
        candidate_splits = (
            tuple(sorted(rng.choice(periods, size=half, replace=False))) for _ in range(256)
        )
    for in_sample in candidate_splits:
        out_sample = tuple(index for index in range(periods) if index not in in_sample)
        key = min(tuple(in_sample), tuple(out_sample))
        if key in seen or not out_sample:
            continue
        seen.add(key)
        selected = int(np.argmax(values[:, in_sample].mean(axis=1)))
        out = values[:, out_sample].mean(axis=1)
        failures += int(out[selected] < np.median(out))
        total += 1
    return float(failures / total) if total else 0.0


def concentration_stress(
    trades: pd.DataFrame,
    *,
    return_column: str = "net_return",
    time_column: str = "exit_time",
) -> dict[str, float]:
    if trades.empty or return_column not in trades:
        return {"without_best_five": 0.0, "without_best_month": 0.0}
    values = pd.to_numeric(trades[return_column], errors="coerce").fillna(0.0)
    without_best = float(values.sort_values(ascending=False).iloc[5:].sum())
    data = trades.copy()
    data[time_column] = pd.to_datetime(data[time_column], utc=True, errors="coerce")
    data["_month"] = data[time_column].dt.to_period("M").astype(str)
    monthly = data.assign(_return=values).groupby("_month")["_return"].sum()
    best_month = monthly.idxmax() if not monthly.empty else None
    without_month = float(monthly.drop(index=best_month).sum()) if best_month is not None else 0.0
    return {"without_best_five": without_best, "without_best_month": without_month}


def evaluate_gates(
    metrics: dict[str, float | int],
    *,
    config: V3Config,
    trials: int,
    returns: pd.Series | np.ndarray,
    trades: pd.DataFrame,
    fold_returns: list[float] | None = None,
    strategy_matrix: np.ndarray | None = None,
    seed_metrics: list[dict[str, float | int]] | None = None,
    required_trades: int | None = None,
) -> V3GateResult:
    reasons: list[str] = []
    trade_count = int(metrics.get("closed_trades", 0))
    if required_trades is not None and trade_count < required_trades:
        reasons.append(f"closed_trades<{required_trades}")
    if float(metrics.get("total_return", 0.0)) <= 0:
        reasons.append("non_positive_return")
    if float(metrics.get("profit_factor", 0.0)) < config.minimum_profit_factor:
        reasons.append("profit_factor_below_gate")
    if float(metrics.get("max_drawdown", 1.0)) > config.maximum_drawdown:
        reasons.append("drawdown_above_gate")
    sharpe = float(metrics.get("sharpe_hac", 0.0))
    if sharpe < config.minimum_sharpe:
        reasons.append("sharpe_below_gate")
    ci_low, ci_high = block_bootstrap_sharpe_ci(returns)
    if ci_low <= config.minimum_sharpe_ci_lower:
        reasons.append("sharpe_ci_lower_not_positive")
    dsr = deflated_sharpe_probability(returns, trials=trials)
    pbo = probability_of_backtest_overfitting(strategy_matrix) if strategy_matrix is not None else 1.0
    if dsr < config.minimum_dsr_probability:
        reasons.append("dsr_below_gate")
    if pbo > config.maximum_pbo:
        reasons.append("pbo_above_gate")
    if fold_returns is not None and sum(value >= 0 for value in fold_returns) < config.minimum_nonnegative_folds:
        reasons.append("too_few_nonnegative_folds")
    concentration = concentration_stress(trades)
    if concentration["without_best_five"] <= 0:
        reasons.append("dependent_on_best_five_trades")
    if concentration["without_best_month"] <= 0:
        reasons.append("dependent_on_best_month")
    if seed_metrics is not None:
        passing = sum(
            float(item.get("total_return", 0.0)) >= 0 and float(item.get("max_drawdown", 1.0)) <= config.maximum_drawdown
            for item in seed_metrics
        )
        if passing < 4:
            reasons.append("seed_stability_failure")
    output = dict(metrics)
    output.update(
        {
            "sharpe_ci_lower": ci_low,
            "sharpe_ci_upper": ci_high,
            "dsr_probability": dsr,
            "pbo": pbo,
            "without_best_five": concentration["without_best_five"],
            "without_best_month": concentration["without_best_month"],
        }
    )
    return V3GateResult(passed=not reasons, reasons=tuple(reasons), metrics=output)
