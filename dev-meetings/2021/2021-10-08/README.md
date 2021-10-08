# Gammapy Developer Meeting

* Friday, October 8st, 2021 at 10 am
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* Short report by everyone, what they have worked on during the past week
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
  * Minor change on IRF.data and .quantity setters ([#3538](https://github.com/gammapy/gammapy/pull/3538), Quentin)
  * Allow quanity for irf data in __init__ and setter,  ([#3537](https://github.com/gammapy/gammapy/pull/3537), Max)
  * Add TemplateNDSpectralModel ([#3535](https://github.com/gammapy/gammapy/pull/3535), Quentin)
  * Follow up on RadMax2d? ([#3515](https://github.com/gammapy/gammapy/pull/3515), Max, Cosimo)
* Status of benchmark/validation
  * https://github.com/gammapy/gammapy-benchmarks
* Some open issues:
  * Fit.run() should not return a dictionary of FitResult objects [#3542](https://github.com/gammapy/gammapy/issues/3542)
  * Reintroduce __init__ methods for IRFs [#3539](https://github.com/gammapy/gammapy/issues/3539)
  * Implement __eq__ for IRFs [#3534](https://github.com/gammapy/gammapy/issues/3534)
  * Support astropy quantities for Map.data [#3533](https://github.com/gammapy/gammapy/issues/3533)
  * Suppress astropy warnings? [#3532](https://github.com/gammapy/gammapy/issues/3532)
  * Missing memory management of MapDataset [#3530](https://github.com/gammapy/gammapy/issues/3530)
  * Inconsistency between gammapy.utils.coordinates.fov and gamma.makers.utils [#3510](https://github.com/gammapy/gammapy/issues/3510)
  * Cryptic error message when FluxPointsEstimator reaches empty bin [#3505](https://github.com/gammapy/gammapy/issues/3505)


