from __future__ import annotations

from datetime import timedelta
from typing import Any

import pandas as pd

from bottrade.data.http import PublicHttpClient


class DefiLlamaClient:
    TVL_URL = "https://api.llama.fi/v2/historicalChainTvl/Solana"
    STABLECOIN_URL = "https://stablecoins.llama.fi/stablecoincharts/Solana"
    DEX_URL = "https://api.llama.fi/overview/dexs/Solana"
    FEES_URL = "https://api.llama.fi/overview/fees/Solana"

    def __init__(self, http: PublicHttpClient) -> None:
        self.http = http

    @staticmethod
    def _chart(payload: dict[str, Any], name: str) -> pd.DataFrame:
        values = payload.get("totalDataChart", [])
        frame = pd.DataFrame(values, columns=["timestamp", name])
        if frame.empty:
            return pd.DataFrame(columns=["event_time", name])
        frame["event_time"] = pd.to_datetime(
            pd.to_numeric(frame["timestamp"]), unit="s", utc=True
        ).dt.floor("D")
        frame[name] = pd.to_numeric(frame[name], errors="coerce")
        return frame[["event_time", name]]

    @staticmethod
    def _stablecoin_value(value: Any) -> float | None:
        if isinstance(value, dict):
            if "peggedUSD" in value:
                return float(value["peggedUSD"])
            numbers = [float(item) for item in value.values() if isinstance(item, (int, float))]
            return sum(numbers) if numbers else None
        if isinstance(value, (int, float)):
            return float(value)
        return None

    def solana_metrics(self, delay_hours: int = 24) -> pd.DataFrame:
        tvl_payload = self.http.get_json(self.TVL_URL)
        stable_payload = self.http.get_json(self.STABLECOIN_URL)
        common_params = {"excludeTotalDataChart": "false", "excludeTotalDataChartBreakdown": "true"}
        dex_payload = self.http.get_json(self.DEX_URL, params=common_params)
        fees_payload = self.http.get_json(self.FEES_URL, params=common_params)

        tvl = pd.DataFrame(tvl_payload)
        if tvl.empty:
            tvl = pd.DataFrame(columns=["event_time", "onchain_ecosystem_tvl_usd"])
        else:
            tvl["event_time"] = pd.to_datetime(
                pd.to_numeric(tvl["date"]), unit="s", utc=True
            ).dt.floor("D")
            tvl["onchain_ecosystem_tvl_usd"] = pd.to_numeric(
                tvl["tvl"], errors="coerce"
            )
            tvl = tvl[["event_time", "onchain_ecosystem_tvl_usd"]]

        stable = pd.DataFrame(stable_payload)
        if stable.empty:
            stable = pd.DataFrame(columns=["event_time", "onchain_stablecoin_supply_usd"])
        else:
            stable["event_time"] = pd.to_datetime(
                pd.to_numeric(stable["date"]), unit="s", utc=True
            ).dt.floor("D")
            source_column = (
                "totalCirculatingUSD"
                if "totalCirculatingUSD" in stable.columns
                else "totalCirculating"
            )
            stable["onchain_stablecoin_supply_usd"] = stable[source_column].map(
                self._stablecoin_value
            )
            stable = stable[["event_time", "onchain_stablecoin_supply_usd"]]

        dex = self._chart(dex_payload, "onchain_dex_volume_usd")
        fees = self._chart(fees_payload, "onchain_ecosystem_fees_usd")
        merged = tvl.merge(stable, on="event_time", how="outer")
        merged = merged.merge(dex, on="event_time", how="outer")
        merged = merged.merge(fees, on="event_time", how="outer")
        merged["available_at"] = merged["event_time"] + timedelta(hours=delay_hours)
        columns = ["event_time", "available_at", *[c for c in merged if c.startswith("onchain_")]]
        return merged[columns].sort_values("event_time").drop_duplicates("event_time", keep="last")
