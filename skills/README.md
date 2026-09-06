# HERMES Skills

Each skill is an instruction contract for one specialist sub-agent. Skills are provider-neutral Markdown so they can be used with different model providers or agent runtimes.

## Installed skills

- `orchestrator.md` — routes work, prioritizes tasks, and requests approvals.
- `research-briefing.md` — produces evidence-aware research.
- `lead-qualification.md` — ranks prospects and prepares outreach drafts.
- `content-repurposing.md` — turns source material into channel-specific content.
- `delivery-quality-assurance.md` — reviews deliverables before release.
- `finance-review.md` — prepares financial analysis without executing money movement.
- `support-triage.md` — classifies support requests and escalates sensitive issues.

A skill must never imply that an agent completed an external action unless a tool receipt confirms it.
