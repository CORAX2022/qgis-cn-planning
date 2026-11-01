# Project scope

## Problem

Chinese planning teams routinely rebuild the same cartographic resources: land-use colours, zoning symbols, road hierarchies, facility markers, title blocks, north arrows, scale bars, and legend structures. The knowledge is often embedded in institute CAD templates, ArcGIS projects, or individual QGIS profiles and is difficult to inspect, compare, or reuse.

The result is duplicated work, inconsistent drawings, and a steep entry barrier for small teams and independent practitioners who use QGIS.

## Goal

Create a public, reusable **standards register and QGIS resource library** for Chinese planning practice that is:

- **Inspectable** — text-based sources wherever practical.
- **Traceable** — each resource points to a registered standard, a local profile, or a recorded design decision.
- **Evidence-first** — standards metadata, source status, and rules are recorded before implementation.
- **Installable** — a documented path into a QGIS profile.
- **Composable** — styles, symbols, layouts, and validation examples can be used separately.
- **Licence-clear** — code, content, data, and third-party assets are distinguished.

## Audiences

- Planning practitioners producing statutory and non-statutory drawings.
- Researchers comparing plans and producing publication graphics.
- Learners who need documented, inspectable conventions, not a simplified teaching-only version.
- QGIS users who need Chinese planning resources without a proprietary stack.

## Domains in scope

### Village and town planning

Village classification, settlement systems, land layout, public facilities, road networks, industry, municipal infrastructure, and village construction boundaries.

### Territorial spatial planning

Three zones and three lines, planning zones, land-use and sea-use classification, transport, ecological protection and restoration, and major facility layout.

### Historical and cultural heritage conservation

Historic towns and villages, traditional villages, protected areas and buffer zones, historic buildings, historic environment elements, character zones, and heritage routes.

### Cross-cutting resources

Standards metadata, clause-level rule extraction, layout templates, Chinese typography, legend construction, scale bars, north arrows, sheet numbering, validation tools, and documentation.

### Standards foundation

Before a style or template is implemented, the project records:

- the standard's identity, edition, issuer, validity, and jurisdiction;
- whether the original text has been obtained and read;
- whether the original may be redistributed;
- the clause-level rule, parameter, unit, and condition;
- whether the rule is mandatory, recommended, or a project design decision.

The public register does not contain local machine paths or restricted files. A separate local index, excluded from version control, records source locations and checksums for local reading.

## Out of scope for v0.1.0

- A full QGIS plugin with a graphical interface.
- Nationwide coverage of every provincial standard.
- A database schema or statutory data model.
- Reproduction of proprietary institute templates or standard full texts.
- Large real-world datasets.
- Automated planning analysis or decision support.
- Any claim of official certification or institute endorsement.

## Profiles

The library separates a **national baseline** from **local profiles**.

- The national baseline captures conventions shared across Chinese planning practice and public national/industry standards.
- A local profile records provincial or municipal adaptations, such as Beijing DB11/T series, Shanghai detailed-planning deliverables, or Shandong mapping guidance.
- A profile must state its source, edition, and scope. It must not be presented as a national standard.

The v0.1.0 baseline includes a Beijing adaptation profile. Additional profiles are added only when a contributor can provide the source and licence status.

## Public and private boundary

The Git repository is the public source of truth for:

- Resource source files.
- Documentation.
- Issue and review records.
- Release metadata.

The repository does not contain:

- Personal or student records.
- Unpublished client data.
- Restricted spatial data.
- Proprietary institute templates.
- Local machine paths, credentials, caches, or QGIS profiles.

Local execution notes may exist outside version control. They are not part of the public project record.

## Success criteria for v0.1.0

A new user can:

1. Clone the repository.
2. Read a quick-start guide and install the resources into a QGIS profile.
3. Open the first layout template selected through a依据卡 and confirm that its drawing type, paper size, orientation, title block, and information layout match the recorded decision.
4. Apply at least one land-use style and one planning-zone style whose fields and values are traceable to the register.
5. Open a small validation project and reproduce a sheet.
6. Run a validation script that reports missing fonts, SVG paths, page sizes, and XML errors.
7. Understand the licence status of code, content, data, and third-party assets.

The release also needs a manifest, checksums, tested QGIS versions, and a changelog.

## Open decisions

- Final licence model.
- Whether v0.1.0 ships a plugin or a resource installer only.
- Which Beijing profile elements are mandatory versus illustrative.
- Whether sample data can be public or must be synthetic.
- How to handle QGIS 3.40 LTR and 4.x format differences.
- **First template:** drawing type, paper size, orientation, and information layout are deliberately undecided until the standards evidence and user choice are recorded.
- **Title block:** the exact dimensions depend on a title-block standard that has not yet been obtained in full; do not invent dimensions.
