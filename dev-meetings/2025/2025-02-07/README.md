# Gammapy Developer Meeting 
 * Friday, February 07, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
# Agenda

## General points
- Register for [coding sprint](https://github.com/gammapy/gammapy-meetings/tree/master/coding-sprints/2025-04-LaLaguna)
- Plans for gammapy presentations in conferences this year

## Status of prototypes
Heres is a list of current draft/protoype PRs open. 

#### Maps
- [Support for array valued regions](https://github.com/gammapy/gammapy/pull/5420) Axel
  - Use case: energy dependent ON region size    
#### DL3 data handling
- [Draft example of a possible event read write with validation](https://github.com/gammapy/gammapy/pull/5313) Régis
- [introducing union support in ObservationFilter](https://github.com/gammapy/gammapy/pull/4616) Maxime
- [Potential modifications to support a future format](https://github.com/gammapy/gammapy/pull/5687) Quentin
#### Dataset 
- [Introduce LazyDatasets](https://github.com/gammapy/gammapy/pull/5450) Régis
  - Use case: Create a lazy `Datasets` object where datasets are created when needed. This can help e.g. creating lightcurves for very long time windows
- [1st implementation of the `EventDataset`](https://github.com/gammapy/gammapy/pull/5677) Maxime
#### Separation of Dataset and FitStatistic
- [Implement FitStatistics / Priors ideas.](https://github.com/gammapy/gammapy/pull/4237) Noah
- [Introduce Fit Statistic classes](https://github.com/gammapy/gammapy/pull/5688) Régis
- [Introducing FitStatistic: a different approach](https://github.com/gammapy/gammapy/pull/5696) Régis
#### Fit Statistic penalties, regularized FP, multiparameters priors 
- [Multi-dimension prior](https://github.com/gammapy/gammapy/pull/5468) Kirsty
- [A regularized flux points estimator](https://github.com/gammapy/gammapy/pull/5625) Régis
#### DL4 and IRFs structures
- [Implement PSFKernelMap](https://github.com/gammapy/gammapy/pull/3689) Laura
- [Improve DL4 irfs support in gammapy.makers](https://github.com/gammapy/gammapy/pull/5632) Quentin
#### DL5 data structures
- [Introduction of a new specialized class for lightcurves](https://github.com/gammapy/gammapy/pull/5174) Claudio
	- use case: Clarify usage of time dependent flux points with specific `LightCurve` container
	  ```python
	    lc = LightCurveEstimator().run(datasets)
	    print(f"Doubling time = {lc.doubling_time()}")
	    lc.write(outfile)	    
	  ```
#### Iterating on Fit/Estimators
- [ResolvedEstimator to fit models on datasets in bins defined by an axis.](https://github.com/gammapy/gammapy/pull/5444) Claudio
- [Introduction of the FitResults container class for lists of FitResult objects and axes](https://github.com/gammapy/gammapy/pull/5443) Claudio
  - use case: Repeat a modeling/fitting or estimator operation over an axis (e.g. time)
	```python
		fits_results = ResolvedEstimator(axis=time_axis).run(datasets)
	```
#### Improved access to FitResult
- [Visualisation function to plot stat profile](https://github.com/gammapy/gammapy/pull/5678) Maxime
  - use case: Simple visualization of some `Fit` results
	```python
	result = Fit().stat_profile(datasets, amplitude)
	result.profile.plot()
	```

## Report

### PRs opened last week (less than 8 days ago): 
* [#5696](https://github.com/gammapy/gammapy/pull/5696) [PROTOYPE] Introducing FitStatistic: a different approach - Régis Terrier
* [#5694](https://github.com/gammapy/gammapy/pull/5694) `e_peak` on `SuperExpCutoffPowerLaw4FGLDR3SpectralModel` - REGEARD Maxime
* [#5690](https://github.com/gammapy/gammapy/pull/5690) Fix and cleanup mask handling in TSMapEstimator - Quentin Remy
* [#5688](https://github.com/gammapy/gammapy/pull/5688) [PROTOTYPE] Introduce Fit Statistic classes - Régis Terrier
* [#5687](https://github.com/gammapy/gammapy/pull/5687) [PROTOTYPE] Potential modifications to support a future format  - Quentin Remy

### PRs merged last week (less than 8 days ago): 
* [#5689](https://github.com/gammapy/gammapy/pull/5689) Bump stefanzweifel/git-auto-commit-action from 5.0.1 to 5.1.0 - None
* [#5686](https://github.com/gammapy/gammapy/pull/5686) Correct time sampling issue #5685 - Régis Terrier
* [#5649](https://github.com/gammapy/gammapy/pull/5649) Add functions to create MapDataset from Fermi-LAT files - Quentin Remy

### issues opened last week (less than 8 days ago): 
* [#5695](https://github.com/gammapy/gammapy/issues/5695) TemplateSpatialModel serialisation - Atreyee Sinha
* [#5693](https://github.com/gammapy/gammapy/issues/5693) Request to Add Finke et al. (2022) EBL Model. - Bruno Arsioli
* [#5692](https://github.com/gammapy/gammapy/issues/5692) Add the functions `sigma_to_ts` and `ts_to_sigma` into the API documentation - Bruno Khélifi
* [#5691](https://github.com/gammapy/gammapy/issues/5691) Upper limit computation for cases with negative fluctuations in flux (or significance) - Juan 

 report created at 07/02/2025, 07:19:50
