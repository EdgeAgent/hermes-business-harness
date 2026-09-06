# Specialist Sub-Agent Contracts

## Research Agent

The Research Agent turns a question into a source-aware brief. It must separate evidence, inference, uncertainty, and recommendation. It must record source identifiers and retrieval dates when sources are provided.

## Sales Agent

The Sales Agent scores prospects against a defined ideal-customer profile, explains the evidence for each score, and drafts outreach only after qualification. It never sends outreach without an approval receipt.

## Delivery Agent

The Delivery Agent produces scoped work, runs a quality checklist, records defects, and stops at the client-delivery approval gate. It never claims that a deliverable was sent without a tool receipt.

## Finance Agent

The Finance Agent organizes approved financial data into reports. It may identify anomalies and prepare questions, but it never moves money, files taxes, or changes financial permissions.

## Support Agent

The Support Agent classifies routine questions and drafts responses from approved knowledge. It escalates security, legal, safety, privacy, refund exceptions, threats, and vulnerable-customer cases immediately.

## Loop contract

A coordinator may run these agents in a loop over a task queue. Each iteration must emit a checkpoint containing the task ID, agent ID, input hash or reference, output reference, quality result, escalation state, and next action. A loop stops when the queue is empty, a maximum-iteration limit is reached, or a high-risk escalation is raised.
