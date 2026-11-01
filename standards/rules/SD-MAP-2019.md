# 山东省市县国土空间总体规划制图指南（征求意见稿）— extracted rules

- Standard ID: `SD-MAP-2019`
- Edition: 2019-10 征求意见稿
- Issuer: 山东省自然资源厅
- Source read: PDF compilation hosted at `http://www.jsghy.com/uploadfiles/file/202004/15.pdf`; the mapping guide begins at printed p.223 / PDF p.227.
- Local copy: `L-001` (PDF; see local index, not in Git)
- Extraction date: 2026-11-01
- Status: **draft / other-local reference**, not a Beijing standard and not a current national standard.

## Rules

Page references use `printed p. / PDF p.` where both are visible.

| Rule ID | Clause | Location | Short paraphrase | Parameter / value | Unit | Condition | Nature | Proposed QGIS resource | Verification |
|---|---|---|---|---|---|---|---|---|---|
| R-SD-001 | 4.3.1 | printed p.231 / PDF p.235 | Figure name contains the plan name and theme name; Chinese in Song, numbers in Times New Roman; theme type size should be equal to or larger than the plan name; place outside the map border at the top. | Chinese: 宋体; numbers: Times New Roman; theme size ≥ plan name | — | Territorial master plan drawings | recommended / mandatory mix | Layout title typography | read |
| R-SD-002 | 4.3.2 | printed p.231–232 / PDF p.235–236 | Map border has an outer thick solid line and an inner thin solid line; a grid may be placed between them; label longitude/latitude at the four inner corners. | Grid interval: 10 km (1:100,000 city), 5 km (1:50,000 county) | km | Master plan drawings | mandatory for the guide's formal sheets | Map frame and grid | read |
| R-SD-003 | 4.3.3 | printed p.231 / PDF p.235 | A small-scale locator map shows the area within its parent region, usually at the upper left or upper right inside the sheet. | Position: upper left/right | — | Master plan drawings | recommended | Locator inset | read |
| R-SD-004 | 4.3.4 | printed p.231 / PDF p.235 | North arrow or wind rose at upper left/right; use a 16- or 8-direction wind rose where wind data exist, otherwise a north arrow. | 16 or 8 directions | — | Master plan drawings | mandatory/recommended | North arrow / wind rose | read |
| R-SD-005 | 4.3.5 | printed p.232 / PDF p.236 | Scale outside the map border at the bottom; wall maps use numeric or numeric + linear scale; linear scale total length about 10 cm, head 2 cm. | Total 10 cm; head 2 cm | cm | Wall maps | recommended | Layout scale bar | read |
| R-SD-006 | 4.3.6 | printed p.232 / PDF p.236 | Legend inside the map frame at lower left or lower right; composed of line/area/symbol graphics plus text. | Position: lower left/right | — | All formal sheets | mandatory | Legend frame | read |
| R-SD-007 | 4.3.7 | printed p.232 / PDF p.236 | Show the formal names of the plan-preparation unit and drawing unit, plus the plan completion date; place preparation unit/date at lower left outside the border and drawing unit at lower right outside the border. | Position: lower left/right outside border | — | All formal sheets | mandatory | Signature/date fields | read |
| R-SD-008 | 4.5 | printed p.232–233 / PDF p.236–237 | Paper size is selected from the mapping area and must express the content completely; formal drawings should not exceed two A0 sheets in area; printing paper 125 g/m²; A0 roll width 0.914 m; 8-colour printing. | Max two A0 sheets; 125 g/m²; 0.914 m roll | — | Formal printed sheets | recommended | Page-size decision record | read |
| R-SD-009 | 4.2.2 | printed p.230 / PDF p.234 | Use no more than four Chinese font families in one file; prefer Song; Western text Times New Roman or Arial Black, preferably Times New Roman. | Max 4 Chinese font families | — | Annotation | recommended | Font policy | read |
| R-SD-010 | 4.2.3–4.2.5 | printed p.230–231 / PDF p.234–235 | Text orientation is normally upright with the top toward the north border; arrangements may be horizontal, vertical, stepped, or curved; spacing is close, normal, or isolated. | Close 0–0.5 mm; normal 1.0–3.0 mm; isolated 1–5× character size | mm | Annotation | mandatory/recommended | Label placement rules | read |
| R-SD-011 | 5.4 | printed p.233 / PDF p.237 | Layer order for the land-use status map, from top to bottom: annotation, administrative boundary, other base geographic elements, land-use status. | Top→bottom: annotation > boundary > base > land use | — | Land-use status map | recommended | Layer order preset | read |
| R-SD-012 | 3.1 | printed p.227 / PDF p.231 | Use CGCS2000; vertical datum 1985 National Height Datum; Gauss-Krüger projection; 3-degree zones; 6-degree zones allowed below 1:100,000. | CGCS2000; 1985 datum; 3°/6° zones | — | Formal drawings | mandatory | Project CRS / metadata | read |
| R-SD-013 | 3.2 | printed p.227 / PDF p.231 | Scale selection: city territory generally 1:100,000; county territory generally 1:50,000; central urban area 1:10,000–1:25,000 (1:50,000 if large); wall maps no more than two A0 sheets. | 1:100k; 1:50k; 1:10k–1:25k | — | Master plan drawings | recommended | Scale decision record | read |
| R-SD-014 | 3.4.1 | printed p.228 / PDF p.232 | Use warm colours mainly for construction land and cool colours mainly for agriculture, nature conservation, and marine use. | Warm/cool semantic grouping | — | Land-use/zoning maps | recommended | Colour-ramp policy | read |

## Gaps and cautions

- **Title-block dimensions are not specified in this guide.** It lists title-block elements but does not give a full field table or dimensions. Do not infer them from the sample figures.
- **Exact RGB/CMYK values are not extracted.** The appendices contain colour/pattern figures; this extraction did not sample them.
- **Line widths, point-symbol sizes, and legend order are not fully extracted.** They require the appendix figures and tables.
- **The guide is a draft and is specific to Shandong.** It can inform general layout logic, but it is not a Beijing profile and not a national standard.
- **The public URL is a mirror**, not the Shandong Natural Resources Department's own download page. The local copy is for reading; do not redistribute it from this repository.
- The guide states that the map title should be outside the border; this differs from some local practices. Keep it as a documented rule, not a universal requirement.

## Follow-up

- Obtain the official Shandong source page and record its checksum if the mirror is replaced.
- Extract appendix B/N colours and symbol sizes only for a selected template.
- Compare with Beijing DB11/T 1949 before using any layout rule in a Beijing template.
