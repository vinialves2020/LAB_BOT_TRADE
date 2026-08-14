from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from bottrade.domain import RunStage
from bottrade.evaluation import FinalGateEvaluator
from bottrade.storage import Storage


def test_paper_phase_state_and_incomplete_final_gate(app_config) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    start = datetime.now(UTC) - timedelta(days=1)
    canary = storage.start_paper_phase(
        RunStage.CANARY,
        started_at=start,
        duration_days=app_config.paper.canary_days,
    )
    assert canary["phase"] == "canary"
    with pytest.raises(ValueError, match="already active"):
        storage.start_paper_phase(
            RunStage.CANARY,
            started_at=start,
            duration_days=app_config.paper.canary_days,
        )
    storage.finish_paper_phase(RunStage.CANARY, ended_at=datetime.now(UTC))
    storage.reset_paper_state(app_config)
    storage.start_paper_phase(
        RunStage.PAPER,
        started_at=datetime.now(UTC),
        duration_days=app_config.paper.official_paper_days,
    )
    evaluation = FinalGateEvaluator(app_config, storage).evaluate()
    assert evaluation["eligible_for_future_real_review"] is False
    assert "official_paper_duration_incomplete" in evaluation["global_reasons"]
