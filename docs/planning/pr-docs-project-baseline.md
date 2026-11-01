# PR: docs/project-baseline

## Title

`docs: establish project baseline, standards, and v0.1.0 plan`

## Summary

This PR establishes the public project baseline for `qgis-cn-planning`:

- project scope and public/private boundary;
- standards baseline and citation rules;
- curriculum coverage matrix for village/town planning, territorial spatial planning, and heritage conservation;
- contribution and review rules;
- licence-status record and third-party notices;
- release policy and versioning;
- issue templates and pull-request template;
- draft v0.1.0 milestone and issue plan.

No styles, templates, symbols, sample data, or PDFs are added in this PR.

## Related issue

Refs #1. This PR establishes the baseline documentation; Issue #1 remains open for the Beijing profile deliverable.

## Type of change

- [x] Documentation (`docs`)
- [x] Maintenance/tooling (`chore`)
- [ ] New resource (`feat`)
- [ ] Correction (`fix`)

## Standards and sources

The PR records, but does not reproduce:

- 《国土空间规划制图规范》（2025 征求意见稿）
- CJJ/T 97-2003
- GB/T 10609.1
- Beijing DB11/T 1947-2021, DB11/T 1948-2021, DB11/T 1949-2021
- 山东省市县国土空间总体规划制图指南

Curriculum references:

- Tongji University 2024 undergraduate planning programme
- Tongji University 2025 graduate programmes (083300, 085300)
- Tsinghua University undergraduate planning programme
- Nanjing University graduate planning programme

## Licence status

- Final licence: **not selected**.
- No licence grant is implied.
- Third-party assets are referenced, not vendored.
- The PR does not add any asset with unresolved permission.

## Validation

- [x] Markdown files reviewed for broken relative links (manual).
- [x] No absolute local paths in public files.
- [x] No credentials, tokens, personal data, or restricted data.
- [x] `git status` checked before staging.
- [ ] GitHub Actions (not configured at baseline).

## Reviewer decisions needed

1. Confirm the final licence model.
2. Confirm whether the v0.1.0 scope should include a Beijing profile only, or additional profiles.
3. Confirm whether the first release should ship an installer script or a QGIS plugin.
4. Confirm the repository owner and default branch before the remote is created.

## Out of scope

- Styles, templates, symbols, sample projects, PDFs.
- A QGIS plugin.
- A final licence text.
- A release tag.

## Checklist

- [x] Scope fits `docs/scope.md`.
- [x] Branch name is `docs/project-baseline`.
- [x] Commit messages use the type prefix.
- [x] No credentials, personal data, restricted data, or standard full texts.
- [x] No absolute local paths, caches, or QGIS profile files.
- [x] Changelog updated.
- [x] I have not merged this PR or published a release.
