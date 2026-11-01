# Beijing plan samples — layout evidence

This note records what the project learned from publicly downloadable Beijing planning drawings. It is **not** a standard, not a compliance claim, and not a template specification.

Local PDFs and preview images are kept under `standards/_local/beijing-plans/` and are ignored by Git. Only the official links and observations are public.

## Samples

| ID | Sample | Official page | Format | What it is |
|---|---|---|---|---|
| P-001 | 北京城市副中心 07 组团 FZX-0703-6005 等地块规划综合实施方案（规划图则） | [official page](https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/ghcg/csfzxgh/202412/t20241205_3957247.html) | A3 landscape, 1 page | Project-level planning implementation plan sheet |
| P-002 | 怀柔新城 HR00-0101～0103 街区（老城区单元）控制性详细规划（街区层面） | [official page](https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/ghcg/xxgh/hr/202505/t20250514_4088664.html) | A3 landscape, 39 pages | Control detailed plan book; drawings from p.24, 图则 from p.36 |
| P-003 | 通州区宋庄镇 TZ03-0403-6008 等地块规划综合实施方案（规划图则） | [official page](https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/ghcg/csfzxgh/202309/t20230901_3241073.html) | A2 landscape, 1 page | Project-level planning implementation plan sheet |
| P-004 | 北京市顺义区牛栏山镇安乐村村庄规划（2019—2035） | [official page](https://www.bjshy.gov.cn/web/zwgk/zfxxgk2/qqd/zhjd/nlsz16/ghjsyhjbh22/667261/index.html) | A3 landscape, 26 pages | Village planning presentation/atlas, not a statutory 图则 |

## Common layout pattern

The three 图则 (P-001, P-002 p.37, P-003) share a layout family:

1. **Landscape sheet**, A3 for the smaller project-level sheets, A2 for the larger site.
2. **Outer border** with a narrow margin; no bottom engineering title block.
3. **Top title bar** across the sheet:
   - project/plan name on the left;
   - “规划图则” or the control-unit name on the right;
   - sheet number (for example `01`) at the far right of the control-plan sheet.
4. **Main map field** occupying roughly two-thirds of the sheet.
5. **Right-hand information column**:
   - project/location locator inset;
   - north arrow and scale;
   - legend;
   - plot control indicator table;
   - notes;
   - issuing authority / QR / electronic-review mark on the issued version.
6. **Scale** may be placed at the lower right of the map or in the right column; the samples are not consistent.
7. **Official issue marks** (watermark, QR code, electronic seal) are part of the issued drawing, not design elements to copy.

P-002 p.37 is the clearest control-plan 图则: top title bar across the full width, main map on the left, legend column in the middle, and three small inset maps (dominant function, base intensity, base height) on the right.

P-004 is a **village planning presentation**, not a statutory 图则: project header at the upper right, paired “before/after” maps, legends and north arrows inside each map, no formal title block. It is useful for village content and colour conventions, not for a statutory sheet frame.

## Standards references visible in the samples

- **P-001**: the notes visible on the sheet refer to 《北京市城乡规划用地分类标准》（DB11/996-2013）and 《北京市城乡规划计算机辅助制图标准》（DB11/T 997-2013）. These are the 2013 editions; their current status must be checked before reuse.
- **P-002**: the plan book does not visibly cite a drawing standard in the extracted text. Do not infer one.
- **P-003**: the PDF is a raster scan without a text layer; no standard reference can be reliably extracted without OCR and verification.
- **P-004**: the presentation cites 《北京市村庄规划导则》. It does not provide a statutory title block.

## What this means for the first template

The actual Beijing 图则 are **not** A1 engineering sheets with a bottom title block. They are A3/A2 landscape sheets with a **top title bar + right information column**.

Therefore:

- Do not start from the earlier A1 Layout Hub frame and call it a Beijing 图则.
- Do not assume A1; A3 and A2 are the observed formats in these samples.
- Do not copy the official watermark, QR code, or issuing-authority mark into a generic template.
- The title bar is a **图则 header**, not the GB/T 10609.1 title block. A title-block standard may still be needed for a different sheet type, but it should not be forced onto this 图则 family.
- The samples are raster scans; exact colours, line widths, and font sizes cannot be measured from the PDF text layer. Any pixel-sampled value must be marked `sample-image approximation`.

## Next decision

The first template should be chosen from a **图则 family**, not from an A1 engineering frame:

1. Project-level 规划综合实施方案 图则 (A3/A2, top title bar + right column).
2. Control-plan 图则 (A3, top title bar + legend + inset maps).
3. Village plan sheet (A3, project header, paired maps; not a statutory 图则).

Paper size, orientation, and information layout still require the project owner's decision.
