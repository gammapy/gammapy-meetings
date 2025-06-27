# Gammapy Developer Meeting 
 * Friday, June 27, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

## Participants 
(Zoom display names, zoom chosen order)
Axel Donath, Tomas Bylund, Hanna Stapel, Régis Terrier, Kirsty Feijen, Samantha Wong, Matthias Fuessling, Claudio Galelli, Katharina Egg, Daniel Morcuende 

# Agenda

## Information
### CTAO school
Kirsty reports that things went well, about 20 students.

### EAS gammapy session
Katharina was only zoom participant, things seemed to go well

## Recurring items
### Open issues
No report

### Bugs
Atreyee created a [list of bugs](https://github.com/gammapy/gammapy/issues?q=state%3Aopen%20label%3Abug%20milestone%3A2.0) to be solved for the 2.0 milestone, most have been assigned.

### Documentation
Kirsty has been working on the reorganisation of the documentation, she has a local draft and will open a pull request today to allow for further discussion.

Axel has talked to NumFOCUS and gotten contact information to some of their technical writers, who could provide feedback on the existing documentation. Would be interesting to hear their feedback on it, after 2.0 has shipped

Samantha reports that the licencing of the VERITAS data will hopefully be resolved by Tuesday next week, but meanwhile the build in the CI fails because the data is missing. 
She has tried building it locally and is working on consolidating the tutorial to not repeat material already documented in other places in the gammapy documentation. 
Kirsty reports she has successfully built the tutorial locally and shared a link to where she has hosted it.

The VERITAS tutorial created a discussion about the proper way to handle the creation of exclusion masks from stellar and VHE catalogues. Regis said this is a big discussion that should be postponed until more core developers are present.

Kirsty has created a draft PR that implements a `check_tutorials_setup` function and cli command that will print the environment and also download the data files if they are not found. With this merged most calls to `check_setup` at the start of every tutorial can be safely removed.

### DevOps
All documentation is built using old numpy version because the build was configured to use an old python version. Regis has opened a pull request upgrading the python version. 
It is notable that upgrading the python version was forgotten, it needs to be investigated if dependabot can be made to keep track of this

A PR that allows for skipping parts of the CI process is ready to review 

### Validation & benchmark
Daniel has created an issue reporting that the lightcurve validation seems to be broken, he will investigate.

We also found that the benchmarks have not been produced for all minor releases since 1.1, these should be produced and an instruction about it will be added to the developer documentation (in the release section presumably?)

Kirsty ask how the stacking functionality to the LightCurveEstimator should be tested. Regis replied but I didn't follow.

### Ongoing projects:
    - sensi
    - HLI
    - MWL
No report

## Any other Business
Regis reports there are about 30 open pull requests scheduled for 2.0 that needs to be reviewed and merged.

Regis raised PR 5865 that tries to solve the problem that users sometimes get attribute names wrong and set completely new attributes on (for example) a datasets instead of updating the attribute that gammapy uses.
After a discussion the PR was moved to the whislist.

Regis has started the process of collecting the contributor info that goes into the `citation.cff` file. There is still space for someone to volunteer to write the changelog.

## Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#5947](https://github.com/gammapy/gammapy/pull/5947) [PIG] Systematics Modifier API - Stefan Fröse
* [#5945](https://github.com/gammapy/gammapy/pull/5945) Create exclusion.py - Samantha Wong
* [#5944](https://github.com/gammapy/gammapy/pull/5944) Add unit support on HpxGeom - Régis Terrier
* [#5941](https://github.com/gammapy/gammapy/pull/5941) Tutorial setup command line option - Kirsty Feijen
* [#5939](https://github.com/gammapy/gammapy/pull/5939) Update citation.cff for v2.0 - Régis Terrier
* [#5938](https://github.com/gammapy/gammapy/pull/5938) ci: allow to skip ci step using PR labels - npigoux
* [#5937](https://github.com/gammapy/gammapy/pull/5937) Remove binlike from testing - Kirsty Feijen
* [#5936](https://github.com/gammapy/gammapy/pull/5936) Update of the user guide documentation of `Modelling and Fitting` - Bruno Khélifi
* [#5934](https://github.com/gammapy/gammapy/pull/5934) Estimator documentation: update the n_sigma description - Bruno Khélifi

### PRs merged last week (less than 8 days ago): 
* [#5942](https://github.com/gammapy/gammapy/pull/5942) Test CI fail mentioned in #4438 - Atreyee Sinha
* [#5940](https://github.com/gammapy/gammapy/pull/5940) Update sherpa message and add gammapy info to docs - Kirsty Feijen
* [#5925](https://github.com/gammapy/gammapy/pull/5925) Adapt docstring for `ReflectedRegionsFinder` - Kirsty Feijen
* [#5924](https://github.com/gammapy/gammapy/pull/5924) Cleanup of psf functionalities - Kirsty Feijen
* [#5922](https://github.com/gammapy/gammapy/pull/5922) Clean up of `irf/background.py` - Kirsty Feijen
* [#5921](https://github.com/gammapy/gammapy/pull/5921) Add `Notes` section to `HpxMap`,  `HpxNDMap` and `HpxGeom` - Kirsty Feijen
* [#5919](https://github.com/gammapy/gammapy/pull/5919) Add notes to `RegionGeom` and `RegionNDMap` - Kirsty Feijen
* [#5916](https://github.com/gammapy/gammapy/pull/5916)  Fix link label display in parameters.to_table - Quentin Remy
* [#5914](https://github.com/gammapy/gammapy/pull/5914) Modify sampler to handle linked params in models - Fabio Acero
* [#5905](https://github.com/gammapy/gammapy/pull/5905) Fix documentation of of the installation - Bruno Khélifi
* [#5897](https://github.com/gammapy/gammapy/pull/5897) Examples for estimator utils - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#5946](https://github.com/gammapy/gammapy/issues/5946) For HAWC, `ObservationTable.select_sky_circle` crashes - Bruno Khélifi
* [#5943](https://github.com/gammapy/gammapy/issues/5943) DataStore.get_observations duplicates - Régis Terrier
* [#5935](https://github.com/gammapy/gammapy/issues/5935) Confusion between predicted counts and background predicted counts - Juan 
