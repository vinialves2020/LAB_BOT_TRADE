from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from bottrade.data.alternative import AlternativeMeClient
from bottrade.data.binance import BinanceClient
from bottrade.data.coinmetrics import CoinMetricsClient
from bottrade.data.defillama import DefiLlamaClient
from bottrade.data.http import PublicHttpClient
from bottrade.domain import Asset


@pytest.mark.integration
def test_all_public_sources_return_expected_schemas(app_config) -> None:
    with PublicHttpClient(30, 2) as http:
        binance = BinanceClient(app_config.market, http=http)
        market = binance.fetch_recent_klines(Asset.BTCUSDT.value, limit=5)
        assert len(market) == 5
        assert not market[market["is_closed"]].empty
        assert binance.exchange_rules(Asset.BTCUSDT.value).step_size > 0
        assert binance.market_quote(Asset.BTCUSDT, 5).ask > 0

        sentiment = AlternativeMeClient(http).fear_and_greed()
        assert {"event_time", "available_at", "sentiment_fear_greed"} <= set(
            sentiment.columns
        )
        end = datetime.now(UTC)
        coinmetrics = CoinMetricsClient(http).asset_metrics(
            "btc", end - timedelta(days=7), end
        )
        assert len(coinmetrics) >= 5
        solana = DefiLlamaClient(http).solana_metrics()
        assert {
            "onchain_ecosystem_tvl_usd",
            "onchain_stablecoin_supply_usd",
            "onchain_dex_volume_usd",
            "onchain_ecosystem_fees_usd",
        } <= set(solana.columns)
