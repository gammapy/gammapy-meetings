# Gammapy Developer Meeting

* Friday, October 29th, 2021 at 2 pm (CEST)
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* Short report by everyone, what they have worked on during the past week
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
  * Add sqrt_ts_threshold info to FluxPoints.to_table() ([#3561](https://github.com/gammapy/gammapy/pull/3561), Quentin)
  * Add the sampling of a variable source in the event sampling tutorial  ([#3557](https://github.com/gammapy/gammapy/pull/3557), Fabio)
  * Remove lru cache properties ([#3554](https://github.com/gammapy/gammapy/pull/3554), Régis)
  * Support iminuit v2.0 ([#3409](https://github.com/gammapy/gammapy/pull/3409), Axel)
  * Codespell: see ( ([#3559](https://github.com/gammapy/gammapy/pull/3559) & [#3548](https://github.com/gammapy/gammapy/pull/3548), Dimitri)
  * LGTM.com errors ([#3552](https://github.com/gammapy/gammapy/pull/3552), Dimitri)
  * Flake8   ([#3550](https://github.com/gammapy/gammapy/pull/3550), Dimitri)
* Status of benchmark/validation
  * Fix Fermi-LAT 3FHL validation ([#114](https://github.com/gammapy/gammapy-benchmarks/pull/114), Quentin)
  * Update hess validation ([#116](https://github.com/gammapy/gammapy-benchmarks/pull/116), Régis)
* New issues
  * OnOff datasets npred computation fails in case no counts is present [#3555](https://github.com/gammapy/gammapy/issues/3555)
  * The Event Sampler does not work with Alpha configuration IRFs [#3556](https://github.com/gammapy/gammapy/issues/3556)


* Older open PR 
  * Pass empty dataset in Datasets.stack_reduce ([#3498](https://github.com/gammapy/gammapy/pull/3498), Atreyee)
  * Use FluxMaps as return type for ExcessMapEstimator ([#3491](https://github.com/gammapy/gammapy/pull/3491), Axel)
  * Implement FluxProfileEstimator ([#3480](https://github.com/gammapy/gammapy/pull/3480), Axel)
  * Add multiple selection in ObservationTable.select_observations  ([#3431](https://github.com/gammapy/gammapy/pull/3431), Régis)
  * Add plot_at_energy option for Background3D ([#3388](https://github.com/gammapy/gammapy/pull/3388), Atreyee)
  * Add codemeta.json and CITATION.cff description metadata files ([#3344](https://github.com/gammapy/gammapy/pull/3344), Jose-Enrique)
* Open issues marked 0.19:
  * Optional keywords required by gammapy [#3352](https://github.com/gammapy/gammapy/issues/3352)
  * Optional key words required for dl3 data [#3119](https://github.com/gammapy/gammapy/issues/3119)
  * Unify mask handling in Dataset methods and Estimators [#3031](https://github.com/gammapy/gammapy/issues/3031)
  * Accessing observations through the high-level interface [#2515](https://github.com/gammapy/gammapy/issues/2515)
  * Improve read / write method API consistency [#2442](https://github.com/gammapy/gammapy/issues/2442)
  * Defaults for IRF axes [#2482](https://github.com/gammapy/gammapy/issues/2482)
  * Missing memory management of MapDataset [#3530](https://github.com/gammapy/gammapy/issues/3530)
  * Inconsistency between gammapy.utils.coordinates.fov and gamma.makers.utils [#3510](https://github.com/gammapy/gammapy/issues/3510)
 


