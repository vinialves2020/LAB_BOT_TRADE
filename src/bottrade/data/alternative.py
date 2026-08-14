from __future__ import annotations

from datetime import timedelta

import pandas as pd

from bottrade.data.http import PublicHttpClient

FEAR_GREED_URL = "https://api.alternative.me/fng/"


class AlternativeMeClient:
    def __init__(self, http: PublicHttpClient) -> None:
        self.http = http

    def fear_and_greed(self, delay_hours: int = 24, *, limit: int = 0) -> pd.DataFrame:
        payload = self.http.get_json(
            FEAR_GREED_URL,
            params={"limit": max(0, int(limit)), "format": "json"},
        )
        metadata = payload.get("metadata", {})
        if metadata.get("error"):
            raise RuntimeError(f"Alternative.me returned an error: {metadata['error']}")
        frame = pd.DataFrame(payload.get("data", []))
        if frame.empty:
            return pd.DataFrame(
                columns=["event_time", "available_at", "sentiment_fear_greed", "classification"]
            )
        frame["event_time"] = pd.to_datetime(
            pd.to_numeric(frame["timestamp"]), unit="s", utc=True
        ).dt.floor("D")
        frame["available_at"] = frame["event_time"] + timedelta(hours=delay_hours)
        frame["sentiment_fear_greed"] = pd.to_numeric(frame["value"], errors="coerce")
        frame = frame.rename(columns={"value_classification": "classification"})
        return (
            frame[["event_time", "available_at", "sentiment_fear_greed", "classification"]]
            .sort_values("event_time")
            .drop_duplicates("event_time", keep="last")
            .reset_index(drop=True)
        )
