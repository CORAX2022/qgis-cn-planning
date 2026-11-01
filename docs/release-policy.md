# Release policy

## Versioning

The project uses semantic versioning: `MAJOR.MINOR.PATCH`.

- **MAJOR** — incompatible changes to resource semantics, field names, template structure, or installation layout.
- **MINOR** — new styles, templates, profiles, tools, or documentation that remain backward compatible.
- **PATCH** — corrections that do not change resource semantics.

Pre-release versions use a suffix such as `v0.1.0-rc.1`.

## Tags and releases

- Formal versions are tagged `vX.Y.Z`.
- A GitHub Release is created only after the release checklist passes.
- Release assets include a source archive, a resource bundle, a manifest, and checksums.
- The release notes state the tested QGIS versions and any known limitations.
- A tag is not a release until the assets and notes are published.

## Release gates

A release requires:

1. **Scope** — the milestone issues are closed or explicitly deferred.
2. **Standards** — every resource has a recorded source, clause/page where applicable, and profile.
3. **Licence** — the licence decision is recorded; third-party notices are complete; no unresolved asset is bundled.
4. **Validation** — XML, page size, fonts, SVG paths, absolute paths, and missing resources pass the validator.
5. **Visual check** — at least one complete sheet per domain pack has been rendered and reviewed.
6. **Compatibility** — tested on the declared QGIS versions; differences are documented.
7. **Documentation** — quick start, field mapping, standards mapping, changelog, and known issues are current.
8. **Reproducibility** — a clean checkout can reproduce the sample outputs with documented commands.
9. **Public-content check** — no credentials, personal data, restricted data, proprietary templates, or standard full texts.
10. **Manifest** — file list, sizes, checksums, and licence status are published.

## Compatibility

- Target QGIS 3.40 LTR and QGIS 4.x unless a release states otherwise.
- QPT and QML serialisation can differ between versions. If a single file cannot serve both, provide separate files or a documented conversion step.
- Record the exact QGIS version used for validation.
- Do not claim compatibility that has not been tested.

## Source formats

Prefer reviewable text formats:

- `.qml` — layer styles
- `.qpt` — layout templates
- `.svg` — symbols
- `.xml` — style-library exports
- `.csv` — attribute tables and mappings
- `.md` — documentation
- uncompressed `.qgs` where a project file needs review

Compressed `.qgz` may be used for user-facing samples, but the source of truth should remain reviewable.

## Data and large files

- Do not use Git LFS by default.
- Evaluate data size, change frequency, and download convenience before proposing LFS.
- Large real-world datasets do not belong in the repository.
- Sample data must be small, synthetic or public-domain, and licence-clear.
- Release bundles may include larger examples as Release assets with checksums.

## Migration and deprecation

- A change to field names, style identifiers, or template semantics requires a migration note.
- Deprecated resources remain available for at least one minor release unless a security or licensing issue requires removal.
- Release notes identify removed or renamed resources and the replacement path.

## Release checklist

- [ ] Milestone complete or deferred items recorded
- [ ] Standards mapping updated
- [ ] Licence decision recorded
- [ ] Third-party notices updated
- [ ] Validation passed
- [ ] Visual review completed
- [ ] QGIS compatibility tested
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Manifest and checksums generated
- [ ] Release notes written
- [ ] Tag created
- [ ] Release published

## Relationship to standards versions

The project version and the standards versions are separate. A release records:

- the project version,
- the standards and editions it was built against,
- the local profiles it includes,
- any known deviations.

Updating a standard does not automatically require a major project release, but it may require a minor release and a new mapping note.
