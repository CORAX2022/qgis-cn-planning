# Standards baseline

This document records the standards and guidance the project tracks. It does not reproduce them. Citations are for traceability; users must obtain the official texts.

## Status vocabulary

- **Current** — published and in force at the time of writing.
- **Draft** — published for comment; not a basis for a compliance claim.
- **Local profile** — provincial or municipal adaptation; valid only within its jurisdiction.
- **Reference** — informative guidance, not a mandatory standard.

## Baseline table

| Document | Status | Intended use | Notes |
|---|---|---|---|
| 《国土空间规划制图规范》（2025 征求意见稿） | Draft | National baseline for map elements, colours, patterns, line types, annotation, sheet composition | Label outputs as "aligned with the draft", not "compliant with the national standard" |
| CJJ/T 97-2003《城市规划制图标准》 | Current industry standard | Figure title, figure number, map boundary, north arrow, scale, legend, signature, sheet size, sheet order | Older but still widely referenced; check whether a newer national standard applies |
| GB/T 10609.1《技术制图 标题栏》 | Current national standard | Title-block data fields and layout | Use for field structure, not as a planning-specific standard |
| 北京市 DB11/T 1947-2021《国土空间分区规划计算机辅助制图标准》 | Local profile | Beijing zoning-plan layers, symbols, colours, and drawing rules | Beijing profile only |
| 北京市 DB11/T 1948-2021《国土空间详细规划计算机辅助制图标准》 | Local profile | Beijing detailed-planning drawing rules | Beijing profile only |
| 北京市 DB11/T 1949-2021《乡镇国土空间规划计算机辅助制图标准》 | Local profile | Beijing township planning drawing rules | Closest to village/town work |
| 山东省市县国土空间总体规划制图指南 | Provincial reference | Detailed rules for figure name, map border, locator, north arrow/wind rose, scale, legend, signature, date, sheet layout | Use as a worked example of provincial guidance; not a national standard |
| 《国土空间调查、规划、用途管制用地用海分类指南》 | Current national guidance | Land-use and sea-use classification | Use the current edition; record the edition in style metadata |

## Rules

1. **Never claim compliance without a clause-level mapping.** A style or template may be "aligned with" a document, but compliance requires a recorded clause, page, and verification result.
2. **Separate draft from current.** Draft standards are labelled in the README, documentation, and release notes.
3. **Separate national from local.** A Beijing or Shandong profile is not a national baseline.
4. **Record editions.** Standards are revised; styles and templates must state the edition they were built against.
5. **Do not copy full texts.** Summarise the requirement, cite the source, and link to the official publisher where possible.
6. **Do not infer colour values.** If a standard does not publish RGB/CMYK values, record the source of the values (official annex, sampled colour chart, or a documented approximation).
7. **Check licence before importing.** A public standard may be free to read but not free to redistribute.

## Known gaps

- Exact title-block dimensions for a national planning sheet are not fully specified in the public documents reviewed; the project needs a documented, profile-specific decision.
- Colour values for some land-use classes are published as charts rather than machine-readable tables; the extraction method must be recorded.
- Chinese font availability differs across operating systems; the project needs a font fallback policy.
- QGIS 3.40 LTR and 4.x differ in layout serialisation and some symbol APIs; compatibility must be tested rather than assumed.
- Provincial profiles may conflict; the project will not merge them into a single "national" style.

## Citation format for resources

When a style or template is added, include metadata in the accompanying documentation:

```text
Standard: <title>
Edition/date: <edition>
Clause/page: <clause or page>
Profile: <national | Beijing | other>
Implementation: <QGIS style/template path>
Verification: <how it was checked>
Licence of source: <status>
```

## Sources consulted at baseline

- 《国土空间规划制图规范》（2025 征求意见稿）— public consultation page.
- CJJ/T 97-2003 — standard record.
- GB/T 10609.1 — standard record.
- Beijing DB11/T 1947-2021, DB11/T 1948-2021, DB11/T 1949-2021 — standard records.
- 山东省市县国土空间总体规划制图指南 — public provincial compilation.
- 《国土空间调查、规划、用途管制用地用海分类指南》 — public national guidance.

Links are recorded in the project issue for standards tracking rather than duplicated here, to avoid stale URLs.
