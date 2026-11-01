# qgis-cn-planning

Open, reusable QGIS styles and layout templates for Chinese planning practice.

**Status: pre-alpha / project baseline. No public release yet.**

## Why this project

Chinese planning drawings are rich in locally specific conventions: land-use colours, zoning symbols, title blocks, figure numbering, north arrows, scale bars, legend order, and sheet composition. Much of this knowledge is locked inside individual institutes, CAD templates, or proprietary ArcGIS projects.

This project is a clean-room effort to turn public standards and common practice into reusable QGIS resources that can be installed, inspected, modified, and redistributed under clear licences.

## Scope

The library covers three initial domains:

- **Village and town planning** — village classification, settlement systems, land layout, public facilities, roads, industry, municipal infrastructure.
- **Territorial spatial planning** — three zones and three lines, planning zones, land-use classification, transport, ecological protection and restoration.
- **Historical and cultural heritage conservation** — historic towns and villages, traditional villages, protected areas and buffer zones, historic buildings, historic environment, heritage routes.

The v0.1.0 baseline also includes a **Beijing local adaptation profile** and a national baseline. Additional provincial profiles are planned.

## Who this is for

- Planning practitioners who need a reproducible QGIS starting point.
- Teachers and students who need documented, inspectable cartographic conventions.
- Researchers who need consistent symbols and layouts for comparative work.
- QGIS users who want Chinese planning styles without rebuilding them from scratch.

## What this repository will contain

```text
docs/                 Project scope, standards, curriculum coverage, release policy
styles/               QGIS layer styles (.qml) and style-library exports
symbols/              SVG markers and fill symbols
templates/            QGIS print layouts (.qpt) for A0–A3 sheets
examples/             Small, licence-clear reference projects
tools/                Install, validate and export scripts
tests/                Validation and regression checks
.github/              Issue and pull-request templates
```

The directories are created as work lands; this baseline branch contains documentation only.

## Design principles

1. **Standards first.** Every style or layout should point to a public standard, a local profile, or a documented design decision.
2. **Clean-room.** No proprietary institute drawings, CAD title blocks, ArcGIS projects, or standard full texts are copied into the repository.
3. **Text-first sources.** QML, QPT, SVG, XML, CSV, Markdown, and uncompressed QGS where practical.
4. **Reproducible.** A contributor should be able to re-render a sample from the repository and documented data.
5. **Explicit licences.** Code, cartographic resources, documentation, and data are licensed separately. Third-party assets keep their own notices.
6. **No false claims.** Draft standards are labelled as drafts. Local adaptations are labelled as profiles, not as national standards.

## Standards baseline

The project tracks, but does not reproduce, documents including:

- 《国土空间规划制图规范》（2025 征求意见稿）
- CJJ/T 97-2003《城市规划制图标准》
- GB/T 10609.1《技术制图 标题栏》
- 北京市 DB11/T 1947-2021、DB11/T 1948-2021、DB11/T 1949-2021
- 山东省市县国土空间总体规划制图指南

See [`docs/standards-baseline.md`](docs/standards-baseline.md) for status, scope, and citation rules.

## Curriculum coverage

The resource taxonomy is checked against Chinese urban and rural planning curricula at undergraduate and graduate levels. See [`docs/curriculum-coverage.md`](docs/curriculum-coverage.md) for the course-to-resource matrix and current gaps.

## Getting started

There is no installable release yet. The intended first-run path is:

1. Install QGIS 3.40 LTR or QGIS 4.x.
2. Run `tools/install.py` (planned) to copy styles and templates into the active QGIS profile.
3. Open a template from **Layout Manager** and a sample project from `examples/`.
4. Run `tools/validate.py` (planned) to check fonts, page sizes, SVG paths, and missing resources.

## Contributing

Contribution rules, branch naming, commit style, resource requirements, and review checks are in [`CONTRIBUTING.md`](CONTRIBUTING.md).

The short version: open an issue, work on a topic branch, include the standard/source and licence for every asset, run validation, and open a pull request.

## Versioning and releases

The project uses semantic versioning. Formal releases are tagged `vMAJOR.MINOR.PATCH` and published through GitHub Releases with a file manifest, checksums, and tested QGIS versions. See [`docs/release-policy.md`](docs/release-policy.md).

## Licence status

**No final licence has been selected for this repository.** No licence is granted for third-party assets. Candidate licences and the asset inventory are recorded in [`LICENSES/README.md`](LICENSES/README.md) and [`NOTICE.md`](NOTICE.md). Do not reuse content from this repository until the licence decision is recorded.

## Disclaimer

This is an independent community project. It is not endorsed by any planning institute, standards body, or software vendor. Users are responsible for checking the standards and statutory requirements that apply to their own projects.
