# ADR 0001 — Project baseline and source of truth

- Status: Proposed
- Date: 2026-11-01
- Decision owners: project maintainers

## Context

The project needs a durable record for resource source files, documentation, change history, task management, and releases. Local folders and chat history are insufficient: they do not provide reviewable diffs, issue tracking, or reproducible releases.

The project also handles standards, third-party templates, and potentially restricted data. Public and private material must be separated.

## Decision

1. **Git is the source of truth** for resource source files, documentation, and change history.
2. **GitHub Issues** track tasks, defects, data gaps, and resource requests.
3. **GitHub Pull Requests** are the review and merge mechanism.
4. **GitHub Milestones** track stage goals; the first is `v0.1.0`.
5. **Git tags and GitHub Releases** publish formal versions and downloadable bundles.
6. **Project-manager instructions are converted into repository issues and acceptance criteria**, not kept only in chat.
7. The repository uses a lightweight branch model:
   - `main` — reviewed, usable state
   - `feat/<topic>` — new resources or capabilities
   - `fix/<topic>` — corrections
   - `docs/<topic>` — documentation and project records
   - `chore/<topic>` — maintenance and tooling
8. Public content and local execution records are separated. Local records are not committed.
9. No duplicate repository is created when an existing project repository can be used. History is not reset, force-pushed, or overwritten.
10. The licence decision remains open. No licence grant is implied until a final decision and licence texts are recorded.

## Consequences

- Contributors need a GitHub account and review process.
- The repository needs issue templates, a pull-request template, a changelog, and a release policy.
- Sensitive or proprietary material must stay outside the repository.
- Local-only execution notes must not be referenced by absolute path in public documents.
- A release is a deliberate act with a checklist, not a side effect of a commit.

## Alternatives considered

- **Local folder only** — rejected: no reviewable history, no issue tracking, no release record.
- **Chat history as record** — rejected: not durable, not searchable by contributors, not auditable.
- **Single monolithic branch** — rejected: makes review and release control difficult.
- **Git LFS by default** — rejected for now: the expected resources are small text files; data policy should be decided after measuring size and change frequency.

## Follow-up

- Create the `v0.1.0` milestone.
- Create the initial issue set.
- Decide the final licence model.
- Add validation and release tooling.
- Record any local-only material and its exclusion reason outside the repository.
