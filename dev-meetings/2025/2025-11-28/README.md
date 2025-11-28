# Gammapy Developer Meeting 
 * Friday, November 28, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Régis Terrier, Tomas Bylund, Kirsty Feijen, Quentin Remy, Daniel Morcuende, Fabio Pintore, Matthias Fuessling, Atreyee Sinha, Roberto Alexander Cerviñio Cortinez, Bruno Khelifi, Aritra Gupta

# Agenda
## General information

### Conferences 
* [SPIE 2026 conference](https://spie.org/conferences-and-exhibitions/astronomical-telescopes-and-instrumentation/presenters) (Copenhagen, 5-10 July): the abstract submission deadline is December, 3rd. KF is potentially interested to present Gammapy there.
* Numerical methods conference in Greece. AS will submit Gammapy abstract soon (deadline is Monday 1 December)
* Indian multimessenger community organisation starting up, AS will present Gammapy there next week.

BK reminds everyone there is a dedicated repository to collect presentations about Gammapy.

### Gammapy 2.0 paper
Bi-weekly meetings on Fridays at 10:30. Next meeting 12th of December. Everyone is invited to look at the existing draft in a [dedicated repository](https://github.com/gammapy/gammapy-2.0-paper/wiki/Possible-skeleton-for-the-paper) and assign themselves if they wish.

### Zenodo release of v2.0
Needs to be done manually. BK will look into it.

### Unbinned analysis
No update. Need to more clearly establish meeting times.

### Dark matter 
There is a new channel on slack dedicated to dark matter development: #dark-matter.

RACC has created [#6232](https://github.com/gammapy/gammapy/pull/6232)  to add support for a new dark matter spectral source. Currently the PR proposes shipping a CosmiXs production file as part of GAMMAPY_DATA, the feasibility of this needs to be investigated further.

## [Open issues](https://github.com/gammapy/gammapy/issues)
Maxime REGEARD has found bug in the `plot_error` method of `SpectralModel`, reported in [#6228](https://github.com/gammapy/gammapy/issues/6228). Models with values close to parameter boundaries can generate samples outside the allowed range, and these "forbidden" samples are not handled properly. 

In the reported example these samples resulted in NaNs, which then prevented the use of the samples when making the plot, making the call fail.

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)
DM working on getting the sonarcube integration working completely with PR [#6231](https://github.com/gammapy/gammapy/pull/6231), there is a problem with the paths used in the CI which resulted in SonarQube not find the coverage report problem. The existing solution is a bit messy. 

DM also suggest using tox-uv to improve performance of the CI jobs.

RT opened  [#6239](https://github.com/gammapy/gammapy/issues/6239) to track the status of all the issues that sonarqube has flagged, and opened PR [#6240](https://github.com/gammapy/gammapy/pull/6240)  to solve some of the flagged issues.

KF calls attention to PR [#6223](https://github.com/gammapy/gammapy/pull/6223) that updates the script for generating the list of contributors to a certain release. It is ready for review.

## Validation & benchmark

## Ongoing projects

## Any other business
AS raises a question about the 1D Spectrum simulation tutorial, where the faking example uses no containment correction but also disregards the PSF. Nobody is certain if this entirely correct, AS  will open an issue.

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6240](https://github.com/gammapy/gammapy/pull/6240) Cleanup: Solves some reliability issues from SonarQube - Régis Terrier
* [#6232](https://github.com/gammapy/gammapy/pull/6232) Dark Matter module: Include the option of using either CosmiXs or PPPC4 as a source for creating the DM spectra - None
* [#6231](https://github.com/gammapy/gammapy/pull/6231) Infra: Fix parsing paths in coverage report for SonarQube - Daniel Morcuende

### PRs merged last week (less than 8 days ago): 
* [#6236](https://github.com/gammapy/gammapy/pull/6236) Backport PR #6235 on branch v2.0.x (Fix astropy deprecation) - Lumberbot (aka Jack)
* [#6235](https://github.com/gammapy/gammapy/pull/6235) Fix astropy deprecation - Régis Terrier
* [#6234](https://github.com/gammapy/gammapy/pull/6234) Backport PR #6137 on branch v2.0.x (Adapt size_factor value for error) - Lumberbot (aka Jack)
* [#6233](https://github.com/gammapy/gammapy/pull/6233) Backport PR #6173 on branch v2.0.x (Add missing fragment files for bug release) - Lumberbot (aka Jack)
* [#6230](https://github.com/gammapy/gammapy/pull/6230) Backport PR #6224 on branch v2.0.x (Fix the way labels are fetched for changelog check) - Lumberbot (aka Jack)
* [#6224](https://github.com/gammapy/gammapy/pull/6224) Fix the way labels are fetched for changelog check - Daniel Morcuende
* [#6222](https://github.com/gammapy/gammapy/pull/6222) Update mailmap with old email addresses - Daniel Morcuende
* [#6213](https://github.com/gammapy/gammapy/pull/6213) Add a link towards the `npred` computation into the stats user-guide page - Bruno Khélifi
* [#6173](https://github.com/gammapy/gammapy/pull/6173) Add missing fragment files for bug release - Kirsty Feijen
* [#6150](https://github.com/gammapy/gammapy/pull/6150) Sonarqube integration - Daniel Morcuende
* [#6147](https://github.com/gammapy/gammapy/pull/6147) Add Logparabola2Spectral model - Quentin Remy
* [#6137](https://github.com/gammapy/gammapy/pull/6137) Adapt size_factor value for error - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6239](https://github.com/gammapy/gammapy/issues/6239) SonarQube Reliability Issues - Régis Terrier
* [#6238](https://github.com/gammapy/gammapy/issues/6238) Speed up CI using tox-uv - Daniel Morcuende
* [#6237](https://github.com/gammapy/gammapy/issues/6237) Cache gammapy-dataset and test environments in CI - Daniel Morcuende
* [#6229](https://github.com/gammapy/gammapy/issues/6229) Negative `lambda_` and non-integer `alpha` in `ExpCutoffPowerLawSpectralModel` returns NaN - REGEARD Maxime
* [#6228](https://github.com/gammapy/gammapy/issues/6228) `plot_error` method of `SpectralModel` can fail by sampling specific parameter values - REGEARD Maxime

 report created at 28/11/2025, 07:25:40

