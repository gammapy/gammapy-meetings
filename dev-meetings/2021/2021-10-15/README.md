# Gammapy Developer Meeting

* Friday, October 15th, 2021 at 2:30 pm
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* Short report by everyone, what they have worked on during the past week
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
  * Correct bug in integrate_spectrum ([#3545](https://github.com/gammapy/gammapy/pull/3545), Régis)
  * Correct FluxPointsEstimator to handle empty datasets slices  ([#3543](https://github.com/gammapy/gammapy/pull/3543), Régis)
  * Addition of a success entry in FluxMap ([#3544](https://github.com/gammapy/gammapy/pull/3544), Bruno)
  * Include CovarianceResults into OptimizeResults  ([#3547](https://github.com/gammapy/gammapy/pull/3547), Régis) 
* Status of benchmark/validation
  * https://github.com/gammapy/gammapy-benchmarks
* Some open issues:
  * Memory leak with MapDataset.evaluators [#3546](https://github.com/gammapy/gammapy/issues/3546)
  * Reintroduce __init__ methods for IRFs [#3539](https://github.com/gammapy/gammapy/issues/3539)
  * Implement __eq__ for IRFs [#3534](https://github.com/gammapy/gammapy/issues/3534)
  * Support astropy quantities for Map.data [#3533](https://github.com/gammapy/gammapy/issues/3533)
  * Missing memory management of MapDataset [#3530](https://github.com/gammapy/gammapy/issues/3530)
  * Inconsistency between gammapy.utils.coordinates.fov and gamma.makers.utils [#3510](https://github.com/gammapy/gammapy/issues/3510)
 


