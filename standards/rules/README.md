# Rule extraction index

Each file records rules extracted from a text that was actually obtained and read. A rule is not a template and does not authorise a QGIS implementation by itself.

| Rule file | Standard ID | Edition | Evidence | Extracted |
|---|---|---|---|---|
| `CJJ-T-97-2003.md` | `CN-CJJ-97-2003` | CJJ/T 97-2003 | Full HTML text, university official page | General drawing, title, boundary, north arrow, scale, legend, signature, text, sheet sizes, ordering |
| `SD-MAP-2019.md` | `SD-MAP-2019` | 2019-10 draft | Full PDF, local reading copy | Figure name, border, locator, north arrow, scale bar, legend, signature, paper, fonts, layer order, CRS, scale selection |

## Rules not yet extracted

- `CN-GBT-10609.1-2008` — title-block dimensions; metadata only, paid standard not obtained.
- `BJ-DB11-1947-2021` — Beijing zoning plan; official link only, text not read.
- `BJ-DB11-1948-2021` — Beijing detailed plan; catalogue only.
- `BJ-DB11-1949-2021` — Beijing township plan; catalogue only.
- `CN-HERITAGE-REG-2021` — heritage law; official link only; legal terminology, not a drawing standard.
- `CN-HERITAGE-STD-2018` — heritage conservation planning standard; catalogue only.
- `CN-LANDUSE-2023` — classification guide; official link only; code list not yet imported.
- `CN-MAP-DRAFT-2025` — national draft; secondary preview only; do not treat as current.
- `CN-MASTER-MAP-2021` — catalogue only.
- Topographic map standards — catalogue only.

## Quality rules

- Do not extract from a secondary summary when the standard text is available.
- Do not fill an unspecified dimension or colour with a visual guess.
- Mark sampled colours as `sample-map approximation` and record the sample source and method.
- Keep separate: classification basis, colour basis, line/symbol basis, layout basis.
- When two standards conflict, record both and state their object and jurisdiction; do not average them.
