# Gammapy Developer Meeting 
 * Friday, February 06, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Tomas Bylund (TB), Regis Terrier (RT), Bruno Khelifi (BK), Marie Carrasco (MC), Kirsty Feijen (KF), Atreyee Sinha (AS), Claudio Galelli (CG), Livia Silva Rocha (LR), Daniel Morcuende (DM), Matthias Fuessling (MF)
 Katharina Egg (KE), Quentin Remy (QR), Fabio Pintore (FP), Fabio Acero (FA), Nathan Pigoux (NP)

# Agenda
## General information

### Google summer of code
KF submitted proposal via Numfocus (realised too late to submit via Open Astronomy): project to add capability to serialise models to ASDF, RT and KF as mentors. 

A bit unclear when we will know if we get any intern.

AS was contacted by an interested computer science student asking if there will be a 

### Next user call
Mathieu de Bony interested in giving a talk, AS will propose a date. Will be held in the morning.

### Next coding sprint
LST inauguration and collaboration meeting week 42 (October 12-October 18) and the CTAO construction meeting week 43. Idea is to hold coding sprint around then.

Possibly a spring sprint, in April or May. A doodle will be create in the dev-channel.

Last coding sprint in Paris was in December 2022.

### Design documents for the Critical design reviews
We need to write them, unclear who will, when they will, and what they should contain. 

## [Open issues](https://github.com/gammapy/gammapy/issues)
 [#6375](https://github.com/gammapy/gammapy/issues/6375) reports an issue with the FermipyDatasetsReader, the primary suspect was the users config. We decided to request more information before doing anything else.

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)
A lof of PR has been opened and merged to fix issues highlighed by sonarcube.

## Validation & benchmark

