
# Gammapy Developer Meeting

* Friday, December 16th, 2022 at 2 pm (CET)
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* Energy dependent LightCurveTemplateTemporalModel - Atreyee
  * A template from the SDC has been introduced in GAMMAPY_DATA [#31](https://github.com/gammapy/gammapy-data/pull/31)
  * The format is not very well defined. Gammapy API should not support this format. Proposed workaround: introduce utility function to
  convert to a proper `RegionMap` format, but don't make it public to allow removing it easily.
* Implement the _sample_coord_time_energy function in MapDatasetEventSampler [#4100](https://github.com/gammapy/gammapy/pull/4100) - Fabio 
  * This has been restructured and can be commented/reviewed already.
* Exposure correction for MapDataset.to_region_map_dataset() [#4256](https://github.com/gammapy/gammapy/pull/4256) - Luca
  * `MapDataset.to_region_map_dataset(region)` does not hangle properly regions not fully covered by the `mask_safe` or by the `dataset.geom`.
  The resulting exposure should be averaged using valid solid angle over the whole solid angle of the region. 
  * Several cases must be clarified and properly tested: partial/null coverage of the region wrt `dataset.geom`, partial coverage by `mask_safe`. 
  What should be the behaviour in the no-overlap case? Proposition, return dataset with `mask_safe=False`. What exception should `WcsNDMap.to_region()` raise?
* Add support for spatial model correction on background models [#4209](https://github.com/gammapy/gammapy/pull/4209) - Quentin
  * The PR adds a `spatial_model` argument to the `FoVBackgroundModel`. The `spatial_model` is evaluated on the bkg map geometry and multiplied to its values.
  * Main issue: typical `SpatialModel` return normalized quantities with 1/sr units. Currently only the `value` is kept. Silently keeping a `value` probably not a safe approach.
  * Proposition: for now, raise an exception if `spatial_model` returns a quantity not dimensionless. This would therefore mostly support used defined model for now.
* Map dataset on off in phase maker [#4252](https://github.com/gammapy/gammapy/pull/4252) - Maxime
  * Ready for review. 
  * Note: tutorial should be updated once PR is merged.   
* Add Observations clustering by IRFs quality [#4242](https://github.com/gammapy/gammapy/pull/4242) - Quentin 
  * Provides a method to group observations inside an `Observations` into groups with similar responses. Relies on scipy hierarchical clustering methods.
  * Note: clustering could be applied at various steps: directly on the `ObservationTable`, on the selected `Observations` or the final `Datasets`. Functionality should be suffienctly general: put clustering function in a dedicated `gammapy.utils` file. Could it take a `Table` input?
  * How to document: a tutorial/recipe? What usage to document?
* Add plot_rgb() function in gammapy.visualization [#4210](https://github.com/gammapy/gammapy/pull/4210) - Luca
  * Comments implemented. Ready for new review
* Add interp_scale to parameter scaling [#4218](https://github.com/gammapy/gammapy/pull/4218) - Quentin
  * Adds a scaling relying on the interpolation scheme. This breaks tests. Current CI fails prevent checking exact changes.
  * Make sure that default behaviour is unchanged. Check that this does not change minima values in general.  
* New API for FixedPointingInfo, decouple from GADF metadata [#4220](https://github.com/gammapy/gammapy/pull/4220) - Max
  * Ready for review.
  * CI fails preventing proper testing.
  
* CI fails with devdeps. 
  * This should be an allowed fail and should not block all the CI matrix
  * This might run also independently of PRs.  
