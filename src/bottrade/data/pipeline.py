from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from bottrade.config import AppConfig
from bottrade.data.alternative import FEAR_GREED_URL, AlternativeMeClient
from bottrade.data.binance import BinanceClient, validate_hourly_continuity
from bottrade.data.coinmetrics import COMMUNITY_BASE_URL, CoinMetricsClient
from bottrade.data.defillama import DefiLlamaClient
from bottrade.data.http import PublicHttpClient
from bottrade.data.manifest import DatasetManifest

LOGGER = logging.getLogger(__name__)
SCHEMA_VERSION = "market-alt-v2"


class DataPipeline:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.raw_dir = config.project.data_dir / "raw"
        self.manifest_dir = config.project.data_dir / "manifests"

    def sync(
        self,
        *,
        start: datetime,
        end: datetime,
        include_alternatives: bool = True,
    ) -> DatasetManifest:
        start = start.astimezone(UTC)
        end = end.astimezone(UTC)
        manifest = DatasetManifest(
            dataset="bottrade-public-sources",
            schema_version=SCHEMA_VERSION,
            metadata={"start": start.isoformat(), "end": end.isoformat()},
        )
        with PublicHttpClient(
            timeout_seconds=self.config.market.request_timeout_seconds,
            max_retries=self.config.market.max_retries,
        ) as http:
            binance = BinanceClient(self.config.market, http=http)
            intervals = list(
                dict.fromkeys([self.config.market.interval, *self.config.market.additional_intervals])
            )
            for interval in intervals:
                for symbol, listing_date in self.config.market.symbols.items():
                    path = self.raw_dir / "market" / f"{symbol}_{interval}.parquet"
                    listed_at = datetime.fromisoformat(listing_date).replace(tzinfo=UTC)
                    frame = binance.sync_history(
                        symbol,
                        max(start, listed_at),
                        end,
                        path,
                        manifest,
                        interval=interval,
                    )
                    missing = validate_hourly_continuity(frame) if interval == "1h" else []
                    if missing:
                        LOGGER.warning(
                            "%s has %s missing hourly candles", symbol, len(missing)
                        )
            if include_alternatives:
                self._sync_alternatives(http, start, end, manifest)
        stamp = manifest.collected_at.strftime("%Y%m%dT%H%M%SZ")
        manifest.write(self.manifest_dir / f"dataset-{stamp}.json")
        manifest.write(self.manifest_dir / "latest.json")
        return manifest

    def _write_alternative(
        self,
        frame: pd.DataFrame,
        path: Path,
        source: str,
        url: str,
        manifest: DatasetManifest,
    ) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_parquet(path, index=False)
        manifest.add_file(
            source=source,
            url=url,
            path=path,
            rows=len(frame),
            min_event_time=frame["event_time"].min().isoformat() if not frame.empty else None,
            max_event_time=frame["event_time"].max().isoformat() if not frame.empty else None,
            schema={column: str(dtype) for column, dtype in frame.dtypes.items()},
        )

    def _sync_alternatives(
        self,
        http: PublicHttpClient,
        start: datetime,
        end: datetime,
        manifest: DatasetManifest,
    ) -> None:
        delay = self.config.features.alternative_delay_hours
        sentiment = AlternativeMeClient(http).fear_and_greed(delay)
        sentiment = sentiment[
            (sentiment["event_time"] >= pd.Timestamp(start).floor("D"))
            & (sentiment["event_time"] <= pd.Timestamp(end).floor("D"))
        ]
        self._write_alternative(
            sentiment,
            self.raw_dir / "alternative" / "fear_greed.parquet",
            "alternative_me_fear_greed",
            FEAR_GREED_URL,
            manifest,
        )
        coinmetrics = CoinMetricsClient(http)
        for asset in ("btc", "eth"):
            frame = coinmetrics.asset_metrics(asset, start, end, delay)
            self._write_alternative(
                frame,
                self.raw_dir / "alternative" / f"{asset}_coinmetrics.parquet",
                f"coinmetrics_{asset}",
                f"{COMMUNITY_BASE_URL}/timeseries/asset-metrics",
                manifest,
            )
        solana = DefiLlamaClient(http).solana_metrics(delay)
        solana = solana[
            (solana["event_time"] >= pd.Timestamp(start).floor("D"))
            & (solana["event_time"] <= pd.Timestamp(end).floor("D"))
        ]
        self._write_alternative(
            solana,
            self.raw_dir / "alternative" / "sol_defillama.parquet",
            "defillama_solana_ecosystem",
            ",".join(
                [
                    DefiLlamaClient.TVL_URL,
                    DefiLlamaClient.STABLECOIN_URL,
                    DefiLlamaClient.DEX_URL,
                    DefiLlamaClient.FEES_URL,
                ]
            ),
            manifest,
        )

    def load_market(self) -> dict[str, pd.DataFrame]:
        frames: dict[str, pd.DataFrame] = {}
        for symbol in self.config.market.symbols:
            path = self.raw_dir / "market" / f"{symbol}_{self.config.market.interval}.parquet"
            if not path.exists():
                raise FileNotFoundError(f"market data missing: {path}; run 'bottrade data sync'")
            frames[symbol] = pd.read_parquet(path)
        return frames

    def load_intrahour(self) -> dict[str, pd.DataFrame]:
        """Load optional 15-minute candles used only as hourly features."""

        frames: dict[str, pd.DataFrame] = {}
        interval = self.config.features.intrahour_interval
        for symbol in self.config.market.symbols:
            path = self.raw_dir / "market" / f"{symbol}_{interval}.parquet"
            frames[symbol] = pd.read_parquet(path) if path.exists() else pd.DataFrame()
        return frames

    def load_derivatives(self) -> dict[str, pd.DataFrame]:
        """Load optional archived futures metrics, if present.

        The downloader deliberately does not synthesize these files from the
        recent-only REST statistics endpoints.  Missing files are represented
        as empty frames and become auditable stale/missing features.
        """

        frames: dict[str, pd.DataFrame] = {}
        for symbol in self.config.market.symbols:
            path = self.raw_dir / "derivatives" / f"{symbol}.parquet"
            frames[symbol] = pd.read_parquet(path) if path.exists() else pd.DataFrame()
        return frames

    def load_alternatives(self) -> tuple[dict[str, pd.DataFrame], pd.DataFrame]:
        mapping = {
            "BTCUSDT": self.raw_dir / "alternative" / "btc_coinmetrics.parquet",
            "ETHUSDT": self.raw_dir / "alternative" / "eth_coinmetrics.parquet",
            "SOLUSDT": self.raw_dir / "alternative" / "sol_defillama.parquet",
        }
        onchain: dict[str, pd.DataFrame] = {}
        for symbol, path in mapping.items():
            onchain[symbol] = pd.read_parquet(path) if path.exists() else pd.DataFrame()
        sentiment_path = self.raw_dir / "alternative" / "fear_greed.parquet"
        sentiment = pd.read_parquet(sentiment_path) if sentiment_path.exists() else pd.DataFrame()
        return onchain, sentiment

    def recent_market(self, limit: int = 500) -> dict[str, pd.DataFrame]:
        with PublicHttpClient(
            timeout_seconds=self.config.market.request_timeout_seconds,
            max_retries=self.config.market.max_retries,
        ) as http:
            binance = BinanceClient(self.config.market, http=http)
            return {
                symbol: binance.fetch_recent_klines(symbol, limit=limit)
                for symbol in self.config.market.symbols
            }

    def recent_intrahour(self, limit: int = 4 * 500) -> dict[str, pd.DataFrame]:
        """Fetch closed 15-minute candles for V2 feature construction.

        This is read-only market data.  A missing response is returned as an
        empty frame so the runtime can fail closed when the feature completeness
        flag is absent rather than opening a position from fabricated bars.
        """

        interval = self.config.features.intrahour_interval
        with PublicHttpClient(
            timeout_seconds=self.config.market.request_timeout_seconds,
            max_retries=self.config.market.max_retries,
        ) as http:
            binance = BinanceClient(self.config.market, http=http)
            return {
                symbol: binance.fetch_recent_klines(symbol, limit=limit, interval=interval)
                for symbol in self.config.market.symbols
            }

    def recent_alternatives(
        self, start: datetime, end: datetime
    ) -> tuple[dict[str, pd.DataFrame], pd.DataFrame]:
        delay = self.config.features.alternative_delay_hours
        with PublicHttpClient(
            timeout_seconds=self.config.market.request_timeout_seconds,
            max_retries=self.config.market.max_retries,
        ) as http:
            sentiment = AlternativeMeClient(http).fear_and_greed(delay, limit=180)
            sentiment = sentiment[
                (sentiment["event_time"] >= pd.Timestamp(start).floor("D"))
                & (sentiment["event_time"] <= pd.Timestamp(end).ceil("D"))
            ]
            coinmetrics = CoinMetricsClient(http)
            onchain = {
                "BTCUSDT": coinmetrics.asset_metrics("btc", start, end, delay),
                "ETHUSDT": coinmetrics.asset_metrics("eth", start, end, delay),
                "SOLUSDT": DefiLlamaClient(http).solana_metrics(delay),
            }
            onchain["SOLUSDT"] = onchain["SOLUSDT"][
                (onchain["SOLUSDT"]["event_time"] >= pd.Timestamp(start).floor("D"))
                & (onchain["SOLUSDT"]["event_time"] <= pd.Timestamp(end).ceil("D"))
            ]
            return onchain, sentiment
