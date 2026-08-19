from __future__ import annotations

import io
import logging
import zipfile
from datetime import UTC, datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any

import httpx
import pandas as pd

from bottrade.config import MarketConfig
from bottrade.data.http import PublicHttpClient
from bottrade.data.manifest import DatasetManifest
from bottrade.domain import Asset, ExchangeRules, MarketQuote
from bottrade.utils import sha256_bytes, utc_now

LOGGER = logging.getLogger(__name__)

KLINE_COLUMNS = [
    "open_time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "quote_volume",
    "trade_count",
    "taker_buy_base_volume",
    "taker_buy_quote_volume",
    "ignore",
]


def _to_timestamp(values: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(values, errors="coerce")
    maximum = numeric.dropna().max() if not numeric.dropna().empty else 0
    unit = "us" if maximum >= 100_000_000_000_000 else "ms"
    return pd.to_datetime(numeric, unit=unit, utc=True, errors="coerce")


def _interval_timedelta(interval: str | int | float) -> pd.Timedelta:
    if isinstance(interval, (int, float)):
        return pd.Timedelta(hours=float(interval))
    value = str(interval).strip().lower()
    if value.endswith("m"):
        return pd.Timedelta(minutes=float(value.removesuffix("m")))
    if value.endswith("h"):
        return pd.Timedelta(hours=float(value.removesuffix("h")))
    if value.endswith("d"):
        return pd.Timedelta(days=float(value.removesuffix("d")))
    raise ValueError(f"unsupported Binance interval: {interval}")


def normalize_klines(frame: pd.DataFrame, interval_hours: int | float | str = 1) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(columns=[*KLINE_COLUMNS[:-1], "as_of", "is_closed"])
    data = frame.copy()
    data.columns = KLINE_COLUMNS
    data["open_time"] = _to_timestamp(data["open_time"])
    data["close_time"] = _to_timestamp(data["close_time"])
    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "quote_volume",
        "trade_count",
        "taker_buy_base_volume",
        "taker_buy_quote_volume",
    ]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data["as_of"] = data["open_time"] + _interval_timedelta(interval_hours)
    now = pd.Timestamp.now(tz="UTC")
    data["is_closed"] = data["as_of"] <= now
    data = data.drop(columns=["ignore"])
    data = data.dropna(subset=["open_time", "open", "high", "low", "close"])
    return data.sort_values("open_time").drop_duplicates("open_time", keep="last").reset_index(drop=True)


