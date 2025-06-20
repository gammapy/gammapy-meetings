# Gammapy Developer Meeting 
 * Friday, June 20, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

## Participants 
(Zoom display names, zoom chosen order)
Bruno Khelifi, Tomas Bylund, Natthan Pigoux, Quentin Remy, Atreyee Sinha, Fabio Pintore, Daniel Morcuende, Kirsty Feijen, Fabio Acero, Hanna Stapel, Axel Donath, Jean-Philippe Lenain, Régis Terrier, Samantha Wong.

# Agenda

### SAT IKC latest news
* [presentation](./DevCall_IKC_20250620_v1.pdf)

### Gammapy organisation

* unordered list:
  - Open issues
  - Bugs
  - Documentation
  - DevOps
  - Validation & benchmark
  - Ongoing projects:
    - sensi
    - HLI
    - MWL
    - AoB

### Documentation
* There were a number of PRs opened (some merged) in a general clean up of the documentation
* We should make a decision on the following:
   * Proposal for re-ordering the tutorials [#5796](https://github.com/gammapy/gammapy/issues/5796)
   * Removing the setup in every tutorial [#5816](https://github.com/gammapy/gammapy/issues/5816)

### Features
* How to support the default plot labels [#5894](https://github.com/gammapy/gammapy/pull/5894)
* How to correctly test the stacking functionality for LightCurveEstimator [#5898](https://github.com/gammapy/gammapy/pull/5898)

# Minutes
## SAT IKC latest news
* Bruno presented news about the CTAO Science Analysis Tools project. 
* Bruno reminded the meeting that the In kind contribution includes two year of bug fixes after the hand-over of the tools.
* Formally there are 38 FTEs in the project, but by Bruno's count there are currently around 42 FTEs already used up and experience tells us that the work needed is frequently underestimated.
* Bruno showed a release plan  

    * SAT release 0 to happen by September 30 in 2025

    * SAT release 1 to happen by January 31 in 2026

    * Final acceptance release to be delivered by end of September 2027

* Bruno suggests that the release plan should be aligned with the IKC review process 
* Bruno suggests we start working on defining a project dedicated to the maintenance and upgrade of the SAT
* Bruno warns that there is a coming cost in terms of work on the verification documentation.
* Bruno provides an overview of work defining the VOD format

### Questions
* Quentin asked who would provide for the science data challenge, would the Gammapy devs have to provide this? Bruno says this is a good question, not clear how it will work but CTAO  will somehow provide support.
* After a question from Quentin, Daniel clarifies that the SAT will mostly be an import of gammapy that lives in and is managed via gitlab with additional CTAO-specific documentation and possibly some additional functionalities. The plan is being worked out, discussed and will be presented to CTAO Computing. They have to approve it.
* Atreyee asks if this includes if also the documentation should be hosted on gitlab, Daniel answers yes. 
* Atreyee asks what happens with user questions. Daniel answers that it is not clear at the moment. Bruno remarks that this is a good example of an issue that would be resolved by an IKC agreement covering support and future upgrades.
* In a discussion following a question Atreyee it is highlighted that there is a risk that the Gammapy version accepted, and required to be supported for 2 years, could end up out of step with the Gammapy LTS releases, requiring the support of two separate LTS releases! Another reason to create a IKC agreement covering support.
* Atreyee asked a further question I was not able to record

## VERITAS tutorial
* Samantha presents her draft tutorial showing VERITAS users how to use gammapy to make a real analysis
* Samantha found she needs to use a local star catalogue file, because queries to Simbad tended to crash; this filed would be hosted in gammapy-data.
* Still some questions regarding licensing left to be clarified, but Samantha is not expecting any problems and think that it will be resolved today.
* Regis remarks that it is anyway good practice to not have network lookups in the documentation because that regularly causes CI jobs to fail when the lookups timeout.
* Samantha reports she is working a bit on getting the VERITAS catalogue uploaded.
* Atreyee remarks that the star masking part of the tutorial could be moved into a separate function in gammapy utils.

## Bugs overview
* Fabio reports that the issues regarding linked parameters in sampled models have been understood and PRs resolving them have been merged.
* Atreyee volunteers to take a look at the open issues and make sure any bugs get assigned

## Documentation overview
* Kirsty reports that several PRs about documentation have been created, some of which has been merged.
* In the discussion about whether the tutorials should reordered, Regis stated he thinks the reorder should happen in time for version 2.0
* The decision for the new structure is postponed to next week
* Kirsty asks if the `check_setup()` part of every tutorial really _needs_ to be part of precisely every tutorial. After much discussion the conclusion is it is kept (the `check_setup` command automatically downloads the gammapy data if it is missing). It is further suggested that `gammapy info` could print a message along the lines of "congratulations, everything works".
* Kirsty highlighted #5922 where `inter_kwargs` are used for two different purposes, which makes it unclear how to document it.
* Atreyee shows the new tutorial on upper limits. It was concluded that it would be more appropriate to split the tutorial into two different tutorials.

## Project management
* Regis has created a [project on github for coordinating the work remaining on Gammapy 2.0](https://github.com/orgs/gammapy/projects/30/views/1). He highlights the need to start working on the changelog and the authorlist now.

## Activity report 

### PRs opened last week (less than 8 days ago): 
* [#5936](https://github.com/gammapy/gammapy/pull/5936) Update of the user guide documentation of `Modelling and Fitting` - Bruno Khélifi
* [#5934](https://github.com/gammapy/gammapy/pull/5934) Estimator documentation: update the n_sigma description - Bruno Khélifi
* [#5933](https://github.com/gammapy/gammapy/pull/5933) Add tutorial for upper limit computations - Atreyee Sinha
* [#5927](https://github.com/gammapy/gammapy/pull/5927) Add mask plot for spectral - Kirsty Feijen
* [#5925](https://github.com/gammapy/gammapy/pull/5925) Adapt docstring for `ReflectedRegionsFinder` - Kirsty Feijen
* [#5923](https://github.com/gammapy/gammapy/pull/5923) simple fix to problem with EventList printing - Tomas Bylund
* [#5922](https://github.com/gammapy/gammapy/pull/5922) Clean up of `irf/background.py` - Kirsty Feijen
* [#5921](https://github.com/gammapy/gammapy/pull/5921) Add `Notes` section to `HpxMap`,  `HpxNDMap` and `HpxGeom` - Kirsty Feijen
* [#5919](https://github.com/gammapy/gammapy/pull/5919) Add notes to `RegionGeom` and `RegionNDMap` - Kirsty Feijen
* [#5918](https://github.com/gammapy/gammapy/pull/5918) Adding VERITAS tutorial - Samantha Wong
* [#5916](https://github.com/gammapy/gammapy/pull/5916)  Fix link label display in parameters.to_table - Quentin Remy
* [#5914](https://github.com/gammapy/gammapy/pull/5914) Modify sampler to handle linked params in models - Fabio Acero
* [#5911](https://github.com/gammapy/gammapy/pull/5911) Introducing generic reproject_irf_on_geom functions using FoVFrame classes - Régis Terrier
* [#5910](https://github.com/gammapy/gammapy/pull/5910) Change argument name in ul - Kirsty Feijen

### PRs merged last week (less than 8 days ago): 
* [#5932](https://github.com/gammapy/gammapy/pull/5932) Remove SkyCoord.from_name - Kirsty Feijen
* [#5929](https://github.com/gammapy/gammapy/pull/5929) Add note on PR doc build access - Kirsty Feijen
* [#5926](https://github.com/gammapy/gammapy/pull/5926) Update sphinxext.py - Samantha Wong
* [#5924](https://github.com/gammapy/gammapy/pull/5924) Cleanup of psf functionalities - Kirsty Feijen
* [#5915](https://github.com/gammapy/gammapy/pull/5915) Fix parameters links after models copy - Quentin Remy
* [#5913](https://github.com/gammapy/gammapy/pull/5913) Add a function to retrieve free and unique parameters  - Fabio Acero
* [#5912](https://github.com/gammapy/gammapy/pull/5912) moving linkcheck from ci to a separate workflow - Hanna Stapel
* [#5905](https://github.com/gammapy/gammapy/pull/5905) Fix documentation of of the installation - Bruno Khélifi
* [#5904](https://github.com/gammapy/gammapy/pull/5904) Add requires_module decorator - Quentin Remy
* [#5896](https://github.com/gammapy/gammapy/pull/5896) Improve docstring of run function for `EnergyDependentMorphologyEstimator` - Kirsty Feijen
* [#5892](https://github.com/gammapy/gammapy/pull/5892) Improve docstring of run function for `ParameterEstimator` and `ParameterSensitivityEstimator` - Kirsty Feijen
* [#5889](https://github.com/gammapy/gammapy/pull/5889) Adapt intructions for static figures - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#5935](https://github.com/gammapy/gammapy/issues/5935) Confusion between predicted counts and background predicted counts - Juan 
* [#5931](https://github.com/gammapy/gammapy/issues/5931) Doc on gammapy.extern obsolete? - Bruno Khélifi
* [#5928](https://github.com/gammapy/gammapy/issues/5928) Bug in linear IRF Interpolation near boundary - Karl Kosack
* [#5920](https://github.com/gammapy/gammapy/issues/5920) EventList created with default constructor cannot be printed - Tomas Bylund
* [#5917](https://github.com/gammapy/gammapy/issues/5917) Remove deprecations for v2.1 - Régis Terrier

