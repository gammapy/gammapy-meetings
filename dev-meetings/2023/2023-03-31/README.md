
# Gammapy Developer Meeting

* Friday, March 31th, 2023 at 2 pm (CET)
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

### Preparation of v1.1 release
* What has been achieved so far
  * [37 Merged PRs](https://github.com/gammapy/gammapy/pulls?q=is%3Aclosed+is%3Apr+milestone%3A1.1)
  * [11 closed PRs](https://github.com/gammapy/gammapy/issues?q=is%3Aissue+is%3Aclosed+milestone%3A1.1)
* [Open issues](https://github.com/gammapy/gammapy/issues?page=1&q=is%3Aopen+is%3Aissue+milestone%3A1.1)
  * 39 remaining open issues. 17 are not assigned.
  * Need to determine what needs to go in and what can be postponed.
* [Open PRs](https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A1.1)
  * 35 open PRs (including 15 old PRs, pre v1.0)
* What minimal required features for the release?
* What calendar:
  * Initially planned on April 7th.
  * Aim for the week April 17th-21st (before the CTA meeting)?
  
### Open PRs
#### Bug
* Obs filter live time [#4394](https://github.com/gammapy/gammapy/pull/4394) - Maxime
  * Does it work for more complex phase selection?
* Check of the time system information of the DataStore [#4399](https://github.com/gammapy/gammapy/pull/4399) - Bruno 
  * Should it go in v1.0.x?
  * Some mix-up with files.
* Fix example code of ring background maker [#4440](https://github.com/gammapy/gammapy/pull/4440) - Atreyee  

#### Feature
##### Data
* Allow to load observations with only IRFs defined [#4280](https://github.com/gammapy/gammapy/pull/4280) - Quentin
* Use datastore maker in Observation.read [#4426](https://github.com/gammapy/gammapy/pull/4426) - Quentin
 * Draft. Connection with PR above
##### Makers
* Adding rad max cut in PhaseBackgroundMaker [#4352](https://github.com/gammapy/gammapy/pull/4352) - Maxime
  * Approved. CI fails -> Rebase from main?
##### Datasets
* Add a livetime map on dataset [#4407](https://github.com/gammapy/gammapy/pull/4407) - Atreyee
##### Models 
* LightCurveTemplateModel serialisation [#4412](https://github.com/gammapy/gammapy/pull/4412) - Atreyee
* Update the evaluate_timevar_source function in MapDatasetEventSampler [#4418](https://github.com/gammapy/gammapy/pull/4418) - Fabio
##### Maps
* adding from_stack and append to LabelMapAxis [#4417](https://github.com/gammapy/gammapy/pull/4417) - Maxime
##### Estimators
* Serialise gti table to flux points object [#4432](https://github.com/gammapy/gammapy/pull/4432) - Atreyee
* Add a function to combine excess maps [#4433](https://github.com/gammapy/gammapy/pull/4433) - Quentin 
  * Still draft
* Expose more methods in ExcessMapEstimator [#4414](https://github.com/gammapy/gammapy/pull/4414) - Quentin
* Addition of an ExtensionEstimator [#4419](https://github.com/gammapy/gammapy/pull/4419) - Régis
  * Still draft
##### Plotting
* Add .to_string('latex_inline') to axis y/xlabel with powers [#4428](https://github.com/gammapy/gammapy/pull/4428) - Arnau
* Add a function that plot the npred_signal of models of a dataset [#4409](https://github.com/gammapy/gammapy/pull/4409) - Maxime
* plot function for 1D distribution of map data [#4408](https://github.com/gammapy/gammapy/pull/4408) - Maxime
* Add the possibility to plot in MJD the light curves [#4395](https://github.com/gammapy/gammapy/pull/4395) - Bruno
#### Performance
* Support for parallel evaluation in FluxPointsEstimator [#4402](https://github.com/gammapy/gammapy/pull/4402) - Quentin
* Support for parallel evaluation in LightCurveEstimator [#4404](https://github.com/gammapy/gammapy/pull/4404) - Quentin
* Add configuration and helper function to run multiprocessing or ray  [#4406](https://github.com/gammapy/gammapy/pull/4406) - Quentin
##### Infrastructure
* Add profilers to dev environment [#4398](https://github.com/gammapy/gammapy/pull/4398) - Quentin
##### Documentation
* Pulsar analysis tutorial [#4369](https://github.com/gammapy/gammapy/pull/4369) - Maxime & Alvaro

