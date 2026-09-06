from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import Harness


def repo_root() -> Path:
    current = Path.cwd()
    if (current / "config").exists() and (current / "workflows").exists():
        return current
    return Path(__file__).resolve().parents[2]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hermes", description="HERMES AI-native business harness")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("validate")
    sub.add_parser("skills")
    sub.add_parser("workflows")
    run = sub.add_parser("run", help="render an auditable workflow run")
    run.add_argument("workflow")
    run.add_argument("--input", required=True, help="path to JSON input payload")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    harness = Harness(repo_root())
    try:
        if args.command == "status":
            print(json.dumps(harness.status(), indent=2))
        elif args.command == "validate":
            errors = harness.validate()
            if errors:
                print("Validation failed:")
                print("\n".join(f"- {error}" for error in errors))
                return 1
            print("HERMES configuration is valid.")
        elif args.command == "skills":
            for path in sorted((harness.root / "skills").glob("*.md")):
                print(path.stem)
        elif args.command == "workflows":
            for workflow in harness.load_json("workflows/workflows.json")["workflows"]:
                approval = "approval required" if workflow["approval_required"] else "no approval required"
                print(f"{workflow['id']}: {workflow['name']} ({approval})")
        elif args.command == "run":
            with Path(args.input).open(encoding="utf-8") as handle:
                payload = json.load(handle)
            print(json.dumps(harness.run_workflow(args.workflow, payload), indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
