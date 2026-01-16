# Gammapy Developer Meeting 
 * Friday, January 16, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Atreyee Sinha (AS), Katharina Egg (KE), Matthias Fuessling (MF), Daniel Morcuende (DM), Fabio Pintore (FP), Livia Rocha (LR), Tomas Bylund (TB), Quentin Remy (QR)

# Agenda
## General information

## [Open issues](https://github.com/gammapy/gammapy/issues)
KE has created [#6259](https://github.com/gammapy/gammapy/pull/6259) to fix issue [#6258](https://github.com/gammapy/gammapy/issues/6258), it is ready to review.

AS volunteered to investigated the issue solved by PR [#6194](https://github.com/gammapy/gammapy/pull/6194) and see if there is some better solution.
## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)
* Issue with sonarcube complaining about the use of variable casing for `nuFnu`, but this casing is desirable in this case because it matches existing notation. DM will investigate further.
* DM plans to add python 3.14 to the CI and drop 3.10
 
## Validation & benchmark
AS highlights that it would be nice of the validation could be run on each release,  see [#179](https://github.com/gammapy/gammapy-benchmarks/issues/179).

Also raised by AS is that we are repeatedly having problems with the benchmarks failing due to hitting file size limits for the execution profiling, along with the problem of the fetching of data files failing.

## Ongoing projects
* TB created [#6299](https://github.com/gammapy/gammapy/pull/6299) to make _get_fov_coord support the case when the passed frame contains several observation time, required for properly handling drift-scan type observations. Needs review
* The PR to support projecting EffectiveAreas at several points in time, [#6194](https://github.com/gammapy/gammapy/pull/6194) is ready to review, it depends on [#6299](https://github.com/gammapy/gammapy/pull/6299). TB will try to add some diagrams to explain what is going on.

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6314](https://github.com/gammapy/gammapy/pull/6314) Minor improvement from SonarCube report (3) - Bruno Khélifi
* [#6313](https://github.com/gammapy/gammapy/pull/6313) Minor improvement from SonarCube report (2) - Bruno Khélifi
* [#6312](https://github.com/gammapy/gammapy/pull/6312) Minor improvement from SonarCube report - Bruno Khélifi

### PRs merged last week (less than 8 days ago): 
* [#6315](https://github.com/gammapy/gammapy/pull/6315) Backport PR #6305 on branch v2.0.x (Add support for numpy 2.4) - Lumberbot (aka Jack)
* [#6311](https://github.com/gammapy/gammapy/pull/6311) Backport PR #6308 on branch v2.0.x (Correct CITATION location in distribution) - Lumberbot (aka Jack)
* [#6308](https://github.com/gammapy/gammapy/pull/6308) Correct CITATION location in distribution - Régis Terrier
* [#6305](https://github.com/gammapy/gammapy/pull/6305) Add support for numpy 2.4 - Régis Terrier

### issues opened last week (less than 8 days ago): 
