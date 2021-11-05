# Gammapy Developer Meeting

* Friday, November 5th, 2021 at 2 pm (CEST)
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* Short report by everyone, what they have worked on during the past week
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
  * Implement Map broadcasting ([#3573](https://github.com/gammapy/gammapy/pull/3570), Axel)
  * Remove link from parameter.to_table() ([#3570](https://github.com/gammapy/gammapy/pull/3573), Quentin)
  * Add test for event sampler using CTA IRF alpha configuration ([#3568](https://github.com/gammapy/gammapy/pull/3568), Fabio)
  * Use FluxMaps as return type for ExcessMapEstimator ([#3491](https://github.com/gammapy/gammapy/pull/3491), Axel)
  * Add plot_at_energy option for Background3D ([#3388](https://github.com/gammapy/gammapy/pull/3388), Atreyee)
  * Add multiple selection in ObservationTable.select_observations  ([#3431](https://github.com/gammapy/gammapy/pull/3431), Régis)
  * Correct FluxPointsEstimator to handle empty datasets slices ([#3543](https://github.com/gammapy/gammapy/pull/3543), Régis)
  * Addition of a success entry in FluxMap ([#3544](https://github.com/gammapy/gammapy/pull/3544), Bruno)
 
* Status of benchmark/validation
 
  * Update hess validation ([#116](https://github.com/gammapy/gammapy-benchmarks/pull/116), Régis)
* New issues
  * OnOff datasets npred computation fails in case no counts is present [#3555](https://github.com/gammapy/gammapy/issues/3555)
  * The Event Sampler does not work with Alpha configuration IRFs [#3556](https://github.com/gammapy/gammapy/issues/3556)

* Older open PR 
  * Pass empty dataset in Datasets.stack_reduce ([#3498](https://github.com/gammapy/gammapy/pull/3498), Atreyee)
  * Implement FluxProfileEstimator ([#3480](https://github.com/gammapy/gammapy/pull/3480), Axel)
  * Add codemeta.json and CITATION.cff description metadata files ([#3344](https://github.com/gammapy/gammapy/pull/3344), Jose-Enrique)
* Open issues marked 0.19:
  * https://github.com/gammapy/gammapy/issues/3505 
  * Optional keywords required by gammapy [#3352](https://github.com/gammapy/gammapy/issues/3352)
  * Optional key words required for dl3 data [#3119](https://github.com/gammapy/gammapy/issues/3119)
  * Unify mask handling in Dataset methods and Estimators [#3031](https://github.com/gammapy/gammapy/issues/3031)
  * Accessing observations through the high-level interface [#2515](https://github.com/gammapy/gammapy/issues/2515)
  * Improve read / write method API consistency [#2442](https://github.com/gammapy/gammapy/issues/2442)
  * Defaults for IRF axes [#2482](https://github.com/gammapy/gammapy/issues/2482)
  * Missing memory management of MapDataset [#3530](https://github.com/gammapy/gammapy/issues/3530)
  * Inconsistency between gammapy.utils.coordinates.fov and gamma.makers.utils [#3510](https://github.com/gammapy/gammapy/issues/3510)
 


