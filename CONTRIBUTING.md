# Contributing

## Before you start

- Check existing issues and pull requests. If a related issue exists, comment there instead of opening a duplicate.
- For a new resource, open a **Resource request** issue first and describe the standard, source, licence, and intended use.
- For a defect, open a **Bug report** with the QGIS version, operating system, template/style file, and a minimal reproduction.
- For a standards question, open a **Standard alignment** issue and cite the document, edition, clause, and page.

## Branch naming

Use a short, descriptive branch:

- `feat/<topic>` — new styles, symbols, templates, examples, or tools
- `fix/<topic>` — corrections to existing resources
- `docs/<topic>` — documentation and project records
- `chore/<topic>` — repository maintenance and tooling

One topic per branch. Do not mix raw source material, environment files, and finished resources in one commit.

## Commit messages

Use a type prefix and a concrete summary:

```text
docs: define project scope and Beijing adaptation basis
feat: add village land-use teaching styles
fix: correct A1 title-block field alignment
chore: add issue and pull-request templates
```

Keep each commit to one explainable change. Avoid committing generated caches, screenshots that are not part of the documentation, or local QGIS profiles.

## Resource submission requirements

Every contributed style, symbol, template, or sample must include:

1. **Purpose** — which planning domain and sheet type it supports.
2. **Standard or source** — document title, edition/date, clause/page where applicable, or a documented design rationale.
3. **Licence** — the licence of the resource and of any third-party asset embedded in it. If the licence is unknown, do not submit the asset; open an issue first.
4. **QGIS compatibility** — tested QGIS version(s), for example 3.40 LTR and 4.0.
5. **Fonts** — font family and fallback; do not assume a proprietary font is installed.
6. **Data** — sample data must be synthetic, public-domain, or explicitly licensed for redistribution. Do not submit personal, confidential, or restricted spatial data.
7. **Validation** — run the repository validation script when available and paste the result.
8. **Preview** — one small PNG or PDF preview for visual review, with no personal or restricted content.

## What not to submit

- Access tokens, passwords, keys, `.env` files, or credential stores.
- Proprietary institute title blocks, CAD templates, ArcGIS projects, or standard full texts without written permission.
- Personal information, student records, unpublished client data, or restricted spatial data.
- Local absolute paths, machine names, QGIS profile dumps, caches, or editor backups.
- Large raw datasets. Keep examples small and licence-clear.

## Pull requests

A pull request should:

- Link the issue it resolves.
- State what changed and why.
- List the standards/sources used.
- Record licence status for every new asset.
- Include validation output and a preview where relevant.
- Call out anything the reviewer must decide.
- Keep unrelated changes out of the same PR.

Use the repository pull-request template. Draft PRs are welcome for early review.

## Review checks

Reviewers will check:

- Scope fit and naming.
- Standard/source traceability.
- Licence compatibility and third-party notices.
- QGIS compatibility and font fallback.
- XML validity, missing SVG paths, absolute paths, and page sizes.
- Visual hierarchy, legend completeness, label overlap, and title-block alignment.
- Whether the change is reproducible from the repository.

## Public/private boundary

The repository is the public source of truth. Local execution notes, private data inventories, and machine-specific paths belong outside version control. If sensitive material has already entered Git history, stop the push and report it; do not rewrite shared history without the maintainer's decision.

## Communication

Be specific. Use file names, line numbers, page numbers, screenshots, and command output. "Looks fine" is not a review.
