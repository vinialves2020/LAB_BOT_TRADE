"""Small, explicit persistence helpers for the V3 research tables.

The functions in this module deliberately keep the holdout closed by default.
Every table written by the pre-holdout commands receives a sidecar manifest so
that a later report can identify the exact rows, schema and source hash.
"""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pandas as pd

from bottrade.v3.config import V3Config


def _utc_timestamp(value: object) -> pd.Timestamp:
    timestamp = pd.Timestamp(value)
    if timestamp.tzinfo is None:
        return timestamp.tz_localize("UTC")
    return timestamp.tz_convert("UTC")


def ensure_preholdout(
    frame: pd.DataFrame,
    *,
    config: V3Config,
    time_columns: tuple[str, ...] = ("as_of",),
) -> pd.DataFrame:
    """Return a copy containing only rows wholly before the locked holdout.

    ``time_columns`` may include ``entry_time``/``exit_time`` for labels.  A
    row crossing the boundary is rejected rather than truncated, preventing a
    training example from borrowing even one candle from the holdout.
    """

    result = frame.copy()
    holdout_start = _utc_timestamp(config.holdout_start)
    keep = pd.Series(True, index=result.index)
    for column in time_columns:
        if column not in result:
            continue
        values = pd.to_datetime(result[column], utc=True, errors="coerce")
        if values.isna().any() and column == "as_of":
            raise ValueError(f"{column} contains invalid timestamps")
        if values.isna().any():
            result[column] = values
            continue
        keep &= values < holdout_start
        result[column] = values
    # Raw sources may include the later period.  The pre-holdout command
    # filters it out here; it never truncates a surviving row or interpolates
    # an event.  Labels with no entry/exit keep their NaT and remain invalid.
    return result.loc[keep].copy()


def _schema(frame: pd.DataFrame) -> dict[str, str]:
    return {str(column): str(dtype) for column, dtype in frame.dtypes.items()}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_versioned_table(
    frame: pd.DataFrame,
    output: str | Path,
    *,
    config: V3Config,
    table_type: str,
    source_paths: tuple[str | Path, ...] = (),
    holdout_safe: bool = True,
    time_columns: tuple[str, ...] = ("as_of",),
) -> Path:
    """Write parquet plus an auditable JSON manifest next to it."""

    data = ensure_preholdout(frame, config=config, time_columns=time_columns) if holdout_safe else frame.copy()
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    data.to_parquet(destination, index=False)
    sources = []
    for source in source_paths:
        path = Path(source)
        sources.append({"path": str(path), "sha256": _sha256(path) if path.exists() else None})
    manifest = {
        "protocol_version": config.protocol_version,
        "table_type": table_type,
        "created_at": datetime.now(UTC).isoformat(),
        "path": str(destination),
        "sha256": _sha256(destination),
        "rows": int(len(data)),
        "schema": _schema(data),
        "sources": sources,
        "holdout_safe": holdout_safe,
        "holdout_start": config.holdout_start,
        "holdout_end": config.holdout_end,
    }
    destination.with_suffix(destination.suffix + ".manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True, default=str), encoding="utf-8"
    )
    return destination


def read_versioned_table(path: str | Path, *, config: V3Config, holdout_safe: bool = True) -> pd.DataFrame:
    destination = Path(path)
    if not destination.exists():
        raise FileNotFoundError(destination)
    frame = pd.read_parquet(destination)
    if holdout_safe:
        time_columns = tuple(column for column in ("as_of", "entry_time", "exit_time") if column in frame)
        frame = ensure_preholdout(frame, config=config, time_columns=time_columns)
    return frame


def manifest_for(path: str | Path) -> dict[str, Any]:
    destination = Path(path).with_suffix(Path(path).suffix + ".manifest.json")
    if not destination.exists():
        raise FileNotFoundError(destination)
    return json.loads(destination.read_text(encoding="utf-8"))
