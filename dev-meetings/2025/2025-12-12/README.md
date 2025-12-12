# Gammapy Developer Meeting 
 * Friday, December 12, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

Attendees: Régis Terrier, Tomas Bylund, Kirsty Feijen, Claudio Galelli, Natthan PIGOUX, Katharina Egg, Fabio Acero, Atreyee Sinha,   Quentin Remy

# Agenda

## General information
- Bug fix is expected next week. Discussion monday at 10am. It will probably require a release candidate to make sure everything works.

## [Open issues](https://github.com/gammapy/gammapy/issues)

- [#6258](https://github.com/gammapy/gammapy/issues/6258) See discussion below on #6259.

## [Bugs](https://github.com/orgs/gammapy/projects/36)

- [#6254](https://github.com/gammapy/gammapy/pull/6254)  Discussion on the possible effect of stacking int on float. Q.R. notes that this PR harmonizes with current behavior of `HpxNDMap` and `RegionNDMap`. Decision to keep PR as is.
- [#6248](https://github.com/gammapy/gammapy/pull/6248) Decision to go for this and open reminder issue to uniformize `interp_by_coord` on `HpxNDMap` and `RegionNDMap`.
- [#6270]{https://github.com/gammapy/gammapy/pull/6270) Make `normalize` a `kwargs` in the init function to not break API. Turn into bug and include in the coming release.
- [#6259](https://github.com/gammapy/gammapy/pull/6259) In connection to issue #6258. Discussion on expected behaviour for a `SpectrumDataset`. RT recalls past choice of keeping PSF on a `MapDataset` with `RegionGeom`, while droping it if converted to a regular `SpectrumDataset`. `MapDataset.to_spectrum_Dataset()` drops the PSF. Decision to follow this logic and remove PSF from `SpectrumDataset.create()`. RT suggests to override `MapDataset.create()` to limit if else statements in the parent class. KE will try to update PR for inclusion in 2.0.1.

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

- [#6272](https://github.com/gammapy/gammapy/pull/6272) This is in fact documentation rather than bug. Add a fragment as this is more than a small fix.

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

- [#6176](https://github.com/gammapy/gammapy/pull/6176) REady to be merged. Check locally by cloning the current branch. Decision to merge today and include as part of bugfix. Significant change compared to v2.0 but transparent to the user. In the long run, it is not possible to maintain setup.cfg on v2.0.x and pyproject.toml on main.

## Validation & benchmark

## Ongoing projects

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6270](https://github.com/gammapy/gammapy/pull/6270) Add optional normalization on phasecurve models - Régis Terrier
* [#6259](https://github.com/gammapy/gammapy/pull/6259) Create PSFMap for `SpectrumDataset` only if RegionGeom `region` defined - Katharina Egg

### PRs merged last week (less than 8 days ago): 
* [#6271](https://github.com/gammapy/gammapy/pull/6271) Backport PR #6252 on branch v2.0.x (Fix plot_error for models evaluated with not finite values) - Régis Terrier
* [#6269](https://github.com/gammapy/gammapy/pull/6269) Correct CI workflow on v2.0.x to force downloading datasets from 2.0 release - Régis Terrier
* [#6268](https://github.com/gammapy/gammapy/pull/6268) Backport PR #6265 on branch v2.0.x (Adapt estimator tutorial and add warning for lin interp) - Lumberbot (aka Jack)
* [#6267](https://github.com/gammapy/gammapy/pull/6267) Backport PR #6251 on branch v2.0.x (Resolves issues associated to plot_error) - Lumberbot (aka Jack)
* [#6266](https://github.com/gammapy/gammapy/pull/6266) Change DM PPPC4 file location - Régis Terrier
* [#6265](https://github.com/gammapy/gammapy/pull/6265) Adapt estimator tutorial and add warning for lin interp - Kirsty Feijen
* [#6264](https://github.com/gammapy/gammapy/pull/6264) Backport PR #6253 on branch v2.0.x (Fix Models and DatasetModels addition for any order ) - Lumberbot (aka Jack)
* [#6263](https://github.com/gammapy/gammapy/pull/6263) Backport PR #6247 on branch v2.0.x (INFRA: Set exclusions for sonar coverage analysis) - Régis Terrier
* [#6262](https://github.com/gammapy/gammapy/pull/6262) Backport PR #6116 on branch v2.0.x (Add missing contributor in release notes for v2.0) - Régis Terrier
* [#6260](https://github.com/gammapy/gammapy/pull/6260) Backport PR #6108 on branch v2.0.x (fix Flux unit of FluxPoints object inconsistent) - Lumberbot (aka Jack)
* [#6257](https://github.com/gammapy/gammapy/pull/6257) Backport PR #6249 and #6250 on branch v2.0.x - Régis Terrier
* [#6253](https://github.com/gammapy/gammapy/pull/6253) Fix Models and DatasetModels addition for any order  - Quentin Remy
* [#6252](https://github.com/gammapy/gammapy/pull/6252) Fix plot_error for models evaluated with not finite values - Quentin Remy
* [#6251](https://github.com/gammapy/gammapy/pull/6251) Resolves issues associated to plot_error - Quentin Remy
* [#6247](https://github.com/gammapy/gammapy/pull/6247) INFRA: Set exclusions for sonar coverage analysis - Daniel Morcuende
* [#6116](https://github.com/gammapy/gammapy/pull/6116) Add missing contributor in release notes for v2.0 - Gabriel Emery

### issues opened last week (less than 8 days ago): 
* [#6258](https://github.com/gammapy/gammapy/issues/6258) `SpectrumDataset.create()` creates PSFMap that can not be applied if RegionGeom without `region` attribute - Katharina Egg

 report created at 12/12/2025, 07:28:28
