# Lightcurves

A first version of a new `LightCurveEstimator` was introduced shortly after Erlangen coding sprint. The general approach is described 
in [pig 11](https://docs.gammapy.org/dev/development/pigs/pig-011.html). 

The PIG has been withdrawn because it is already partly implemented and parts of the discussion are no longer relevant given the changes
introduced in the data reduction since Erlangen.

## Current status and proposed solutions

### Time information on datasets
- `LightCurveEstimator` relies on dataset time start and stop information stored as `meta`.
  * to have a cleaner, treatment we have introduced a `GTI` table on the various datasets
- `LightCurveEstimator` should rather deal with `GTI` 
  * see issue [#2547](https://github.com/gammapy/gammapy/issues/2547) 
  * see also related issue [#2545](https://github.com/gammapy/gammapy/issues/2547)

### Combining datasets for varying time bins
- `LightCurveEstimator` assumes on dataset per time bin and uses only the binning given by the list of dataset
  * a very common use case is to rebin groups of datasets on nightly, weekly, monthly etc basis
- I propose to pass a tuple of time bins to `LightCurveEstimator` and let him combine datasets together
  * We need to define the rule (e.g. `GTI` fully contained in the time bin, or `GTI` center within time bin)
  * This behaviour is then similar to `FluxPointsEstimator`
  * see issue [#2548](https://github.com/gammapy/gammapy/issues/2548) 

### Code duplication
- The current `LightCurveEstimator` suffers from heavy code duplication from `FluxPointsEstimator`. See the [code](https://docs.gammapy.org/dev/_modules/gammapy/time/lightcurve_estimator.html#LightCurveEstimator)
  * this is due to a very similar task with a slightly different logic
    * Both extract flux by fitting a scaled model of the source on the dataset
    * But `FluxPointsEstimator` uses the *same* datasets for all steps (i.e. all energy bins)
    * `LightCurveEstimator` uses different datasets for each time bin.
  * the `Fit` object has to be re-instantiated at each step in the loop
  * inheritance will not work
- I propose to simplify `LightCurveEstimator` heavily to rely on `FluxPointsEstimator`
  * For each time bin, create a `FluxPointsEstimator` for the current list of dataset with one single energy bin
  * Run flux point estimation and extract info from the table 
  
### Light curves with high level interface
  
We need to be able to run light curve from the HLI. This requires a number of additional features.
- Define a schema for time bins definition in yaml
  * a tstart - tstop, and bin duration? What format for `tstart` and `tstop`?
  * from a file containing a list of `Time`?
- Apply time selection on `Observations`

### Other issues - important but lower priority

- How do we deal with *sub-observations* statistics, in particular for ON-OFF datasets?
  * Usually, OFF can be extracted from the full observation
    * This implies to perform the `ReflectedRegionsBackgroundMaker` on an unfiltered `EventList`
    * This introduces bin-to-bin correlations
    * This makes `LightCurve` extraction more complex if the time bin size is different from the one used to filter the dataset
  * Can there be a grouping scheme to allow for shared background among datasets using `wstat`?  
