# Gammapy Developer Meeting 
 * Friday, February 20, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Tomas Bylund (TB), Livia Silvia Rocha (LR),  Regis Terrier (RT), Daniel Morcuende (DM), Basmala Hekal (BH), Marie-Sophie Carrasco (MC), Natthan Pigoux (NP), Quentin Remy (QR), Bruno Khelifi (BK), Katharina Egg (KE)

# Agenda
## General information

### Next coding sprint
Paris, April 27 to 30th [See page](https://github.com/gammapy/gammapy-meetings/tree/master/coding-sprints/2026-04-APC)

### Gammapy Release 2.1
March 13, next week we will tag a release candidate. Many issues and PRs to solve before then!

## [Open issues](https://github.com/gammapy/gammapy/issues)
PR [#6409](https://github.com/gammapy/gammapy/pull/6409),  solving an issue where the minimiser could get beyond the bounds of the prior and then get irrecoverably stuck. However the automatic tests revealed an design issue where at serialisation time the priors are expected to have a prior because they are inheriting from `Parameter`. This needs a proper solution, in a separate PR. 

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

## Validation & benchmark

## Ongoing projects

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6420](https://github.com/gammapy/gammapy/pull/6420) refactor: remove linting dependencies - Natthan Pigoux
* [#6416](https://github.com/gammapy/gammapy/pull/6416) Extends the `set_and_restore_mask_fit` context manager - Quentin Remy
* [#6415](https://github.com/gammapy/gammapy/pull/6415) Fix SonarQube reliability issue with dict key access - Marie-Sophie Carrasco
* [#6409](https://github.com/gammapy/gammapy/pull/6409) sync Parameter min/max with bounded prior bounds dynamically - Ebraam 
* [#6407](https://github.com/gammapy/gammapy/pull/6407) Modify info script to use importlib.metadata and fix deprecation warning - Basmala Hekal
* [#6406](https://github.com/gammapy/gammapy/pull/6406) Correct the developement docs and towncrier fragment - Kirsty Feijen
* [#6402](https://github.com/gammapy/gammapy/pull/6402) Sonar analysis on tagged versions - Daniel Morcuende
* [#6398](https://github.com/gammapy/gammapy/pull/6398) Address UserWarning for setting units converter several times, lift matplotlib version upper bound, require astropy>=6.1.5 - Daniel Morcuende

### PRs merged last week (less than 8 days ago): 
* [#6419](https://github.com/gammapy/gammapy/pull/6419) Backport PR #6410 on branch v2.0.x (SonarQube relability major fix for identical sub-expressions) - Lumberbot (aka Jack)
* [#6418](https://github.com/gammapy/gammapy/pull/6418) Backport PR #6412 on branch v2.0.x (Fix SonarQube reliability issue with reassigned variables) - Lumberbot (aka Jack)
* [#6413](https://github.com/gammapy/gammapy/pull/6413) Backport PR #6411 on branch v2.0.x (Fix SonarQube relability for `Priors`) - Lumberbot (aka Jack)
* [#6412](https://github.com/gammapy/gammapy/pull/6412) Fix SonarQube reliability issue with reassigned variables - Marie-Sophie Carrasco
* [#6411](https://github.com/gammapy/gammapy/pull/6411) Fix SonarQube relability for `Priors` - Kirsty Feijen
* [#6410](https://github.com/gammapy/gammapy/pull/6410) SonarQube relability major fix for identical sub-expressions - Kirsty Feijen
* [#6408](https://github.com/gammapy/gammapy/pull/6408) Backport PR #6405 on branch v2.0.x (Remove deprecated json_encoders in workflow) - Lumberbot (aka Jack)
* [#6405](https://github.com/gammapy/gammapy/pull/6405) Remove deprecated json_encoders in workflow - Régis Terrier
* [#6396](https://github.com/gammapy/gammapy/pull/6396) Update CI and code quality sections in docs - Daniel Morcuende
* [#6392](https://github.com/gammapy/gammapy/pull/6392) Backport PR #6383 on branch v2.0.x (Correct off-by-one error in `WcsGeom.pix_to_idx` clipping) - Lumberbot (aka Jack)
* [#6391](https://github.com/gammapy/gammapy/pull/6391) Backport PR #6388 on branch v2.0.x (Fix HPX pix_to_idx handling of non-spatial pix and add regression test) - Lumberbot (aka Jack)
* [#6390](https://github.com/gammapy/gammapy/pull/6390) Backport PR #6360 on branch v2.0.x (Do not perform equality checks with floating point values) - Lumberbot (aka Jack)
* [#6388](https://github.com/gammapy/gammapy/pull/6388) Fix HPX pix_to_idx handling of non-spatial pix and add regression test - None
* [#6386](https://github.com/gammapy/gammapy/pull/6386) fix(maps): align TimeMapAxis pixel convention with MapAxis; add round… - None
* [#6383](https://github.com/gammapy/gammapy/pull/6383) Correct off-by-one error in `WcsGeom.pix_to_idx` clipping - None
* [#6360](https://github.com/gammapy/gammapy/pull/6360) Do not perform equality checks with floating point values - Bruno Khélifi

### issues opened last week (less than 8 days ago): 
* [#6417](https://github.com/gammapy/gammapy/issues/6417) Add lstat to the list of supported statistics - Régis Terrier
* [#6414](https://github.com/gammapy/gammapy/issues/6414) Modify project metadata to be compliant with Zenodo expectation for EU funded projects - Régis Terrier
* [#6404](https://github.com/gammapy/gammapy/issues/6404) Modify gammapy info script to use importlib.metadata - Régis Terrier
* [#6403](https://github.com/gammapy/gammapy/issues/6403) Fix warning messages in tutorials - Kirsty Feijen
* [#6401](https://github.com/gammapy/gammapy/issues/6401) SonarQube reliability: attribute access on a value that can be 'None'. - Régis Terrier
* [#6400](https://github.com/gammapy/gammapy/issues/6400) "gammapy download" uses dependences that are not included with gammapy - Karl Kosack
* [#6399](https://github.com/gammapy/gammapy/issues/6399) Lift matplotlib upper version bound (<3.10) - Daniel Morcuende
* [#6397](https://github.com/gammapy/gammapy/issues/6397) Defining parameters Priors when no min/max is set - Fabio Acero
* [#6395](https://github.com/gammapy/gammapy/issues/6395) AI use in Gammapy - Bruno Khélifi
* [#6394](https://github.com/gammapy/gammapy/issues/6394) Binder link in README not working - Daniel Morcuende
* [#6393](https://github.com/gammapy/gammapy/issues/6393) Implement Highest Density Region (HDR) for sample results ? - Fabio Acero

 report created at 20/02/2026, 07:51:02
