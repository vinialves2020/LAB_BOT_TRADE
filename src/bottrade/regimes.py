from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def classify_regimes(reference_close: pd.Series) -> pd.DataFrame:
    """Create descriptive, non-trading regime labels from the evaluated price path.

    These labels are only used after predictions have been frozen. They must never be
    passed back into training or threshold calibration.
    """

    close = pd.to_numeric(reference_close, errors="coerce").replace(0, np.nan)
    log_close = np.log(close)
    hourly_return = log_close.diff()
    trend = log_close.diff(72)
    volatility = hourly_return.rolling(168, min_periods=72).std(ddof=0)
    expanding_median = volatility.expanding(min_periods=168).median().shift(1)
    high_volatility = volatility > expanding_median

    trend_scale = hourly_return.rolling(168, min_periods=72).std(ddof=0) * np.sqrt(72)
    normalized_trend = trend / trend_scale.replace(0, np.nan)
    direction = np.select(
        [normalized_trend > 0.75, normalized_trend < -0.75],
        ["trend_up", "trend_down"],
        default="sideways",
    )
    volatility_label = np.where(high_volatility.fillna(False), "high_vol", "normal_vol")
    return pd.DataFrame(
        {
            "trend_regime": direction,
            "volatility_regime": volatility_label,
            "combined_regime": [
                f"{trend_name}__{vol_name}"
                for trend_name, vol_name in zip(direction, volatility_label, strict=True)
            ],
        },
        index=reference_close.index,
    )


def analyze_regimes(
    frame: pd.DataFrame, strategy_returns: pd.Series, positions: pd.Series
) -> dict[str, dict[str, float | int]]:
    if len(frame) != len(strategy_returns) or len(frame) != len(positions):
        raise ValueError("frame, strategy_returns and positions must have equal length")
    regimes = classify_regimes(frame["reference_close"].reset_index(drop=True))
    analysis = regimes.copy()
    analysis["return"] = pd.Series(strategy_returns).reset_index(drop=True).fillna(0.0)
    analysis["position"] = pd.Series(positions).reset_index(drop=True).fillna(0.0)
    result: dict[str, dict[str, float | int]] = {}
    for label, group in analysis.groupby("combined_regime", sort=True):
        values = group["return"].astype(float)
        result[str(label)] = {
            "hours": int(len(group)),
            "total_return": float((1.0 + values.clip(lower=-0.999999)).prod() - 1.0),
            "mean_hourly_return": float(values.mean()),
            "hourly_volatility": float(values.std(ddof=1)) if len(values) > 1 else 0.0,
            "positive_hour_fraction": float((values > 0).mean()),
            "exposure": float(group["position"].mean()),
        }
    return result


def aggregate_regime_analyses(
    records: list[dict[str, dict[str, float | int]]],
) -> dict[str, dict[str, Any]]:
    labels = sorted({label for record in records for label in record})
    output: dict[str, dict[str, Any]] = {}
    for label in labels:
        rows = [record[label] for record in records if label in record]
        output[label] = {
            "folds": len(rows),
            "hours": int(sum(int(row["hours"]) for row in rows)),
            "median_total_return": float(np.median([row["total_return"] for row in rows])),
            "median_exposure": float(np.median([row["exposure"] for row in rows])),
            "median_hourly_volatility": float(
                np.median([row["hourly_volatility"] for row in rows])
            ),
        }
    return output
