# Gammapy Developer Meeting 
 * Friday, October 03, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Régis Terrier (RT), Quentin Remy (QR), Kirsty Feijen (KF), Leander Schlegel (LS), Natthan Pigoux (NP), Tomas Bylund (TB), Claudio Galelli (CG), Axel Donath (AD)

# Agenda
## General information

AS can not attend today and will present the plotters PIG next week.

RT reports on progress with Gammapy recipes this morning. The problem is, that the CI doesn't publish changes even as PRs are merged. Current setup is a bit complex and is not simply a Sphinx build, but requires extra scripts to generate all the pages.

Each recipe needs a yaml-file for the environment.
Suggestion was to use pixi. One file contains for each recipe the dependencies. pixi can generate with few commands the rst-files, that are then processed by Sphinx.

Hope with switching to pixi is, that it will be easier to build  the final Sphinx documentation out of the Jupyter notebooks that currently implement the recipes, even as it adds a new system. There exists a PR and RT encourages it to be merged quickly, AD took a look and thinks it looks good, ND reports good experience with pixi for Gammapy.


## Open issues

## Bugs

- error in PhaseCurve should be fixed by [#6182](https://github.com/gammapy/gammapy/pull/6182)
  
Maybe additional test is missing, but current change does not break existing test.
Plan is to finish review of integration in PR, merge it and then maybe introduce a boolean option to normalize the phase curve or not (Modification of automatic normalization of phase curve introduced in 1.3), with a second PR. Question is if it can be merged as a bugfix or not, RT thinks it can and nobody objected.

## Documentation

- checklist for PR reviews added [#6179](https://github.com/gammapy/gammapy/pull/6179)
  
RT suggests to restructure the list, first milestones and labels, then functionality, then code style, then docstrings+examples. Two additional points suggested by RT and QR: Code should be understandable by reading it + It should be checked that the CI and tests pass. LS will fix broken links and implement changes and KF will add note for towncrier.


## DevOps

- towncrier PR needs reviews [#6130](https://github.com/gammapy/gammapy/pull/6130)
- fragment files added for PRs where it was missed (discussion on this)
- sonarqube also needs reviews [#6150](https://github.com/gammapy/gammapy/pull/6150)
- moving from setup.cfg to pyproject.toml PR has been begun [#6176](https://github.com/gammapy/gammapy/pull/6176) (NP)
  
 RT cautions that `codestyle` should not be removed without first ensuring some other program takes over this task even for edits made directly via the github web interface. This change might also fix a problem that the citation file not properly found when doing a release.

- ND reports he has started work on transitioning Gammapy to use pixi

## Validation & benchmark
- Follow up on the failure of the benchmark run on September 27
  
Just the sherpa install that failed because the servers were down

## Ongoing projects
[#6170](https://github.com/gammapy/gammapy/pull/6170) Introduce ObservationTableReader and Converter between GADF and internal format - Leander Schlegel

Most points from reviews have been addressed. LS reports on two open points, how to best proceed with the deprecated feature in astropy and if the try-except statements capturing a potential wrong dimension of the time-columns and raising a warning in this case, can be checked.
Decision is to take test for not found HDU-extension out, as the default is to not specify it (hdu=None) and in most cases the observation table file will also not contain more than one HDU-extension, so that no failure or deprecation warning happens in most cases.
With this, final review can be done and PR can be merged soon. Then a second PR introducing the new data format to the observation-table itself is planned. For the next step, RT plans that we add a proper writer.

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6182](https://github.com/gammapy/gammapy/pull/6182) Correct PhaseCurveTemporalModel integration bug - Régis Terrier
* [#6179](https://github.com/gammapy/gammapy/pull/6179) Add Checklist for Codereview in Developer Guide - Leander Schlegel
* [#6176](https://github.com/gammapy/gammapy/pull/6176) infra: drop setup cfg for pyproject - npigoux
* [#6173](https://github.com/gammapy/gammapy/pull/6173) Add missing fragment files for next version - Kirsty Feijen
* [#6170](https://github.com/gammapy/gammapy/pull/6170) Introduce ObservationTableReader and Converter between GADF and internal format - Leander Schlegel

### PRs merged last week (less than 8 days ago): 
* [#6180](https://github.com/gammapy/gammapy/pull/6180) Backport PR #6177 on branch v2.0.x (Bump peter-evans/repository-dispatch from 3 to 4) - Lumberbot (aka Jack)
* [#6178](https://github.com/gammapy/gammapy/pull/6178) Bump actions/setup-python from 5 to 6 - None
* [#6177](https://github.com/gammapy/gammapy/pull/6177) Bump peter-evans/repository-dispatch from 3 to 4 - None
* [#6172](https://github.com/gammapy/gammapy/pull/6172) Backport PR #6164 on branch v2.0.x (Fix division in error calculations for compute_flux_doubling) - Lumberbot (aka Jack)
* [#6171](https://github.com/gammapy/gammapy/pull/6171) Backport PR #6142 on branch v2.0.x (Add further information about fitting to the Low Level Analysis tutorial) - Lumberbot (aka Jack)
* [#6169](https://github.com/gammapy/gammapy/pull/6169) Backport PR #6158 on branch v2.0.x (Add further test for sensitivity) - Lumberbot (aka Jack)
* [#6168](https://github.com/gammapy/gammapy/pull/6168) Add __len__ to eventlist - Tomas Bylund
* [#6167](https://github.com/gammapy/gammapy/pull/6167) Backport PR #6162 on branch v2.0.x (Fix small formatting issues in user guide) - Lumberbot (aka Jack)
* [#6164](https://github.com/gammapy/gammapy/pull/6164) Fix division in error calculations for compute_flux_doubling - Pierre Pichard
* [#6162](https://github.com/gammapy/gammapy/pull/6162) Fix small formatting issues in user guide - Leander Schlegel
* [#6158](https://github.com/gammapy/gammapy/pull/6158) Add further test for sensitivity - Kirsty Feijen
* [#6142](https://github.com/gammapy/gammapy/pull/6142) Add further information about fitting to the Low Level Analysis tutorial - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6181](https://github.com/gammapy/gammapy/issues/6181) Acknowledgement and citation functions do not work - Régis Terrier
* [#6175](https://github.com/gammapy/gammapy/issues/6175) Replace "data" by "table" in ObservationTableReader - Leander Schlegel
* [#6174](https://github.com/gammapy/gammapy/issues/6174) Update code quality section in developers documentation - Daniel Morcuende

 report created at 03/10/2025, 07:22:14
