from __future__ import annotations

from collections.abc import Iterable
from dataclasses import asdict, dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True, slots=True)
class PerformanceMetrics:
    total_return: float
    annualized_return: float
    sharpe: float
    sortino: float
    max_drawdown: float
    calmar: float
    profit_factor: float
    closed_trades: int
    hit_rate: float
    turnover: float
    transaction_cost: float
    exposure: float
    mean_daily_return: float
    daily_volatility: float

    def to_dict(self) -> dict[str, float | int]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class PredictiveMetrics:
    mae: float
    rmse: float
    spearman: float
    directional_accuracy: float
    samples: int

    def to_dict(self) -> dict[str, float | int]:
        return asdict(self)


def calculate_predictive(
    actual: Iterable[float], predictions: Iterable[float]
) -> PredictiveMetrics:
    truth = np.asarray(list(actual), dtype=float)
    forecast = np.asarray(list(predictions), dtype=float)
    if truth.shape != forecast.shape:
        raise ValueError("actual and predictions must have the same shape")
    valid = np.isfinite(truth) & np.isfinite(forecast)
    truth = truth[valid]
    forecast = forecast[valid]
    if not len(truth):
        return PredictiveMetrics(0.0, 0.0, 0.0, 0.0, 0)
    error = forecast - truth
    if len(truth) > 1 and np.std(truth) > 0 and np.std(forecast) > 0:
        spearman = float(pd.Series(truth).corr(pd.Series(forecast), method="spearman"))
        if not np.isfinite(spearman):
            spearman = 0.0
    else:
        spearman = 0.0
    return PredictiveMetrics(
        mae=float(np.mean(np.abs(error))),
        rmse=float(np.sqrt(np.mean(error**2))),
        spearman=spearman,
        directional_accuracy=float(np.mean(np.sign(truth) == np.sign(forecast))),
        samples=int(len(truth)),
    )


def compound_returns(returns: pd.Series) -> pd.Series:
    clean = returns.fillna(0.0).clip(lower=-0.999999)
    return (1.0 + clean).cumprod()


def daily_returns(hourly_returns: pd.Series, timestamps: pd.Series | pd.DatetimeIndex) -> pd.Series:
    index = pd.DatetimeIndex(pd.to_datetime(timestamps, utc=True))
    values = pd.Series(hourly_returns.to_numpy(dtype=float), index=index)
    return (1.0 + values.fillna(0.0)).resample("1D").prod() - 1.0


def max_drawdown_from_equity(equity: pd.Series) -> float:
    if equity.empty:
        return 0.0
    drawdown = equity / equity.cummax().replace(0, np.nan) - 1.0
    return abs(float(drawdown.min())) if not drawdown.dropna().empty else 0.0


def annualized_sharpe(returns: pd.Series, annualization_days: int = 365) -> float:
    clean = returns.dropna()
    if len(clean) < 2:
        return 0.0
    std = float(clean.std(ddof=1))
    if std <= 0 or not np.isfinite(std):
        return 0.0
    return float(np.sqrt(annualization_days) * clean.mean() / std)


def annualized_sortino(returns: pd.Series, annualization_days: int = 365) -> float:
    clean = returns.dropna()
    downside = clean[clean < 0]
    if len(clean) < 2 or len(downside) < 2:
        return 0.0
    downside_deviation = float(np.sqrt((downside**2).mean()))
    if downside_deviation <= 0 or not np.isfinite(downside_deviation):
        return 0.0
    return float(np.sqrt(annualization_days) * clean.mean() / downside_deviation)


def profit_factor(trade_returns: Iterable[float]) -> float:
    values = np.asarray(list(trade_returns), dtype=float)
    gains = float(values[values > 0].sum())
    losses = abs(float(values[values < 0].sum()))
    if losses == 0:
        # A finite sentinel keeps JSON/SQL exports standards-compliant while preserving
        # the intended ordering of an all-winning sample. It is not evidence of robustness.
        return gains / 1e-12 if gains > 0 else 0.0
    return gains / losses


def calculate_performance(
    *,
    hourly_returns: pd.Series,
    timestamps: pd.Series | pd.DatetimeIndex,
    positions: pd.Series,
    turnover: float,
    transaction_cost: float = 0.0,
    trade_returns: Iterable[float],
    annualization_days: int = 365,
) -> PerformanceMetrics:
    equity = compound_returns(hourly_returns)
    daily = daily_returns(hourly_returns, timestamps)
    total = float(equity.iloc[-1] - 1.0) if not equity.empty else 0.0
    periods = max(len(daily), 1)
    annualized = float((1.0 + total) ** (annualization_days / periods) - 1.0) if total > -1 else -1.0
    drawdown = max_drawdown_from_equity(equity)
    sharpe = annualized_sharpe(daily, annualization_days)
    sortino = annualized_sortino(daily, annualization_days)
    trades = list(trade_returns)
    hits = sum(value > 0 for value in trades)
    return PerformanceMetrics(
        total_return=total,
        annualized_return=annualized,
        sharpe=sharpe,
        sortino=sortino,
        max_drawdown=drawdown,
        calmar=annualized / drawdown if drawdown > 0 else 0.0,
        profit_factor=profit_factor(trades),
        closed_trades=len(trades),
        hit_rate=hits / len(trades) if trades else 0.0,
        turnover=float(turnover),
        transaction_cost=float(transaction_cost),
        exposure=float(positions.mean()) if not positions.empty else 0.0,
        mean_daily_return=float(daily.mean()) if not daily.empty else 0.0,
        daily_volatility=float(daily.std(ddof=1)) if len(daily) > 1 else 0.0,
    )
