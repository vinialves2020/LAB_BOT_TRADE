"""Small, deterministic overfitting diagnostics used by the V2 report."""

from __future__ import annotations

from itertools import combinations

import numpy as np
from scipy.stats import norm, skew


def deflated_sharpe_probability(
    returns: np.ndarray,
    *,
    trials: int = 1,
    benchmark_sharpe: float = 0.0,
    annualization_factor: float = 1.0,
) -> float:
    """Approximate the probability that a Sharpe exceeds a trial-adjusted benchmark.

    This is a conservative diagnostic, not a guarantee of future profitability.
    It accounts for sample size, skewness, excess kurtosis and the number of
    configurations tried.  Returns should be daily (or another consistent period).
    """

    values = np.asarray(returns, dtype=float)
    values = values[np.isfinite(values)]
    if len(values) < 3:
        return 0.0
    std = float(np.std(values, ddof=1))
    if std <= 0 or not np.isfinite(std):
        return 0.0
    raw_sharpe = float(np.mean(values) / std * annualization_factor)
    skewness = float(skew(values, bias=False)) if len(values) > 3 else 0.0
    centered = values - np.mean(values)
    fourth = float(np.mean(centered**4) / (np.var(values, ddof=0) ** 2)) if std > 0 else 3.0
    excess_kurtosis = fourth - 3.0
    sample_sharpe = float(np.mean(values) / std)
    variance = (
        1.0
        - skewness * sample_sharpe
        + ((excess_kurtosis + 2.0) / 4.0) * sample_sharpe**2
    ) / max(len(values) - 1, 1)
    standard_error = np.sqrt(max(variance, 1e-12)) * annualization_factor
    trial_count = max(int(trials), 1)
    # A Bonferroni-style normal quantile is intentionally conservative and
    # deterministic for small research runs.
    adjusted_benchmark = float(benchmark_sharpe) + norm.ppf(
        1.0 - 0.5 / trial_count
    ) * standard_error
    probability = float(norm.cdf((raw_sharpe - adjusted_benchmark) / standard_error))
    return float(np.clip(probability, 0.0, 1.0))


def probability_of_backtest_overfitting(strategy_returns: np.ndarray) -> float:
    """Estimate PBO with a compact combinatorial symmetric cross-validation.

    ``strategy_returns`` has shape ``[strategies, periods]``.  Each split selects
    the best in-sample strategy and checks whether it is below the median of the
    out-of-sample strategies.  Fewer than two strategies or two periods returns
    zero because no comparison is identifiable.
    """

    values = np.asarray(strategy_returns, dtype=float)
    if values.ndim != 2 or values.shape[0] < 2 or values.shape[1] < 2:
        return 0.0
    values = np.where(np.isfinite(values), values, 0.0)
    periods = values.shape[1]
    half = periods // 2
    if half < 1:
        return 0.0
    candidates = list(combinations(range(periods), half))
    # Symmetric pairs avoid double-counting a split and its complement.
    seen: set[tuple[int, ...]] = set()
    failures = 0
    total = 0
    all_indices = set(range(periods))
    for in_sample_tuple in candidates:
        out_sample_tuple = tuple(sorted(all_indices - set(in_sample_tuple)))
        key = min(in_sample_tuple, out_sample_tuple)
        if key in seen or not out_sample_tuple:
            continue
        seen.add(key)
        in_sample = values[:, in_sample_tuple].mean(axis=1)
        out_sample = values[:, out_sample_tuple].mean(axis=1)
        selected = int(np.argmax(in_sample))
        if out_sample[selected] < float(np.median(out_sample)):
            failures += 1
        total += 1
    return float(failures / total) if total else 0.0


def v2_statistical_gates(
    returns: np.ndarray,
    strategy_matrix: np.ndarray,
    *,
    trials: int,
    max_pbo: float = 0.20,
    min_dsr_probability: float = 0.95,
) -> dict[str, float | bool]:
    dsr = deflated_sharpe_probability(returns, trials=trials, annualization_factor=np.sqrt(365.0))
    pbo = probability_of_backtest_overfitting(strategy_matrix)
    return {
        "deflated_sharpe_probability": dsr,
        "pbo": pbo,
        "passed": bool(dsr >= min_dsr_probability and pbo <= max_pbo),
    }
