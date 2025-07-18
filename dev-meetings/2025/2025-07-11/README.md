# Gammapy Developer Meeting 
 * Friday, July 11, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
 * Attendees: Régis Terrier (RT), Tomas Bylund (TB), Leander Schlegel (LS), Katharina Egg (KE), Quentin Remy (QR), Daniel Morcuende (DM), Fabio Pintore (FP), Bruno Khelifi (BK), Atreyee Sinha (AS) (after 15:15)
 
# Agenda

* DPPS Benchmarking system as inspiration of the Science tools testbench. TB: not so much technically that can be reused because inputs are quite different. DM: Need to understand if the current gammapy-benchmarking repository is enough for release 0 of the science analysis tools.

* Code freeze hopefully next week.

## Information

## Recurring items

### Open Pull Requests 
* [#5971](https://github.com/gammapy/gammapy/pull/5971) SpectrumDatasetChi2 by Mireia Nievas-Rosillo. RT: It is interesting but maybe it should go into gammapy- multiwavelength framework
* [#5972](https://github.com/gammapy/gammapy/issues/5972) Is there a good solution to avoid CI / Actions running on forks? by Leander Schlegel. RT: making it so the CI runs manually is acceptable solution, Leander to update development documentation
* [#5969](https://github.com/gammapy/gammapy/issues/5969) Add tutorial for non-detected sources by Atreyee Sinha. RT and BK: The tutorial needs some work to make it clear it only covers some situations where you want to compute upper limits.
* [#5960](https://github.com/gammapy/gammapy/pull/5960) Energy edges instead of center for aeff-max in SafeMaskMaker - Kirsty Feijen. The proposed PR does not work, after an extensive discussion the proposed solution to the original issue is to update the documentation to say you can skip the safe mask maker if you want to keep the first bin. An issue should be created to discuss ways to improve the SafeMaskMaker, for example to calculate the mask in reco energy instead of true energy.

### Open issues
* [#5549](https://github.com/gammapy/gammapy/issues/5549) TemplateSpatialModel serialisation is not  backward compatible- Quentin Remy. The science data challenge will probably need gammapy to support both old and new models, and so this issue needs to be resolved before SDC really starts production. BK is assigned.

### Bugs

### Documentation

### DevOps

### Validation & benchmark

### Ongoing projects:
    - sensitivity: Nothing to report
    - HLI: RT proposes that we organise a meeting about the High level interface, with the aim to write down a design so everyone knows what is to be done. QR asks if it should be split out into a separate project. RT will circulate a poll to find a date for this meeting, probably last week of September.
        - MWL: Nothing to report

## Any other Business
* AS asks about the memory leak issue [#5706](https://github.com/gammapy/gammapy/issues/5706) . No immediate

### PRs opened last week (less than 8 days ago): 
* [#5977](https://github.com/gammapy/gammapy/pull/5977) Update docs of counts_statistic.py - Atreyee Sinha
* [#5976](https://github.com/gammapy/gammapy/pull/5976) Add option to convert PointSkyRegion to CircleSkyRegion while creating masks - Atreyee Sinha
* [#5975](https://github.com/gammapy/gammapy/pull/5975) Allow configuration of x_width in Models.to_regions - Atreyee Sinha
* [#5974](https://github.com/gammapy/gammapy/pull/5974) Fix links label for CompoundSpectralModel - Quentin Remy
* [#5973](https://github.com/gammapy/gammapy/pull/5973) Warn users when using negative amplitude models in FluxEstimator - Atreyee Sinha
* [#5971](https://github.com/gammapy/gammapy/pull/5971) SpectrumDatasetChi2 (SpectrumDataset with chi2 statistics) - Mireia Nievas-Rosillo
* [#5969](https://github.com/gammapy/gammapy/pull/5969) Add tutorial for non-detected sources - Atreyee Sinha

### PRs merged last week (less than 8 days ago): 
* [#5967](https://github.com/gammapy/gammapy/pull/5967) Part 2 - Tutorial cleanup - Kirsty Feijen
* [#5966](https://github.com/gammapy/gammapy/pull/5966) Part 1 - Tutorial cleanup - Kirsty Feijen
* [#5965](https://github.com/gammapy/gammapy/pull/5965) fix typo in makers tutorial - Fabio Acero
* [#5964](https://github.com/gammapy/gammapy/pull/5964) Fix for Issue #5943 - Leander Schlegel
* [#5959](https://github.com/gammapy/gammapy/pull/5959) Adapt SafeMaskMaker docstring - Kirsty Feijen
* [#5957](https://github.com/gammapy/gammapy/pull/5957) Fix  #5951 - Atreyee Sinha
* [#5956](https://github.com/gammapy/gammapy/pull/5956) Fix tests of EnergyDependentMorphologyEstimator - Atreyee Sinha
* [#5944](https://github.com/gammapy/gammapy/pull/5944) Add unit support on HpxGeom - Régis Terrier
* [#5938](https://github.com/gammapy/gammapy/pull/5938) ci: allow to skip ci step using PR labels - npigoux
* [#5937](https://github.com/gammapy/gammapy/pull/5937) Remove binlike from testing - Kirsty Feijen
* [#5894](https://github.com/gammapy/gammapy/pull/5894) Adapt plot function default labels - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#5972](https://github.com/gammapy/gammapy/issues/5972) Is there a good solution to avoid CI / Actions running on forks? - Leander Schlegel
* [#5970](https://github.com/gammapy/gammapy/issues/5970) SpectrumDataset with chi2 statistics - Mireia Nievas-Rosillo

 report created at 11/07/2025, 07:26:32
