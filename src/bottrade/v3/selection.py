from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def _hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@dataclass(frozen=True, slots=True)
class V3SelectionLock:
    protocol_version: str
    protocol_hash: str
    config_hash: str
    holdout_start: str
    holdout_end: str
    holdout_claimed: bool
    assets: dict[str, dict[str, Any]]
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "protocol_version": self.protocol_version,
            "protocol_hash": self.protocol_hash,
            "config_hash": self.config_hash,
            "holdout_start": self.holdout_start,
            "holdout_end": self.holdout_end,
            "holdout_claimed": self.holdout_claimed,
            "assets": self.assets,
            "created_at": self.created_at,
        }


def create_selection_lock(
    *,
    path: str | Path,
    protocol_path: str | Path,
    config_path: str | Path,
    holdout_start: str,
    holdout_end: str,
    assets: dict[str, dict[str, Any]],
) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(f"selection lock already exists: {destination}")
    lock = V3SelectionLock(
        protocol_version="v3",
        protocol_hash=_hash_file(Path(protocol_path)),
        config_hash=_hash_file(Path(config_path)),
        holdout_start=holdout_start,
        holdout_end=holdout_end,
        holdout_claimed=False,
        assets=assets,
        created_at=datetime.now(UTC).isoformat(),
    )
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_text(json.dumps(lock.to_dict(), indent=2, sort_keys=True), encoding="utf-8")
    temporary.replace(destination)
    return destination


def load_selection_lock(path: str | Path) -> dict[str, Any]:
    destination = Path(path)
    data = json.loads(destination.read_text(encoding="utf-8"))
    required = {
        "protocol_version",
        "protocol_hash",
        "config_hash",
        "holdout_start",
        "holdout_end",
        "holdout_claimed",
        "assets",
    }
    missing = required - set(data)
    if missing:
        raise ValueError(f"selection lock missing fields: {sorted(missing)}")
    if data["protocol_version"] != "v3":
        raise ValueError("selection lock is not V3")
    return data


def claim_holdout(path: str | Path) -> dict[str, Any]:
    destination = Path(path)
    data = load_selection_lock(destination)
    if bool(data["holdout_claimed"]):
        raise RuntimeError("holdout has already been claimed")
    data["holdout_claimed"] = True
    data["holdout_claimed_at"] = datetime.now(UTC).isoformat()
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    temporary.replace(destination)
    return data
