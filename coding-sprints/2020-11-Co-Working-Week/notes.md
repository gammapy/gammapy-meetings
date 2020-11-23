# Discussion topics and coding projects:

## General
- Finish open PRs: https://github.com/gammapy/gammapy/pulls 
- Prototype for a real time analysis?
- Move from Travis-CI to github actions
- Issues: https://github.com/gammapy/gammapy/issues?q=is%3Aopen+is%3Aissue+milestone%3Av0.19


## Discussion and code projects

### Real time analysis
- Implement prototype 

### Model handling (discussion required)
- Remove `BackgroundModel` and support the use case via `TemplateSpatialModel`?
- Model book-keeping in `MapDataset.to_image()`, `MapDataset.cutout()` `MapDataset.to_spectrum_dataset()` etc. methods. Should we rely on `.npred_background()`?
- Model management functionality, such as `Models.select()` and `Parameters.freeze(type="spatial")`
- Implement `EDispEnergyScaleModel`?

### Dataset unification (discussion required)
- Merge `SpectrumDataset` and `MapDataset`?
- Remove support for `EDispKernel` in `MapDataset`
- Check behaviour if model is outside FoV (inrerpolation of IRFs etc.)

### Estimator API / result object (discussion required)
- Finish PIG 22
- Make `Fit` class configurable, so that users can choose backends for flux points estimation.

### Various
- Better support for HPX maps
- Assymetric PSF
- IRFs in zenith bins 

## Documenation
- Move API tutorials to the corresponding sub-packages and build "in place"
- Simplify data download: remove index files and use a single tar file instead?
- Simplify notebook download: remove index files and use a single tar file at the top of the tutorials page instead?
- Resolve content duplication between tutorials / RST 
- Write RST pages for new sub-packages
- Add documentation on `RegionGeom` and `RegionNDMap`
- Further improve IRF documentation
- TS estimation using an `Estimator` or documentation
- User contributed notebooks?

## Validation and testing
- Check status in general
- Update and finish validation of DR1-DL3, CTA 1DC, 3FHL etc.
- Improve benchmarks, extend for missing ones (maybe one for RTA)
