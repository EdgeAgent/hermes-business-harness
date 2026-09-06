import json
from pathlib import Path

from hermes_harness.core import Harness


ROOT = Path(__file__).resolve().parents[1]


def test_configuration_is_valid():
    errors = Harness(ROOT).validate()
    assert errors == []


def test_workflow_loop_emits_every_checkpoint():
    payload = json.loads((ROOT / "examples/weekly-review.json").read_text())
    result = Harness(ROOT).run_workflow("weekly-review", payload)
    assert result["status"] == "needs_review"
    assert [item["stage"] for item in result["checkpoints"]] == [
        "collect", "analyze", "prioritize", "request_approval"
    ]


def test_missing_input_is_rejected():
    try:
        Harness(ROOT).run_workflow("weekly-review", {"period": "x"})
    except ValueError as exc:
        assert "missing inputs" in str(exc)
    else:
        raise AssertionError("missing workflow inputs should fail")
