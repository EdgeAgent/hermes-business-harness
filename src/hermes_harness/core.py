from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Harness:
    root: Path

    def load_json(self, relative: str) -> dict[str, Any]:
        path = self.root / relative
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)

    def validate(self) -> list[str]:
        errors: list[str] = []
        required = [
            "config/agents.json",
            "config/policy.json",
            "config/distribution.json",
            "workflows/workflows.json",
        ]
        for relative in required:
            path = self.root / relative
            if not path.exists():
                errors.append(f"missing: {relative}")
                continue
            try:
                self.load_json(relative)
            except json.JSONDecodeError as exc:
                errors.append(f"invalid JSON in {relative}: {exc}")

        if errors:
            return errors

        agents = self.load_json("config/agents.json")["agents"]
        agent_ids = {agent["id"] for agent in agents}
        workflows = self.load_json("workflows/workflows.json")["workflows"]
        for workflow in workflows:
            if workflow["agent"] not in agent_ids:
                errors.append(f"workflow {workflow['id']} references unknown agent {workflow['agent']}")
            if "request_approval" not in workflow["stages"] and workflow["approval_required"]:
                errors.append(f"workflow {workflow['id']} requires approval but has no approval stage")
        return errors

    def status(self) -> dict[str, int]:
        agents = self.load_json("config/agents.json")["agents"]
        workflows = self.load_json("workflows/workflows.json")["workflows"]
        skills = list((self.root / "skills").glob("*.md"))
        prompts = list((self.root / "prompts").glob("*.md"))
        return {"agents": len(agents), "skills": len(skills), "prompts": len(prompts), "workflows": len(workflows)}

    def run_workflow(self, workflow_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        workflows = self.load_json("workflows/workflows.json")["workflows"]
        workflow = next((item for item in workflows if item["id"] == workflow_id), None)
        if workflow is None:
            raise ValueError(f"unknown workflow: {workflow_id}")
        missing = [key for key in workflow["inputs"] if key not in payload]
        if missing:
            raise ValueError(f"missing inputs for {workflow_id}: {', '.join(missing)}")

        # The loop is intentionally explicit: every stage creates an auditable checkpoint.
        checkpoints = []
        state = "started"
        for stage in workflow["stages"]:
            state = "needs_review" if stage == "request_approval" else stage
            checkpoints.append({"stage": stage, "state": state})
        return {
            "workflow_id": workflow_id,
            "workflow_name": workflow["name"],
            "agent": workflow["agent"],
            "status": "needs_review" if workflow["approval_required"] else "ready",
            "approval_required": workflow["approval_required"],
            "payload": payload,
            "checkpoints": checkpoints,
            "next_action": "human approval" if workflow["approval_required"] else "provider execution",
        }
