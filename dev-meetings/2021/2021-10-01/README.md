# Gammapy Developer Meeting

* Friday, October 1st, 2021 at 10 am
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* Short report by everyone, what they have worked on during the past week
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
  * Correct map evaluator to avoid memory overload ([#3529](https://github.com/gammapy/gammapy/pull/3529), Régis)
  * Change tutorials to use Models.to_parameters_table() method ([#3528](https://github.com/gammapy/gammapy/pull/3528), Régis)
  * Add sample_time to temporal models  ([#3523](https://github.com/gammapy/gammapy/pull/3523), Fabio)
  * Create an Observation object from a single file ([#3514](https://github.com/gammapy/gammapy/pull/3514), Cosimo)
* Some open issues:
  * Suppress astropy warnings? [#3532](https://github.com/gammapy/gammapy/issues/3532)
  * Missing memory management of MapDataset [#3530](https://github.com/gammapy/gammapy/issues/3530)
  * Inconsistency between gammapy.utils.coordinates.fov and gamma.makers.utils [#3510](https://github.com/gammapy/gammapy/issues/3510)
  * Success flag and FluxMaps/FluxPoints [#3493](https://github.com/gammapy/gammapy/issues/3493)
  * MapDataset.downsample and MapDataset.resample_energy_axis have different behaviour [#3495](https://github.com/gammapy/gammapy/issues/3495)
  * Cryptic error message when FluxPointsEstimator reaches empty bin [#3505](https://github.com/gammapy/gammapy/issues/3505)


