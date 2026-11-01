# 北京市村庄规划导则（试行）— extracted drawing rules

- Standard ID: `BJ-VILLAGE-GUIDE-2019`
- Edition: 2019 试行
- Issuer: 北京市规划和自然资源委员会
- Source read: official PDF, `https://www.beijing.gov.cn/zhengce/zhengcefagui/201905/W020190522422367083950.pdf`
- Local copy: `L-003` (52-page PDF; see local index, not in Git)
- Extraction date: 2026-11-01
- Status caution: the document is a 2019 trial and may have a later revision. Verify the current edition before using it as the basis for a new template.

## Rules

Page references use `printed p. / PDF p.` where both are visible.

| Rule ID | Clause / attachment | Location | Short paraphrase | Parameter / value | Unit | Condition | Nature | Proposed QGIS resource | Verification |
|---|---|---|---|---|---|---|---|---|---|
| R-BJV-001 | 2.4.2 | printed p.14 / PDF p.19 | A complete village plan includes text, description, drawings, and attachments; each part has paper and standard electronic files. | Four parts | — | Complete plan | mandatory | Deliverable checklist | read |
| R-BJV-002 | 附件 D | printed p.6 / PDF p.47 | Drawings must show project name, drawing name, north arrow, scale (selected to the administrative area), legend, drawing date, planning/design unit, drafter, reviewer, and approver. | Required label set | — | Village planning drawings | mandatory | Title block / layout fields | read |
| R-BJV-003 | 附件 D | printed p.6 / PDF p.47 | Required drawings: village-area existing-condition map, village-area land-use plan, village-area spatial control zoning map. Optional: landscape, character, heritage protection, disaster prevention, recent projects. | 3 required + optional set | — | Village plan | mandatory / optional | Sheet list | read |
| R-BJV-004 | 附件 D | printed p.6 / PDF p.47 | Existing-condition map shows administrative boundary, construction-land boundary, land-use classification, public facilities and infrastructure, main roads/rivers/corridors, and a land-balance table. | Content list | — | Existing-condition map | mandatory | Layer checklist | read |
| R-BJV-005 | 附件 D | printed p.6 / PDF p.47 | Land-use plan shows planned construction land, land-use classification, public facilities, infrastructure, roads/rivers/corridors, and a planned land-balance table. | Content list | — | Land-use plan | mandatory | Layer checklist | read |
| R-BJV-006 | 附件 D | printed p.6 / PDF p.47 | Spatial control zoning map delineates control lines for two lines/three zones, heritage protection, and related construction-control requirements. | Content list | — | Spatial control map | mandatory | Control-line layers | read |
| R-BJV-007 | 附件 E | printed p.7–11 / PDF p.48–52 | Electronic drawings follow DB11/996-2013 and DB11/T 997-2013; land-use layers use `B-`, `A-`, `HB-`, `HA-` prefixes and separate line/fill layers for existing and planned land. | Layer prefixes: `B-`, `A-`, `HB-`, `HA-` | — | Electronic drawings | mandatory at the time of the guide | Layer naming preset | read; **references older standards, verify current editions** |
| R-BJV-008 | 附件 E | printed p.7–11 / PDF p.48–52 | Representative land-use colours in the guide include village construction land `255,255,127`; public-service land `255,0,255`; education `0,204,204`; health `0,127,255`; social welfare `255,127,159`; industry `153,153,0`; infrastructure `191,0,255`. | RGB values as printed | RGB 0–255 | Village land-use fills | document-specified values | Fill colour palette | read; **legacy values, verify current standard** |
| R-BJV-009 | 附件 E / five-line table | printed p.11 / PDF p.52 | Village five-line colours: red line `255,0,0`; yellow line `255,191,0`; blue line `0,255,255`; green line `0,255,0`; purple/heritage protection `159,255,127`; heritage subcategories use the printed values. | RGB values as printed | RGB 0–255 | Village five-line drawing | document-specified values | Line style palette | read; **legacy values, verify current standard** |

## What is explicitly specified

- The required label set for village planning drawings (R-BJV-002).
- The required drawing set and minimum content (R-BJV-003 to R-BJV-006).
- The layer-prefix convention and separate existing/planned fill/line layers in the 2019 electronic-drawing annex (R-BJV-007).
- RGB values in the 2019 annex tables (R-BJV-008, R-BJV-009).

## What is not specified or not safe to reuse directly

- **Title-block dimensions are not specified.** The guide lists fields but not a complete title-block geometry.
- **Exact font family and size for the title block are not specified.** The general text hierarchy is not enough to fix typography.
- **The colour table is from a 2019 annex that cites DB11/996-2013 and DB11/T 997-2013.** These may be superseded or supplemented. Do not present the values as current Beijing standards without checking the current editions.
- **Line widths, symbol sizes, and legend order are not fully extracted.**
- The guide is a village planning guideline, not a township territorial spatial planning standard. Do not use it as a substitute for DB11/T 1949.

## Follow-up

- Verify whether a later revision of the Beijing village planning guide exists.
- Check the current status of DB11/996-2013 and DB11/T 997-2013.
- If a current edition confirms the colour values, promote them from `legacy document value` to `current profile value`.
- Obtain a title-block standard before fixing title-block dimensions.
