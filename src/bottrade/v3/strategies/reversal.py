from __future__ import annotations

import re

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.v3.config import V3Config
from bottrade.v3.costs import CostModel
from bottrade.v3.domain import StrategyFamily
from bottrade.v3.strategies.base import emit_candidates, require_columns

_REVERSAL = re.compile(r"^reversal_(\d+)h_z(2|25)_h(\d+)$")


class ReversalGenerator:
    family = StrategyFamily.REVERSAL

    def __init__(self, config: V3Config, costs: CostModel) -> None:
        self.config = config
        self.costs = costs

    def generate(self, frame: pd.DataFrame, asset: Asset) -> pd.DataFrame:
        outputs: list[pd.DataFrame] = []
        for variant in self.config.strategy_variants.get(self.family.value, ()):
            match = _REVERSAL.match(variant)
            if match is None:
                raise ValueError(f"invalid reversal variant: {variant}")
            lookback = int(match.group(1))
            threshold = float(match.group(2)) / 10.0
            return_col = f"return_{lookback}h"
            require_columns(
                frame,
                [
                    return_col,
                    "ewma_volatility_1h",
                    "intrahour_drawdown",
                    "intrahour_last_return",
                    "intrahour_close_position",
                ],
            )
            returns = pd.to_numeric(frame[return_col], errors="coerce")
            volatility = pd.to_numeric(frame["ewma_volatility_1h"], errors="coerce")
            normalized = returns / (volatility * np.sqrt(lookback)).replace(0, np.nan)
            drawdown = pd.to_numeric(frame["intrahour_drawdown"], errors="coerce")
            last_return = pd.to_numeric(frame["intrahour_last_return"], errors="coerce")
            close_position = pd.to_numeric(frame["intrahour_close_position"], errors="coerce")
            mask = (
                (normalized <= -threshold)
                & (drawdown <= -volatility)
                & (last_return > 0)
                & (close_position >= 0.35)
            )
            strength = (-normalized).clip(lower=0) + last_return / volatility.replace(0, np.nan)
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
