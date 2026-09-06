# HERMES Business Harness

HERMES is a practical operating system for AI-native businesses. It turns business processes into **skills**, routes work through **workflows**, protects sensitive actions with **approval gates**, and evaluates outputs against measurable quality criteria.

> Automate processes, not responsibility.

## What this repository provides

- A local CLI for inspecting the business operating system.
- Versioned agent skills with explicit inputs, outputs, quality checks, and escalation rules.
- Reusable prompt packs for discovery, research, sales, content, delivery, and weekly reviews.
- Workflow definitions that separate preparation from approval and execution.
- A risk-aware approval matrix for financial, legal, security, privacy, and public actions.
- Lightweight evaluation checks that make agent work reviewable.

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
hermes status
hermes validate
hermes run weekly-review --input examples/weekly-review.json
```

The harness is intentionally provider-neutral. It does not send email, publish content, move money, or call an LLM by itself. It prepares structured work and makes approval requirements visible. Connect an LLM or external tools only after reviewing the workflow and risk boundaries.

## Repository map

```text
config/       Business context, agents, risk rules, and metrics
skills/       Reusable operating skills
prompts/      Copy-ready prompt templates
workflows/    Workflow definitions and approval gates
src/          Python CLI and validation engine
tests/        Offline tests
docs/         Product and implementation documentation
```

## Commands

```bash
hermes status       # Show configured agents, skills, workflows, and metrics
hermes validate     # Validate all JSON configuration and workflow contracts
hermes skills       # List installed skills
hermes workflows   # List workflows and approval requirements
hermes run NAME     # Render a workflow brief from a JSON input file
```

## Design principles

1. **One agent, one job.** Avoid vague general-purpose agents.
2. **Structured outputs.** Every workflow has a reviewable output contract.
3. **Human accountability.** High-impact actions always stop at an approval gate.
4. **Evidence over confidence.** Unknowns and assumptions are labeled.
5. **Provider neutrality.** Prompts and contracts are portable across models and tools.
6. **Measure outcomes.** Track business impact, quality, speed, cost, and risk.

## Roadmap

- Add provider adapters behind the existing workflow contracts.
- Add a persistent run ledger and evaluation dataset.
- Add a web dashboard for approvals, metrics, and skill versioning.
- Add vertical packs for agencies, consultants, ecommerce, and professional services.

## License

Apache-2.0. See `LICENSE`.

## Safety

This project is an operating framework, not legal, financial, medical, tax, or security advice. Review outputs before using them in consequential decisions.
