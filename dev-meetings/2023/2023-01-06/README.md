
# Gammapy Developer Meeting

* Friday, January 06th, 2023 at 2 pm (CET)
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

### Updates from last [meeting](../../2022/2022-12-16/README.md)
#### CI status:
  * devdeps is now an allowed fail and no longer blocks all the CI matrix. See merged PR [#4262](https://github.com/gammapy/gammapy/pull/4262). action versions have been upgraded as well.
  * python3.9 with all deps on Ubuntu still fails for no clear reason. See e.g. this [fail](https://github.com/gammapy/gammapy/actions/runs/3823297732/jobs/6504317044)
  * CI fails with scipy 1.10, for now enforce scipy<1.10 [#4265](https://github.com/gammapy/gammapy/issues/4265)
    * There is already a fix in preparation in scipy (see e.g. scipy PR [#17717](https://github.com/scipy/scipy/pull/17717) and [17726](https://github.com/scipy/scipy/pull/17726) 
#### Merged PRs:
  * Map dataset on off in phase maker [#4252](https://github.com/gammapy/gammapy/pull/4252) - Maxime
#### Remaining reviews to be performed:
  * New API for FixedPointingInfo, decouple from GADF metadata [#4220](https://github.com/gammapy/gammapy/pull/4220) - Max
    * Needs reviews urgently 
  * Implement the _sample_coord_time_energy function in MapDatasetEventSampler [#4100](https://github.com/gammapy/gammapy/pull/4100) - Fabio 
  * Add plot_rgb() function in gammapy.visualization [#4210](https://github.com/gammapy/gammapy/pull/4210) - Luca
#### Updates from other PRs
#### New PRs and on-going work:
  * Patching CVE-2007-4559 [#4267](https://github.com/gammapy/gammapy/pull/4267)
    * This PR solves a security issue posed by `tar.extractall` that can be used to run malicious code. In Gammapy, this is used only in `gammapy.download` which only relies on a trusted source, since it retrieves the gammapy.data tarball from the github repo. This therefore does not seem to be a real concern. 
   * Follow-up on PR [#4245](https://github.com/gammapy/gammapy/pull/4245) which added an evaluate method for CompoundSpectralModel (Lucas)
     * issue: Parameter order is different in models `__init__` and `evaluate` methods. Can this be solved?
     * possible approach: changing the order is a possibility since most called are done by name. Evaluate the impact of such a change.
   * Preparing a PR for GTI internal data model
     * Use directly a table with `Time` columns or keep a reference `Time` and MET `Quantity` objects? There might be performance bottleneck when performing time filtering and `GTI.union`.
     * proposed approach: try to stick with `Time` columns and check how serious bottleneck is. Keeping track of a reference time might not be a necessity.  

### Next bugfix release. 
* Need to fix a date for the milestone (end January?)
* [Open issues with 1.0.1 milestones](https://github.com/gammapy/gammapy/issues?q=is%3Aopen+is%3Aissue+milestone%3Av1.0.1)
  * Incorrect serialisation of light curves time axis [#4257](https://github.com/gammapy/gammapy/issues/4257)
  * PointSpatialModel: min and max of lon_0 [#4255](https://github.com/gammapy/gammapy/issues/4255)
  * MapDataset.create() sets mask to False by default [#4207](https://github.com/gammapy/gammapy/issues/4207)
 
