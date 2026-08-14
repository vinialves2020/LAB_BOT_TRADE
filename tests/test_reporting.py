from __future__ import annotations

from bottrade.reporting import write_model_card


def test_model_card_labels_development_metrics_as_pre_holdout(tmp_path) -> None:
    output = tmp_path / "MODEL_CARD.md"
    write_model_card(
        {
            "asset": "ETHUSDT",
            "family": "transformer",
            "protocol_phase": "development",
            "selection_metrics": {"total_return": 0.01},
        },
        output,
    )
    text = output.read_text(encoding="utf-8")
    assert "## Teste walk-forward pré-holdout" in text
    assert "## Holdout congelado" not in text


def test_model_card_labels_holdout_metrics_as_frozen_holdout(tmp_path) -> None:
    output = tmp_path / "MODEL_CARD.md"
    write_model_card(
        {
            "asset": "ETHUSDT",
            "family": "transformer",
            "protocol_phase": "holdout",
            "holdout_metrics": {"total_return": 0.01},
        },
        output,
    )
    assert "## Holdout congelado" in output.read_text(encoding="utf-8")
