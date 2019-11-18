#Lightcurves

A first version of a new `LightCurveEstimator` was introduced shortly after Erlangen coding sprint. The general approach is described 
in [pig 11](https://docs.gammapy.org/dev/development/pigs/pig-011.html). 

## Current status and proposed solutions

### `LightCurveEstimator` relies on dataset time start and stop information stored as `meta`.
  * to have a cleaner, treatment we have introduced a `GTI` table on the various datasets
  * `LightCurveEstimator` should rather deal with `GTI` :see issue [#2547](https://github.com/gammapy/gammapy/issues/2547) 
  * see also issue [#2545](https://github.com/gammapy/gammapy/issues/2547)

### `LightCurveEstimator` assumes on dataset per time bin and uses only the binning given by the list of dataset
  * a very common use case is to rebin groups of datasets on nightly, weekly, monthly etc basis
  * I propose to pass a tuple of time bins to `LightCurveEstimator` and let him combine datasets together
    * We need to define the rule (e.g. `GTI` fully contained in the time bin, or `GTI` center within time bin)
    * This behaviour is then similar to `FluxPointsEstimator`
  * see issue [#2548](https://github.com/gammapy/gammapy/issues/2548) 

### The current `LightCurveEstimator` suffers from heavy code duplication from `FluxPointsEstimator`.
  * this is due to a very similar task with a slightly different logic
    * Both extract flux by fitting a scaled model of the source on the dataset
    * But `FluxPointsEstimator` uses the *same* datasets for all steps (i.e. all energy bins)
    * `LightCurveEstimator` uses different datasets for each time bin.
  * the `Fit` object has to be re-instantiated at each step in the loop
