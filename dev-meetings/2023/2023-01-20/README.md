
# Gammapy Developer Meeting

* Friday, January 20th, 2023 at 2 pm (CET)
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

#### New open PRs
- Remove safe mask in background stacking [#4275](https://github.com/gammapy/gammapy/pull/4275) - Atreyee
  - Simple fix. Already discussed in issue #4207
- Add energy support for a template temporal model [#4272](https://github.com/gammapy/gammapy/pull/4272) - Atreyee
  - After discussion, the best solution is to have a registry system for various formats for the read methods of `Model`. For now, this branch can be used to convert all SDC models.  
- Allow to set psf max radius in evaluator [#4276](https://github.com/gammapy/gammapy/pull/4276) - Quentin
- Fix datasets io with RecoPSFMap (draft) [#4277](https://github.com/gammapy/gammapy/pull/4277) - Quentin
  - A better apporach would be to create a factory method on `PSFMap` 
- Fix bkgs spectral model io [#4278](https://github.com/gammapy/gammapy/pull/4278) - Quentin
- Add an HowTo for the fit non-convergence [#4268](https://github.com/gammapy/gammapy/pull/4268) - Bruno

#### Open PRs
* Implement the _sample_coord_time_energy function in MapDatasetEventSampler [#4100](https://github.com/gammapy/gammapy/pull/4100) - Fabio 
  * CI issue with codestyle  
* New API for FixedPointingInfo, decouple from GADF metadata [#4220](https://github.com/gammapy/gammapy/pull/4220) - Max
* Add plot_rgb() function in gammapy.visualization [#4210](https://github.com/gammapy/gammapy/pull/4210) - Luca

#### Merged PRs
- Use linebreaks in passenv list in tox.ini [#4269](https://github.com/gammapy/gammapy/pull/4269) - Axel
  - Needs to be adapted to v1.0.x as well
  - Change must be included in gammapy-docs actions
- Deprecate load_cta_irfs, replace usage with load_irf_dict_from_file [#4264](https://github.com/gammapy/gammapy/pull/4264) - Max
- Small docs changes [#4274](https://github.com/gammapy/gammapy/pull/4274), [#4270](https://github.com/gammapy/gammapy/pull/4270), [#4273](https://github.com/gammapy/gammapy/pull/4273)



* [Open PRs](https://github.com/gammapy/gammapy/pulls)

* [Open issues](https://github.com/gammapy/gammapy/issues)
