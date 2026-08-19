from __future__ import annotations

from collections.abc import Mapping

import numpy as np
import pandas as pd

from bottrade.v3.config import V3Config
from bottrade.v3.costs import CostModel
from bottrade.v3.domain import CandidateOutcome


def _normalise_15m(frame: pd.DataFrame) -> pd.DataFrame:
    data = frame.copy()
    if "open_time" not in data:
        raise ValueError("15m frame requires open_time")
    data["open_time"] = pd.to_datetime(data["open_time"], utc=True, errors="coerce")
    if "is_closed" not in data:
        data["is_closed"] = True
    data = data[data["is_closed"].astype(bool)].copy()
    data = data.sort_values("open_time").drop_duplicates("open_time", keep="last")
    return data.reset_index(drop=True)


def _price(row: pd.Series, name: str) -> float:
    value = pd.to_numeric(row.get(name), errors="coerce")
    return float(value) if pd.notna(value) else np.nan


def label_candidates(
    candidates: pd.DataFrame,
    *,
    intrahour: Mapping[str, pd.DataFrame],
    config: V3Config,
    costs: CostModel | None = None,
    holdout_start: str | None = None,
    holdout_end: str | None = None,
) -> pd.DataFrame:
    """Create event labels using only candles after each candidate's as_of."""

    columns = [
        "candidate_id",
        "asset",
        "as_of",
        "strategy_family",
        "variant_id",
        "horizon_hours",
        "signal_strength",
        "take_profit_return",
        "stop_loss_return",
        "entry_time",
        "entry_price",
        "exit_time",
        "exit_price",
        "outcome",
        "gross_return",
        "net_return_1x",
        "net_return_2x",
        "net_return_3x",
        "mfe",
        "mae",
        "bars_to_exit",
        "label_valid",
        "invalid_reason",
    ]
    if candidates.empty:
        return pd.DataFrame(columns=columns)
    cost_model = costs or CostModel(
        fallback_fee_bps_per_leg=config.fallback_fee_bps_per_leg,
        fallback_spread_bps=config.fallback_spread_bps,
        fallback_slippage_bps=config.fallback_slippage_bps,
    )
    def _utc(value: str | None) -> pd.Timestamp | None:
        if value is None:
            return None
        parsed = pd.Timestamp(value)
        return parsed.tz_localize("UTC") if parsed.tzinfo is None else parsed.tz_convert("UTC")

    start = _utc(holdout_start)
    end = _utc(holdout_end)
    normalized = {asset: _normalise_15m(frame) for asset, frame in intrahour.items()}
    time_index = {
        asset: pd.to_datetime(frame["open_time"], utc=True).array.asi8
        for asset, frame in normalized.items()
    }
    rows: list[dict[str, object]] = []
    for candidate in candidates.sort_values("as_of").itertuples(index=False):
        asset = str(candidate.asset)
        as_of_value = pd.Timestamp(candidate.as_of)
        as_of = (
            as_of_value.tz_localize("UTC")
            if as_of_value.tzinfo is None
            else as_of_value.tz_convert("UTC")
        )
        base = {
            "candidate_id": str(candidate.candidate_id),
            "asset": asset,
            "as_of": as_of,
            "strategy_family": str(candidate.strategy_family),
            "variant_id": str(candidate.variant_id),
            "horizon_hours": int(candidate.horizon_hours),
            "signal_strength": float(candidate.signal_strength),
            "take_profit_return": float(candidate.take_profit_return),
            "stop_loss_return": float(candidate.stop_loss_return),
        }
        if (start is not None and as_of < start) or (end is not None and as_of > end):
            rows.append(base | {"outcome": CandidateOutcome.INVALID.value, "label_valid": False, "invalid_reason": "outside_requested_window"})
            continue
        data = normalized.get(asset, pd.DataFrame())
        if data.empty:
            rows.append(base | {"outcome": CandidateOutcome.INVALID.value, "label_valid": False, "invalid_reason": "missing_15m_source"})
            continue
        positions = time_index[asset]
        entry_position = int(np.searchsorted(positions, as_of.value, side="left"))
        if entry_position >= len(data):
            rows.append(base | {"outcome": CandidateOutcome.INVALID.value, "label_valid": False, "invalid_reason": "missing_entry_candle"})
            continue
        entry = data.iloc[entry_position]
        entry_time = pd.Timestamp(entry["open_time"])
        entry_price = _price(entry, "open")
        horizon = int(candidate.horizon_hours)
        expected = horizon * 4
        window = data.iloc[entry_position : entry_position + expected].copy()
        window_times = time_index[asset][entry_position : entry_position + expected]
        if (
            len(window) < expected
            or len(window_times) > 1
            and np.any(np.diff(window_times) != pd.Timedelta(minutes=15).value)
        ):
            rows.append(base | {"entry_time": entry_time, "entry_price": entry_price, "outcome": CandidateOutcome.INVALID.value, "label_valid": False, "invalid_reason": "15m_gap_or_incomplete_horizon"})
            continue
        if not np.isfinite(entry_price) or entry_price <= 0:
            rows.append(base | {"entry_time": entry_time, "entry_price": entry_price, "outcome": CandidateOutcome.INVALID.value, "label_valid": False, "invalid_reason": "invalid_entry_price"})
            continue
        tp = float(candidate.take_profit_return)
        sl = float(candidate.stop_loss_return)
        outcome = CandidateOutcome.TIMEOUT
        exit_time = pd.Timestamp(window.iloc[-1]["open_time"])
        exit_price = _price(window.iloc[-1], "close")
        bars_to_exit = len(window)
        highs = pd.to_numeric(window["high"], errors="coerce").to_numpy(dtype=float)
        lows = pd.to_numeric(window["low"], errors="coerce").to_numpy(dtype=float)
        hit_tp = highs >= entry_price * (1.0 + tp)
        hit_sl = lows <= entry_price * (1.0 + sl)
        hit = np.flatnonzero((hit_tp | hit_sl) & np.isfinite(highs) & np.isfinite(lows))
        if len(hit):
            index = int(hit[0])
            if bool(hit_sl[index]):
                outcome = CandidateOutcome.STOP_LOSS
                exit_price = entry_price * (1.0 + sl)
            else:
                outcome = CandidateOutcome.TAKE_PROFIT
                exit_price = entry_price * (1.0 + tp)
            exit_time = pd.Timestamp(window.iloc[index]["open_time"])
            bars_to_exit = index + 1
        gross = exit_price / entry_price - 1.0 if np.isfinite(exit_price) else np.nan
        snapshot = cost_model.snapshot()
        mfe = float(pd.to_numeric(window["high"], errors="coerce").max() / entry_price - 1.0)
        mae = float(pd.to_numeric(window["low"], errors="coerce").min() / entry_price - 1.0)
        rows.append(
            base
            | {
                "entry_time": entry_time,
                "entry_price": entry_price,
                "exit_time": exit_time,
                "exit_price": exit_price,
                "outcome": outcome.value,
                "gross_return": gross,
                "net_return_1x": cost_model.net_return(gross, snapshot, 1.0),
                "net_return_2x": cost_model.net_return(gross, snapshot, 2.0),
                "net_return_3x": cost_model.net_return(gross, snapshot, 3.0),
                "mfe": mfe,
                "mae": mae,
                "bars_to_exit": bars_to_exit,
                "label_valid": True,
                "invalid_reason": None,
            }
        )
    result = pd.DataFrame(rows)
    for column in ("entry_time", "exit_time"):
        if column in result:
            result[column] = pd.to_datetime(result[column], utc=True, errors="coerce")
    return result.reindex(columns=columns)
