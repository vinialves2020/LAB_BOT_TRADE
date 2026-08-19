from __future__ import annotations

import re

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.v3.config import V3Config
from bottrade.v3.costs import CostModel
from bottrade.v3.domain import StrategyFamily
from bottrade.v3.strategies.base import emit_candidates, require_columns

_TREND = re.compile(r"^trend_ema_(\d+)_(\d+)_h(\d+)$")


class TrendGenerator:
    family = StrategyFamily.TREND

    def __init__(self, config: V3Config, costs: CostModel) -> None:
        self.config = config
        self.costs = costs

    def generate(self, frame: pd.DataFrame, asset: Asset) -> pd.DataFrame:
        outputs: list[pd.DataFrame] = []
        for variant in self.config.strategy_variants.get(self.family.value, ()):
            match = _TREND.match(variant)
            if match is None:
                raise ValueError(f"invalid trend variant: {variant}")
            fast, slow, horizon = (int(value) for value in match.groups())
            fast_col = f"ema_{fast}h"
            slow_col = f"ema_{slow}h"
            return_col = f"return_{fast}h"
            require_columns(frame, [fast_col, slow_col, return_col, "close"])
            slow_slope = pd.to_numeric(frame[slow_col], errors="coerce") - pd.to_numeric(
                frame[slow_col], errors="coerce"
            ).shift(6)
            fast_value = pd.to_numeric(frame[fast_col], errors="coerce")
            slow_value = pd.to_numeric(frame[slow_col], errors="coerce")
            close = pd.to_numeric(frame["close"], errors="coerce")
            returns = pd.to_numeric(frame[return_col], errors="coerce")
            volatility = pd.to_numeric(frame["ewma_volatility_1h"], errors="coerce")
            mask = (fast_value > slow_value) & (slow_slope > 0) & (close > fast_value) & (returns > 0)
            strength = (fast_value / slow_value.replace(0, np.nan) - 1.0) / volatility.replace(0, np.nan)
            outputs.append(
                emit_candidates(
                    frame=frame,
                    asset=asset,
                    family=self.family,
                    variant_id=variant,
                    mask=mask,
                    signal_strength=strength,
                    config=self.config,
                    costs=self.costs,
                )
            )
        return pd.concat(outputs, ignore_index=True) if outputs else pd.DataFrame()
