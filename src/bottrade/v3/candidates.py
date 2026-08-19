from __future__ import annotations

import pandas as pd

from bottrade.domain import Asset
from bottrade.v3.config import V3Config
from bottrade.v3.costs import CostModel
from bottrade.v3.strategies import BreakoutGenerator, ReversalGenerator, TrendGenerator


def build_candidates(
    frame: pd.DataFrame,
    *,
    asset: Asset,
    config: V3Config,
    costs: CostModel | None = None,
    families: tuple[str, ...] | None = None,
) -> pd.DataFrame:
    """Build all pre-registered candidates for one asset.

    The function deliberately returns every candidate.  Selection happens only
    in calibration or in the meta-model, never while building the dataset.
    """

    cost_model = costs or CostModel(
        fallback_fee_bps_per_leg=config.fallback_fee_bps_per_leg,
        fallback_spread_bps=config.fallback_spread_bps,
        fallback_slippage_bps=config.fallback_slippage_bps,
    )
    enabled = set(families or ("trend", "reversal", "breakout"))
    generators = tuple(
        generator
        for family, generator in (
            ("trend", TrendGenerator(config, cost_model)),
            ("reversal", ReversalGenerator(config, cost_model)),
            ("breakout", BreakoutGenerator(config, cost_model)),
        )
        if family in enabled
    )
    outputs = [generator.generate(frame, asset) for generator in generators]
    outputs = [item for item in outputs if not item.empty]
    if not outputs:
        return pd.DataFrame()
    result = pd.concat(outputs, ignore_index=True)
    if result["candidate_id"].duplicated().any():
        raise AssertionError("candidate_id collision detected")
    future_columns = {
        "future_close",
        "future_close_3h",
        "future_close_6h",
        "future_close_12h",
        "target_raw_return",
        "mfe",
        "mae",
        "net_return_1x",
    }
    leaked = future_columns.intersection(result.columns)
    if leaked:
        raise AssertionError(f"candidate frame contains future columns: {sorted(leaked)}")
    return result.sort_values(["as_of", "asset", "variant_id"]).reset_index(drop=True)
