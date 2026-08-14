from __future__ import annotations

import logging
import time
from typing import Any

import httpx

LOGGER = logging.getLogger(__name__)


class PublicHttpClient:
    """Small synchronous client with bounded retries for public, idempotent reads."""

    def __init__(self, timeout_seconds: int = 30, max_retries: int = 4) -> None:
        self.max_retries = max_retries
        self.client = httpx.Client(
            timeout=httpx.Timeout(timeout_seconds),
            follow_redirects=True,
            headers={"User-Agent": "bottrade-research/0.1"},
        )

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> PublicHttpClient:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def get(self, url: str, *, params: dict[str, Any] | None = None) -> httpx.Response:
        last_error: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                response = self.client.get(url, params=params)
                if response.status_code == 429 or response.status_code >= 500:
                    response.raise_for_status()
                if response.status_code >= 400:
                    response.raise_for_status()
                return response
            except (httpx.TransportError, httpx.HTTPStatusError) as exc:
                last_error = exc
                retryable = isinstance(exc, httpx.TransportError)
                if isinstance(exc, httpx.HTTPStatusError):
                    retryable = exc.response.status_code == 429 or exc.response.status_code >= 500
                if not retryable or attempt >= self.max_retries:
                    raise
                delay = min(2**attempt, 8)
                LOGGER.warning("Public request failed; retrying in %ss: %s", delay, url)
                time.sleep(delay)
        raise RuntimeError("unreachable retry loop") from last_error

    def get_json(self, url: str, *, params: dict[str, Any] | None = None) -> Any:
        return self.get(url, params=params).json()

    def get_bytes(self, url: str, *, params: dict[str, Any] | None = None) -> bytes:
        return self.get(url, params=params).content
