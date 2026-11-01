# First-template candidates

No template is selected in this round. These are candidates for a later依据卡 and user decision. Paper size, orientation, and information layout are deliberately not fixed.

## Candidate 1 — Beijing village planning sheet

- **Purpose:** A village plan sheet for Beijing, for example the village-area existing-condition map, village-area land-use plan, or village-area spatial control zoning map.
- **Basis completeness:** Strongest of the three.
  - `BJ-VILLAGE-GUIDE-2019` is obtained and read; it lists the required labels, the required drawing set, content requirements, layer prefixes, and representative RGB values.
  - CJJ/T 97-2003 supplies general drawing rules and sheet-size/text-height values.
  - SD-MAP-2019 supplies additional layout logic, but it is a draft and not Beijing.
- **Known requirements:** project name, drawing name, north arrow, scale, legend, drawing date, planning/design unit, drafter, reviewer, approver; three required village maps; layer prefixes; representative land-use and five-line colours.
- **Still to decide:** which of the three required village maps is first; sheet size; orientation; single-sheet vs multi-sheet; title-block field layout; information zones; map scale; legend position; whether to use the 2019 RGB values or wait for a current edition.
- **Why consider it first:** it has the most complete obtained evidence and is directly within the village planning domain. It should not be treated as current until the 2019 guide's revision status and its references to DB11/996-2013 and DB11/T 997-2013 are checked.

## Candidate 2 — Beijing township territorial spatial master plan sheet

- **Purpose:** A township-level territorial spatial plan sheet for Beijing.
- **Basis completeness:** Partial.
  - `BJ-DB11-1949-2021` is registered but the text is not yet obtained or read.
  - CJJ/T 97-2003 supplies general drawing rules.
  - SD-MAP-2019 supplies a worked provincial layout logic, but it is a draft and not Beijing.
- **Known requirements:** figure title, map boundary, north arrow/wind rose, scale, legend, signature, date, sheet ordering, text-height ranges, paper-family values from CJJ.
- **Still to decide:** sheet size, orientation, single-sheet vs multi-sheet set, title-block field layout, information zones, map scale, legend position, and whether the first sheet is a status map or a planning-structure map.
- **Why consider it:** it is the core Beijing township product, but the Beijing township standard is not yet read; the village guide is not a substitute.

## Candidate 3 — historic building / historic district conservation sheet

- **Purpose:** A heritage conservation sheet for a historic district, historic building group, or traditional village.
- **Basis completeness:** Weakest of the three.
  - The Beijing historic-city regulation is a legal/terminology source, not a drawing standard.
  - `BJ-HIST-BUILDING-2024` is obtained and read at a high level; it lists the contents of a historic-building protection atlas, but not a complete drawing layout.
  - `GB/T 50357-2018` is registered but not read.
  - Protection boundaries, buffer zones, and building categories need separate legal and technical sources.
- **Known requirements:** general drawing elements from CJJ; historic-building atlas contents from the 2024 work rules.
- **Still to decide:** protection-object type, legal boundary source, classification of buildings, sheet size, orientation, title-block layout, and whether the sheet is an inventory, a protection framework, or a design guidance sheet.
- **Why consider it:** heritage is an explicit project domain, but the evidence base is not ready for a first template.

## Recommended sequence

1. Check whether `BJ-VILLAGE-GUIDE-2019` has a current revision and whether DB11/996-2013 and DB11/T 997-2013 are still current.
2. If the village guide is current enough, prepare a依据卡 for Candidate 1 and select one of its three required maps.
3. Keep Candidate 2 as the next Beijing profile after `BJ-DB11-1949-2021` is obtained and read.
4. Do not start Candidate 3 until the heritage conservation standard and the legal boundary source are obtained.

This is a sequencing recommendation, not a template decision. The first template's paper size and drawing type still require the project owner's choice.

## 依据卡 template

```text
Drawing type:
Region and profile:
Planning level and object:
Standards and editions:
Rules with parameters:
Rules not specified by the standard:
Information layout:
Paper size and orientation:
Scale and extent:
Title-block fields:
Legend and symbol requirements:
Known conflicts:
User decisions needed:
Review status:
```
