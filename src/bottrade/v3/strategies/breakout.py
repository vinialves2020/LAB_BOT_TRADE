from __future__ import annotations

import re

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.v3.config import V3Config
from bottrade.v3.costs import CostModel
from bottrade.v3.domain import StrategyFamily
from bottrade.v3.strategies.base import emit_candidates, require_columns

_BREAKOUT = re.compile(r"^breakout_(24|72)h_h(6|12)$")


class BreakoutGenerator:
    family = StrategyFamily.BREAKOUT

    def __init__(self, config: V3Config, costs: CostModel) -> None:
        self.config = config
        self.costs = costs

    def generate(self, frame: pd.DataFrame, asset: Asset) -> pd.DataFrame:
        outputs: list[pd.DataFrame] = []
        data = frame.sort_values("as_of").copy()
        for variant in self.config.strategy_variants.get(self.family.value, ()):
            match = _BREAKOUT.match(variant)
            if match is None:
                raise ValueError(f"invalid breakout variant: {variant}")
            window, _horizon = (int(value) for value in match.groups())
            require_columns(
                data,
                [
                    "high",
                    "close",
                    "volume_z_24h",
                    "intrahour_close_position",
                    "volatility_24h",
                ],
            )
            prior_high = pd.to_numeric(data["high"], errors="coerce").rolling(window).max().shift(1)
            volume_z = pd.to_numeric(data["volume_z_24h"], errors="coerce")
            close = pd.to_numeric(data["close"], errors="coerce")
            close_position = pd.to_numeric(data["intrahour_close_position"], errors="coerce")
            vol = pd.to_numeric(data["volatility_24h"], errors="coerce")
            prior_vol = vol.shift(1)
            trailing_q = prior_vol.rolling(168, min_periods=30).quantile(0.35)
            mask = (
                (close > prior_high)
                & (volume_z >= 1.0)
                & (close_position >= 0.75)
                & (prior_vol <= trailing_q)
            )
            strength = (close / prior_high.replace(0, np.nan) - 1.0) / vol.replace(0, np.nan)
            outputs.append(
                emit_candidates(
                    frame=data,
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
