# Rule-to-resource mappings

This directory links extracted rules to future QGIS resources and records template candidates. A mapping is a design intention, not a claim that the resource exists or complies.

## Mapping table

| Rule ID | Future QGIS resource | Status | Blocking evidence |
|---|---|---|---|
| R-CJJ-001, R-CJJ-002 | Layout title text and typography | planned | Title-block dimensions not yet obtained |
| R-CJJ-003 | Map frame and extent rule | planned | None for the rule; template extent depends on the selected drawing type |
| R-CJJ-004, R-SD-004 | North arrow / wind rose item | planned | Need to choose a symbol source and placement per template |
| R-CJJ-005, R-SD-005 | Scale text and scale bar | planned | Need a selected template and page size |
| R-CJJ-006 | Planning-period field | planned | None |
| R-CJJ-007, R-SD-006 | Legend frame and ordering | planned | Need a rule for legend order per map type |
| R-CJJ-008, R-CJJ-009, R-SD-007 | Signature/date fields | planned | Title-block field layout unresolved |
| R-CJJ-011, R-CJJ-012, R-SD-009 | Typography scale and font policy | planned | Need font availability test |
| R-CJJ-013 | Page-size and margin presets | planned | First template's paper size not decided |
| R-SD-002 | Map border and grid | planned | Draft/provincial rule; compare with Beijing standard |
| R-SD-008, R-SD-013 | Paper-size decision record | planned | User decision needed |
| R-SD-011 | Layer-order preset | planned | Need the selected map type |
| R-SD-012 | Project CRS and metadata | planned | None for the rule; data CRS must be checked per project |
| R-CJJ-017, R-SD-014 | Land-use colour and legend | planned | Current classification and colour basis not yet extracted |
| R-BJV-002 | Village drawing title block fields | planned | Field list known; title-block dimensions still missing |
| R-BJV-003–R-BJV-006 | Village drawing set and layer checklist | planned | Which of the three required maps is first is undecided |
| R-BJV-007 | Village layer-prefix preset | planned | References DB11/996-2013 and DB11/T 997-2013; current status to verify |
| R-BJV-008, R-BJV-009 | Village land-use and five-line colour palettes | planned | 2019 RGB values are legacy until current editions confirm them |

## Template candidates

See [`template-candidates.md`](template-candidates.md). No candidate has been selected.

## Mapping rule

Each implementation must be traceable to:

- a rule ID;
- a standard ID and edition;
- a profile (national or local);
- a QGIS resource path;
- a verification record.

If a visual adjustment is not supported by a rule, it is recorded as **project design**, not as a standard requirement.
