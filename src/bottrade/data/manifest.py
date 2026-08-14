from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from bottrade.utils import content_hash, sha256_file, utc_now


@dataclass(frozen=True, slots=True)
class SourceFile:
    source: str
    url: str
    path: str
    sha256: str
    rows: int
    min_event_time: str | None
    max_event_time: str | None
    schema: dict[str, str]


@dataclass(slots=True)
class DatasetManifest:
    dataset: str
    schema_version: str
    collected_at: datetime = field(default_factory=utc_now)
    sources: list[SourceFile] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def data_version(self) -> str:
        return content_hash(
            [
                self.dataset,
                self.schema_version,
                [asdict(source) for source in self.sources],
                self.metadata,
            ]
        )[:20]

    def add_file(
        self,
        *,
        source: str,
        url: str,
        path: Path,
        rows: int,
        min_event_time: str | None,
        max_event_time: str | None,
        schema: dict[str, str],
    ) -> None:
        self.sources.append(
            SourceFile(
                source=source,
                url=url,
                path=str(path),
                sha256=sha256_file(path),
                rows=rows,
                min_event_time=min_event_time,
                max_event_time=max_event_time,
                schema=dict(sorted(schema.items())),
            )
        )

    def write(self, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = asdict(self)
        payload["collected_at"] = self.collected_at.isoformat()
        payload["data_version"] = self.data_version
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(
            json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str),
            encoding="utf-8",
        )
        temporary.replace(path)
        return path


def read_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))
