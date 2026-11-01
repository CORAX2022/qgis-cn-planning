# Licence status

**Status: not finalized. No licence is granted for this repository or its contents yet.**

This file records the licence decision process. It is not a licence grant. Do not reuse, redistribute, or describe the project as open source until a final decision is recorded and the corresponding licence texts are added.

## Candidate model

The maintainers are considering a split licence model:

| Material | Candidate | Status |
|---|---|---|
| Source code, scripts, tests | Apache License 2.0 | Proposed, not applied |
| QGIS styles, symbols, layout templates | Creative Commons Attribution 4.0 International (CC BY 4.0) | Proposed, not applied |
| Documentation | CC BY 4.0 | Proposed, not applied |
| Sample data | Separate licence per dataset | Not decided |
| Third-party assets | Their original licences | Must be recorded individually |

The final decision must consider:

- Compatibility with QGIS and third-party assets.
- Whether attribution is required for derived cartographic resources.
- Whether a more permissive licence (for example CC0) is preferable for symbols.
- Whether code and content should use different licences.
- Whether a Contributor Licence Agreement or Developer Certificate of Origin is needed.

## Rules until the decision is final

1. Do not add a root `LICENSE` file that implies a grant.
2. Do not add licence headers to new files as if the licence were final.
3. Record the source and licence of every third-party asset in `NOTICE.md`.
4. Do not vendor assets whose licence is unknown or incompatible.
5. Do not describe the project as "open source" in release notes until the licence is applied.

## Asset inventory

The inventory will be maintained as assets are added. At baseline it is empty because no styles, templates, symbols, or data have been committed.

| Asset path | Type | Source | Licence | Status |
|---|---|---|---|---|
| — | — | — | — | No assets committed |

## Questions for maintainers

- Should the code use Apache-2.0 or MIT?
- Should styles and templates use CC BY 4.0 or CC0?
- Should documentation use CC BY 4.0 or CC0?
- Should sample data be excluded from the repository and distributed separately?
- Is a trademark or name-use policy needed to prevent implied endorsement?
