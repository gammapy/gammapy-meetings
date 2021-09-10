# Gammapy Developer Meeting

* Friday, September 10th, 2021 at 10 am
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* Short report by everyone, what they have worked on during the past week
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
  * Implement FluxProfileEstimator ([#3480](https://github.com/gammapy/gammapy/pull/3480), Axel)
  * Add a Datasets API notebook ([#3488](https://github.com/gammapy/gammapy/pull/3488), Atreyee)
  * Use FluxMaps as return type for ExcessMapEstimator ([#3491](https://github.com/gammapy/gammapy/pull/3491), Axel)
  * Pass empty dataset in Datasets.stack_reduce ([#3498](https://github.com/gammapy/gammapy/pull/3498), Atreyee)
  * Adapt caplog tests ([#3502](https://github.com/gammapy/gammapy/pull/3502), Atreyee)
  * Correct ParameterEstimator to return npred and npred_null when no dataset contributes ([#3504](https://github.com/gammapy/gammapy/pull/3504), Régis)
* Some open issues:
  * SafeMaskMaker throws an error when all bins are already safe [#3437](https://github.com/gammapy/gammapy/issues/3437)
  * Optional keywords required by gammapy [#3352](https://github.com/gammapy/gammapy/issues/3352)
  * energy_true not used in simulation tutorial [#3483](https://github.com/gammapy/gammapy/issues/3483)
  * Success flag and FluxMaps/FluxPoints [#3493](https://github.com/gammapy/gammapy/issues/3493)
  * MapDataset.downsample and MapDataset.resample_energy_axis have different behaviour [#3495](https://github.com/gammapy/gammapy/issues/3495)
  * Add a Datasets.fake method [#3496](https://github.com/gammapy/gammapy/issues/3496)
  * LightCurveEstimator fails if no dataset contribute in a time bin [#3501](https://github.com/gammapy/gammapy/issues/3501)
  * Error in TemplateSpatialModel serialisation [#3503](https://github.com/gammapy/gammapy/issues/3503)
  * Cryptic error message when FluxPointsEstimator reaches empty bin [#3505](https://github.com/gammapy/gammapy/issues/3505)