class BinanceClient:
    def __init__(self, config: MarketConfig, http: PublicHttpClient | None = None) -> None:
        self.config = config
        self.http = http or PublicHttpClient(
            timeout_seconds=config.request_timeout_seconds,
            max_retries=config.max_retries,
        )
        self._owns_http = http is None

    def close(self) -> None:
        if self._owns_http:
            self.http.close()

    def _archive_url(self, symbol: str, year: int, month: int, interval: str | None = None) -> str:
        interval = interval or self.config.interval
        filename = f"{symbol}-{interval}-{year:04d}-{month:02d}.zip"
        return (
            f"{self.config.archive_base_url}/data/spot/monthly/klines/"
            f"{symbol}/{interval}/{filename}"
        )

    def fetch_archive_month(
        self, symbol: str, year: int, month: int, *, interval: str | None = None
    ) -> tuple[pd.DataFrame, str, str]:
        interval = interval or self.config.interval
        url = self._archive_url(symbol, year, month, interval)
        payload = self.http.get_bytes(url)
        checksum_url = f"{url}.CHECKSUM"
        try:
            expected = self.http.get(checksum_url).text.strip().split()[0].lower()
            actual = sha256_bytes(payload)
            if expected and expected != actual:
                raise ValueError(f"checksum mismatch for {url}: expected {expected}, got {actual}")
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code != 404:
                raise
            LOGGER.warning("Checksum was not available for %s", url)
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            csv_names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
            if len(csv_names) != 1:
                raise ValueError(f"expected exactly one CSV in {url}, found {csv_names}")
            with archive.open(csv_names[0]) as handle:
                frame = pd.read_csv(handle, header=None)
        return normalize_klines(frame, interval), url, sha256_bytes(payload)

    def fetch_klines_rest(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        *,
        limit: int = 1000,
        interval: str | None = None,
    ) -> pd.DataFrame:
        url = f"{self.config.rest_base_url}/api/v3/klines"
        start_ms = int(start.astimezone(UTC).timestamp() * 1000)
        end_ms = int(end.astimezone(UTC).timestamp() * 1000)
        rows: list[list[Any]] = []
        cursor = start_ms
        interval = interval or self.config.interval
        interval_ms = int(_interval_timedelta(interval).total_seconds() * 1000)
        while cursor <= end_ms:
            batch = self.http.get_json(
                url,
                params={
                    "symbol": symbol,
                    "interval": interval,
                    "startTime": cursor,
                    "endTime": end_ms,
                    "limit": limit,
                },
            )
            if not batch:
                break
            rows.extend(batch)
            next_cursor = int(batch[-1][0]) + interval_ms
            if next_cursor <= cursor:
                raise RuntimeError("Binance pagination did not advance")
            cursor = next_cursor
            if len(batch) < limit:
                break
        return normalize_klines(pd.DataFrame(rows), interval)

    def fetch_recent_klines(
        self, symbol: str, limit: int = 500, *, interval: str | None = None
    ) -> pd.DataFrame:
        url = f"{self.config.rest_base_url}/api/v3/klines"
        interval = interval or self.config.interval
        rows = self.http.get_json(
            url,
            params={"symbol": symbol, "interval": interval, "limit": limit},
        )
        return normalize_klines(pd.DataFrame(rows), interval)

    def sync_history(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        output_path: Path,
        manifest: DatasetManifest,
        interval: str | None = None,
    ) -> pd.DataFrame:
        interval = interval or self.config.interval
        periods = pd.period_range(start=start.date(), end=end.date(), freq="M")
        frames: list[pd.DataFrame] = []
        source_urls: list[str] = []
        for period in periods:
            month_start = datetime(period.year, period.month, 1, tzinfo=UTC)
            next_month = (pd.Timestamp(month_start) + pd.offsets.MonthBegin(1)).to_pydatetime()
            month_end = min(end, next_month - timedelta(microseconds=1))
            try:
                frame, url, _ = self.fetch_archive_month(
                    symbol, period.year, period.month, interval=interval
                )
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code != 404:
                    raise
                LOGGER.info("Monthly archive missing; using REST for %s %s", symbol, period)
                frame = self.fetch_klines_rest(
                    symbol, max(start, month_start), month_end, interval=interval
                )
                url = f"{self.config.rest_base_url}/api/v3/klines"
            frames.append(frame)
            source_urls.append(url)
        combined = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
        if not combined.empty:
            start_ts = pd.Timestamp(start)
            end_ts = pd.Timestamp(end)
            combined = combined[
                (combined["open_time"] >= start_ts) & (combined["open_time"] <= end_ts)
            ]
            combined = combined.sort_values("open_time").drop_duplicates("open_time", keep="last")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        combined.to_parquet(output_path, index=False)
        manifest.add_file(
            source=f"binance_spot_klines_{interval}",
            url=",".join(dict.fromkeys(source_urls)),
            path=output_path,
            rows=len(combined),
            min_event_time=combined["open_time"].min().isoformat() if not combined.empty else None,
            max_event_time=combined["open_time"].max().isoformat() if not combined.empty else None,
            schema={column: str(dtype) for column, dtype in combined.dtypes.items()},
        )
        return combined

    def exchange_rules(self, symbol: str) -> ExchangeRules:
        url = f"{self.config.rest_base_url}/api/v3/exchangeInfo"
        payload = self.http.get_json(url, params={"symbol": symbol})
        symbols = payload.get("symbols", [])
        if len(symbols) != 1:
            raise ValueError(f"exchangeInfo did not return one symbol for {symbol}")
        filters = {entry["filterType"]: entry for entry in symbols[0]["filters"]}
        lot = filters["LOT_SIZE"]
        market_lot = filters.get("MARKET_LOT_SIZE", {})
        price = filters["PRICE_FILTER"]
        notional = filters.get("NOTIONAL") or filters.get("MIN_NOTIONAL") or {}
        lot_minimum = Decimal(lot["minQty"])
        lot_maximum = Decimal(lot["maxQty"])
        lot_step = Decimal(lot["stepSize"])
        market_minimum = Decimal(str(market_lot.get("minQty", "0")))
        market_maximum = Decimal(str(market_lot.get("maxQty", "0")))
        market_step = Decimal(str(market_lot.get("stepSize", "0")))
        return ExchangeRules(
            symbol=symbol,
            min_quantity=max(lot_minimum, market_minimum),
            max_quantity=(
                min(lot_maximum, market_maximum)
                if market_maximum > 0
                else lot_maximum
            ),
            step_size=max(lot_step, market_step),
            tick_size=Decimal(price["tickSize"]),
            min_notional=Decimal(str(notional.get("minNotional", "0"))),
        )

    def market_quote(self, asset: Asset, depth_levels: int = 20) -> MarketQuote:
        ticker_url = f"{self.config.rest_base_url}/api/v3/ticker/bookTicker"
        depth_url = f"{self.config.rest_base_url}/api/v3/depth"
        ticker = self.http.get_json(ticker_url, params={"symbol": asset.value})
        depth = self.http.get_json(depth_url, params={"symbol": asset.value, "limit": depth_levels})
        return MarketQuote(
            asset=asset,
            as_of=utc_now(),
            bid=Decimal(ticker["bidPrice"]),
            ask=Decimal(ticker["askPrice"]),
            bid_quantity=Decimal(ticker["bidQty"]),
            ask_quantity=Decimal(ticker["askQty"]),
            bids=tuple((Decimal(price), Decimal(qty)) for price, qty in depth.get("bids", [])),
            asks=tuple((Decimal(price), Decimal(qty)) for price, qty in depth.get("asks", [])),
        )

    def server_time(self) -> datetime:
        url = f"{self.config.rest_base_url}/api/v3/time"
        value = self.http.get_json(url)["serverTime"]
        return datetime.fromtimestamp(int(value) / 1000, tz=UTC)


def validate_hourly_continuity(frame: pd.DataFrame) -> list[pd.Timestamp]:
    if frame.empty:
        return []
    observed = pd.DatetimeIndex(frame["open_time"].sort_values().unique())
    expected = pd.date_range(observed.min(), observed.max(), freq="1h", tz="UTC")
    return list(expected.difference(observed))
