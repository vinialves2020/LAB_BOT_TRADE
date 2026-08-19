"""Version 3 research protocol.

V3 is intentionally additive.  The V1/V2 modules remain the source of truth
for reproducing the earlier experiments; this package contains the new
candidate-strategy and meta-model protocol.
"""

from bottrade.v3.config import V3Config, load_v3_config
from bottrade.v3.domain import CandidateOutcome, StrategyFamily, TradeCandidate

__all__ = [
    "CandidateOutcome",
    "StrategyFamily",
    "TradeCandidate",
    "V3Config",
    "load_v3_config",
]
