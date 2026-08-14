from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from bottrade.config import AppConfig, load_config


def synthetic_market(periods: int = 600, start: str = "2024-01-01") -> dict[str, pd.DataFrame]:
    rng = np.random.default_rng(42)
    times = pd.date_range(start, periods=periods, freq="1h", tz="UTC")
    output: dict[str, pd.DataFrame] = {}
    for index, (symbol, base_price) in enumerate(
        [("BTCUSDT", 40_000.0), ("ETHUSDT", 2_000.0), ("SOLUSDT", 100.0)]
    ):
        noise = rng.normal(0.0001 + index * 0.00001, 0.004 + index * 0.001, periods)
        close = base_price * np.exp(np.cumsum(noise))
        open_price = np.r_[close[0], close[:-1]]
        high = np.maximum(open_price, close) * (1 + rng.uniform(0, 0.003, periods))
        low = np.minimum(open_price, close) * (1 - rng.uniform(0, 0.003, periods))
        volume = rng.lognormal(5 + index, 0.3, periods)
        output[symbol] = pd.DataFrame(
            {
                "open_time": times,
                "open": open_price,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
                "close_time": times + pd.Timedelta(hours=1) - pd.Timedelta(milliseconds=1),
                "quote_volume": volume * close,
                "trade_count": rng.integers(100, 5000, periods),
                "taker_buy_base_volume": volume * rng.uniform(0.35, 0.65, periods),
                "taker_buy_quote_volume": volume * close * rng.uniform(0.35, 0.65, periods),
                "as_of": times + pd.Timedelta(hours=1),
                "is_closed": True,
            }
        )
    return output


@pytest.fixture
def app_config(tmp_path: Path) -> AppConfig:
    config = load_config(create_dirs=False)
    config.project.data_dir = tmp_path / "data"
    config.project.artifact_dir = tmp_path / "artifacts"
    config.project.report_dir = tmp_path / "reports"
    config.runtime.database_url = f"sqlite:///{(tmp_path / 'paper.db').as_posix()}"
    config.ensure_directories()
    return config


@pytest.fixture
def market_frames() -> dict[str, pd.DataFrame]:
    return synthetic_market()
