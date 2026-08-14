from __future__ import annotations

import pandas as pd

from bottrade.data.binance import KLINE_COLUMNS, normalize_klines
from bottrade.data.defillama import DefiLlamaClient


def _row(timestamp: int) -> list:
    return [timestamp, 1, 2, 0.5, 1.5, 10, timestamp + 3_599_999, 15, 100, 6, 9, 0]


def test_binance_parser_supports_milliseconds_and_microseconds() -> None:
    milliseconds = 1_735_689_600_000
    microseconds = milliseconds * 1000
    parsed_ms = normalize_klines(pd.DataFrame([_row(milliseconds)]))
    parsed_us = normalize_klines(pd.DataFrame([_row(microseconds)]))
    assert parsed_ms.loc[0, "open_time"] == parsed_us.loc[0, "open_time"]
    assert parsed_ms.loc[0, "as_of"] == pd.Timestamp("2025-01-01T01:00:00Z")
    assert list(parsed_ms.columns) == [*KLINE_COLUMNS[:-1], "as_of", "is_closed"]


def test_defillama_stablecoin_nested_value() -> None:
    assert DefiLlamaClient._stablecoin_value({"peggedUSD": 12.5}) == 12.5
    assert DefiLlamaClient._stablecoin_value({"a": 1, "b": 2}) == 3
    assert DefiLlamaClient._stablecoin_value(None) is None
