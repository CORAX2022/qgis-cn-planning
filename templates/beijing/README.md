# Beijing control-plan 图则 templates

Two QGIS layout shells for the first template family:

- `A3_beijing_control_tuze.qpt`
- `A2_beijing_control_tuze.qpt`

They are **layout shells**, not finished statutory drawings. They contain no project data, no map layers, and no official seal or QR mark.

## Evidence and decision

Selected by the project owner on 2026-11-01:

- First template family: **Beijing control-plan 图则**.
- Sizes: **A3 and A2, both landscape**.
- Layout reference: P-002 怀柔新城 HR00-0101～0103 街区控规 p.37 (A3), with P-001 副中心 07 组团图则 and P-003 宋庄镇图则 as the same layout family.

Observed sample layout:

- A3/A2 landscape, double outer border.
- Top title bar across the sheet: project/plan name left; 控制图则 and sheet number right.
- Main map on the left.
- Right information column: locator, scale/north, legend, three inset frames, and (A2 only) an indicator-table placeholder.
- No bottom engineering title block; no drafter/reviewer/approver fields in the observed 图则.
- Official issue watermarks/QR codes are not reproduced.

## What is in the templates

| Item | A3 | A2 |
|---|---|---|
| Page | 420 × 297 mm | 594 × 420 mm |
| Title bar | Full width | Full width |
| Main map frame | 250 × 256 mm | 356 × 366 mm |
| Locator | 148 × 46 mm | 210 × 60 mm |
| Scale/north | Explicit placeholder | Explicit placeholder |
| Legend | 10 placeholder classes | 10 placeholder classes |
| Inset frames | 3 | 3 |
| Indicator table | — | Static placeholder |
| Footer | 编制单位/日期/依据/图号 | 编制单位/日期/依据/图号 |

## How to use

1. Open QGIS **Layout Manager → New from Template** and choose the desired `.qpt`.
2. Replace the main map, locator, and three inset map frames with project layers/extents.
3. Replace the placeholder legend classes with the project legend.
4. Replace the static indicator-table placeholder; it is deliberately not linked to data.
5. Fill the title-bar, footer, scale, and sheet number.
6. Keep the double border and top-bar geometry unless the依据卡 records a deviation.

## Standards status

- **CJJ/T 97-2003** supplies general drawing rules and sheet/text-height values.
- **DB11/T 1948-2021** is the relevant Beijing detailed-planning computer-aided mapping standard, but its full text has **not** been obtained or read. These templates do **not** claim compliance with it.
- P-001 visibly cites **DB11/996-2013** and **DB11/T 997-2013**; these are recorded as `to_verify` in the register. Do not treat their 2013 values as current without checking.
- **GB/T 10609.1-2008** is not obtained; the top title bar is not a GB/T 10609.1 title block.
- The exact millimetre positions are a **project design** inferred from raster samples, not a standard dimension.

## Known limitations

- Map frames are empty; no layers or extents are supplied.
- The legend is a placeholder, not auto-generated from layers.
- The A2 indicator table is static and uses `—`; replace it with real data.
- The north arrow and scale bar are explicit placeholders; the QGIS linked scale bar can replace them after map layers are added.
- Fonts use `Microsoft YaHei`. If unavailable, install an equivalent CJK sans font and adjust the `QFont` in the build script.
- The official PDF samples are raster; exact colours, line widths, and font sizes are not measured.

## Rebuild

```powershell
# Use the python-qgis.bat shipped with your QGIS installation.
& 'python-qgis.bat' 'src\build_beijing_control_tuze.py'
```

Preview PDFs are written to `templates/beijing/previews/` and are excluded from Git by `*.pdf`. The PNG previews are committed for review.
