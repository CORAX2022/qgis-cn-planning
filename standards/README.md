# Standards library

This directory is the public entry point for the project's standards record. It is not a repository of copied standard texts.

The project has two layers:

## A. Public standards record

Committed to Git:

- `register.csv` — one row per standard, edition, or guidance document.
- `rules/` — clause-level rules extracted from texts that were actually obtained and read.
- `mappings/` — links between rules and future QGIS resources, plus template candidates.
- `README.md` — this guide.

The public record contains metadata, official links, summaries, clause mappings, and material that is explicitly cleared for redistribution. It does **not** contain local paths, credentials, restricted data, or full texts with unresolved redistribution rights.

## B. Local standards originals

Kept outside Git, under `standards/_local/` (ignored):

- `source/` — PDF, HTML, or other originals obtained from official or public sources.
- `index.csv` — local path, source URL, retrieval date, size, and SHA-256 checksum.

Local originals are for reading and rule extraction. They are not moved into the public repository unless the licence explicitly permits redistribution and the maintainer records that decision.

## Status fields are separate

Do not collapse these into one "status":

1. **Validity** — current, draft, repealed, or to be verified.
2. **Level and jurisdiction** — national, industry, Beijing local, or other local.
3. **Evidence stage** — catalogue found, original obtained, text read, rules extracted.
4. **Redistribution** — unknown, link only, free download without explicit relicense, or cleared.

The register keeps `validity_status`, `standard_level`, `original_status`, and `redistribution` in separate columns.

## Register schema

| Column | Meaning |
|---|---|
| `id` | Stable project identifier |
| `name` | Full document name |
| `standard_no` | Standard number or document number; blank if none |
| `edition` | Edition, year, or draft label |
| `published_date` | Publication date where verified; blank otherwise |
| `effective_date` | Effective date where verified; blank otherwise |
| `issuer` | Issuing body |
| `validity_status` | `current`, `draft`, `repealed`, `to_verify` |
| `standard_level` | `national`, `industry`, `beijing_local`, `other_local` |
| `jurisdiction` | Geographic or institutional scope |
| `planning_level` | Planning level or object |
| `official_url` | Official source, or a clearly identified public copy |
| `original_status` | `catalog_only`, `official_link_only`, `metadata_only_paid`, `secondary_preview`, `full_text_online_read`, `local_full_text_read`, `rules_extracted` |
| `redistribution` | `unknown`, `link_only`, `official_free_download_no_explicit_relicense`, `cleared` |
| `verified_date` | Date of the last metadata check |
| `supersedes` | Replacement relationship; blank if none verified |
| `expected_use` | Project use, not a claim of compliance |
| `local_index_id` | Local-only index key; blank for documents not held locally |

## Rules schema

Each rule file records:

- rule ID;
- standard ID;
- clause number and printed/PDF page where available;
- a short paraphrase, not a long quotation;
- parameter value and unit;
- conditions;
- normative nature: mandatory, recommended, or project design;
- proposed QGIS resource type;
- verification status.

If a value is not specified, write `not specified`. If a colour is sampled from a sample map, write `sample-map approximation` and record the method. Do not convert an approximation into a standard RGB value.

## Initial scope

1. National general planning-drawing standards.
2. Beijing territorial spatial zoning planning.
3. Beijing territorial spatial detailed planning.
4. Beijing township and village planning.
5. Historic cities, districts, villages, historic buildings, and heritage conservation.
6. Shared bases: land-use classification, symbols, annotation, sheet, and title block.

Beijing is the first adaptation region. Other provinces are not merged into a single "national" style.

## Redistribution caution

A government website that offers a free download does **not** automatically grant permission to redistribute the text under this project's licence. The Beijing planning authority's public notice states that its standards can be viewed and downloaded free of charge, but it does not grant a relicense. Such documents are recorded as `official_link_only` or `official_free_download_no_explicit_relicense`; their full texts stay local.

## Current extraction set

At this baseline, the project has full-text access to:

- CJJ/T 97-2003《城市规划制图标准》— HTML full text via a university official page.
- 山东省市县国土空间总体规划制图指南（征求意见稿）— PDF, local reading copy.

`GB/T 10609.1-2008` is recorded as a paid metadata-only standard. Its exact title-block dimensions are **not** extracted until a lawful copy is obtained.

## Adding a standard

1. Search the official publisher, ministry, provincial/municipal government, or standards portal.
2. Record the identity, edition, issuer, dates, validity, and jurisdiction.
3. Record whether the original was obtained and where it is held locally.
4. Record redistribution status; if unknown, keep the text local and link to the source.
5. Extract only from text actually read; mark every unverified field.
6. Add rules and mappings; do not create QGIS resources yet unless the rule is verified.
7. Update `register.csv` and the local index together.
