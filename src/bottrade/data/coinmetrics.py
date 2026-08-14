from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import pandas as pd

from bottrade.data.http import PublicHttpClient

COMMUNITY_BASE_URL = "https://community-api.coinmetrics.io/v4"
COMMUNITY_METRICS = ("AdrActCnt", "TxCnt", "SplyCur")


class CoinMetricsClient:
    def __init__(self, http: PublicHttpClient) -> None:
        self.http = http

    def asset_metrics(
        self,
        asset: str,
        start: datetime,
        end: datetime,
        delay_hours: int = 24,
    ) -> pd.DataFrame:
        url = f"{COMMUNITY_BASE_URL}/timeseries/asset-metrics"
        params: dict[str, Any] | None = {
            "assets": asset.lower(),
            "metrics": ",".join(COMMUNITY_METRICS),
            "frequency": "1d",
            "start_time": start.date().isoformat(),
            "end_time": end.date().isoformat(),
            "page_size": 10000,
            "paging_from": "start",
        }
        rows: list[dict[str, Any]] = []
        while params is not None:
            payload = self.http.get_json(url, params=params)
            rows.extend(payload.get("data", []))
            next_url = payload.get("next_page_url")
            if next_url:
                url = next_url
                params = None
                payload = self.http.get_json(url)
                rows.extend(payload.get("data", []))
                while payload.get("next_page_url"):
                    payload = self.http.get_json(payload["next_page_url"])
                    rows.extend(payload.get("data", []))
            break
        frame = pd.DataFrame(rows)
        columns = [
            "event_time",
            "available_at",
            "onchain_active_addresses",
            "onchain_transaction_count",
            "onchain_current_supply",
        ]
        if frame.empty:
            return pd.DataFrame(columns=columns)
        frame["event_time"] = pd.to_datetime(frame["time"], utc=True).dt.floor("D")
        frame["available_at"] = frame["event_time"] + timedelta(hours=delay_hours)
        rename = {
            "AdrActCnt": "onchain_active_addresses",
            "TxCnt": "onchain_transaction_count",
            "SplyCur": "onchain_current_supply",
        }
        frame = frame.rename(columns=rename)
        for column in rename.values():
            frame[column] = pd.to_numeric(frame.get(column), errors="coerce")
        return frame[columns].sort_values("event_time").drop_duplicates("event_time", keep="last")