## Ongoing projects

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6378](https://github.com/gammapy/gammapy/pull/6378) add GTI to FermipyDataset - Tora T H Arnesen
* [#6371](https://github.com/gammapy/gammapy/pull/6371) MAJOR fixes for Sonar Qube - Kirsty Feijen
* [#6360](https://github.com/gammapy/gammapy/pull/6360) Do not perform equality checks with floating point values - Bruno Khélifi
* [#6357](https://github.com/gammapy/gammapy/pull/6357) Example PR: Using `Enum` for option-like arguments ? - Maxime Regeard
* [#6348](https://github.com/gammapy/gammapy/pull/6348) Improve functionalities of makers.make_theta_squared_table - Fabio PINTORE

### PRs merged last week (less than 8 days ago): 
* [#6377](https://github.com/gammapy/gammapy/pull/6377) Backport PR #6102 on branch v2.0.x (jfactory integral calculation description) - Lumberbot (aka Jack)
* [#6376](https://github.com/gammapy/gammapy/pull/6376) Backport PR #6353 on branch v2.0.x (Propagate the argument `size_fraction` into `SpatialModel._to_region_error()`) - Lumberbot (aka Jack)
* [#6374](https://github.com/gammapy/gammapy/pull/6374) Backport PR #6365 on branch v2.0.x (SonarQube remove self-assignment and clean up for docs build) - Lumberbot (aka Jack)
* [#6373](https://github.com/gammapy/gammapy/pull/6373) Backport PR #6367 on branch v2.0.x (Correct bug with CLI gamma analysis run) - Lumberbot (aka Jack)
* [#6372](https://github.com/gammapy/gammapy/pull/6372) Backport PR #6366 on branch v2.0.x (Adds SonarQube exceptions for cache tests) - Lumberbot (aka Jack)
* [#6370](https://github.com/gammapy/gammapy/pull/6370) Fix docs non-backported - Kirsty Feijen
* [#6369](https://github.com/gammapy/gammapy/pull/6369) Backport PR #6358 on branch v2.0.x (Use "np.nonzero" for SonarQube - Part 2) - Lumberbot (aka Jack)
* [#6368](https://github.com/gammapy/gammapy/pull/6368) Backport PR #6359 on branch v2.0.x (Use "np.nonzero" for SonarQube - Part 3) - Lumberbot (aka Jack)
* [#6367](https://github.com/gammapy/gammapy/pull/6367) Correct bug with CLI gamma analysis run - Régis Terrier
* [#6366](https://github.com/gammapy/gammapy/pull/6366) Adds SonarQube exceptions for cache tests - Quentin Remy
* [#6365](https://github.com/gammapy/gammapy/pull/6365) SonarQube remove self-assignment and clean up for docs build - Kirsty Feijen
* [#6364](https://github.com/gammapy/gammapy/pull/6364) Backport PR #6349 on branch v2.0.x (Fix fragments) - Lumberbot (aka Jack)
* [#6363](https://github.com/gammapy/gammapy/pull/6363) Backport PR #6355 on branch v2.0.x (Use "np.nonzero" for SonarQube - Part 1) - Lumberbot (aka Jack)
* [#6362](https://github.com/gammapy/gammapy/pull/6362) Backport PR #6361 on branch v2.0.x (Delete unreachable code) - Lumberbot (aka Jack)
* [#6361](https://github.com/gammapy/gammapy/pull/6361) Delete unreachable code - Bruno Khélifi
* [#6359](https://github.com/gammapy/gammapy/pull/6359) Use "np.nonzero" for SonarQube - Part 3 - Kirsty Feijen
* [#6358](https://github.com/gammapy/gammapy/pull/6358) Use "np.nonzero" for SonarQube - Part 2 - Kirsty Feijen
* [#6355](https://github.com/gammapy/gammapy/pull/6355) Use "np.nonzero" for SonarQube - Part 1 - Kirsty Feijen
* [#6354](https://github.com/gammapy/gammapy/pull/6354) Fix `is not` statement for SonarQube - Kirsty Feijen
* [#6353](https://github.com/gammapy/gammapy/pull/6353) Propagate the argument `size_fraction` into `SpatialModel._to_region_error()` - Bruno Khélifi
* [#6352](https://github.com/gammapy/gammapy/pull/6352) Backport PR #6351 on branch v2.0.x (Update setuptools version in `pyproject.toml build-system`) - Lumberbot (aka Jack)
* [#6351](https://github.com/gammapy/gammapy/pull/6351) Update setuptools version in `pyproject.toml build-system` - Maxime Regeard
* [#6349](https://github.com/gammapy/gammapy/pull/6349) Fix fragments - Kirsty Feijen
* [#6347](https://github.com/gammapy/gammapy/pull/6347) Backport PR #6298 on branch v2.0.x (Fix physics error: Use mass/2 for DM decay spectrum lookup) - Lumberbot (aka Jack)
* [#6346](https://github.com/gammapy/gammapy/pull/6346) Backport PR #6194 on branch v2.0.x (Add fix to skip making cutouts if observation is far away from target…) - Lumberbot (aka Jack)
* [#6344](https://github.com/gammapy/gammapy/pull/6344) Backport PR #6338 on branch v2.0.x (Add missing tests for makers.utils) - Lumberbot (aka Jack)
* [#6343](https://github.com/gammapy/gammapy/pull/6343) Backport PR #6314 on branch v2.0.x (Minor improvement from SonarCube report (3)) - Lumberbot (aka Jack)
* [#6342](https://github.com/gammapy/gammapy/pull/6342) Backport PR #6312 on branch v2.0.x (Minor improvement from SonarCube report) - Lumberbot (aka Jack)
* [#6340](https://github.com/gammapy/gammapy/pull/6340) Remove deprecations for v2.1 - Kirsty Feijen
* [#6338](https://github.com/gammapy/gammapy/pull/6338) Add missing tests for makers.utils - Kirsty Feijen
* [#6314](https://github.com/gammapy/gammapy/pull/6314) Minor improvement from SonarCube report (3) - Bruno Khélifi
* [#6312](https://github.com/gammapy/gammapy/pull/6312) Minor improvement from SonarCube report - Bruno Khélifi
* [#6298](https://github.com/gammapy/gammapy/pull/6298) Fix physics error: Use mass/2 for DM decay spectrum lookup - Y. Emre Bahar

### issues opened last week (less than 8 days ago): 
* [#6375](https://github.com/gammapy/gammapy/issues/6375) FermipyDatasetsReader.read() incompatible with fermipy 1.4.0 - Michele Peresano
* [#6356](https://github.com/gammapy/gammapy/issues/6356) Using `Enum` for option-like arguments ? - Maxime Regeard

 report created at 06/02/2026, 07:50:33
