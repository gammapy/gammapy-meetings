# Discussion topics and coding projects:

## General
- Finish open PRs: https://github.com/gammapy/gammapy/pulls 
- Prototype for a real time analysis?
- Move from Travis-CI to github actions
- Issues: https://github.com/gammapy/gammapy/issues?q=is%3Aopen+is%3Aissue+milestone%3Av0.19



## API
- Merge `SpectrumDataset` and `MapDataset`?
- Make `Fit` class configurable, so that users can choose backends for flux points estimation.
- Remove support for `EDispKernel` in `MapDataset`
- Remove `BackgroundModel` and support the use case via `TemplateSpatialModel`?
- Model book-keeping in `MapDataset.to_image()`, `MapDataset.cutout()` `MapDataset.to_spectrum_dataset()` etc. methods. Should we rely on `.npred_background()`?
- PIG 22

## Validation and testing
- Update and finish validation of DR1-DL3, CTA 1DC, 3FHL etc.
- Check status

## Documenation
- Move API tutorials to the corresponding sub-packages and build "in place"
- Simplify data download: remove index files and use a single tar file instead?
- Simplify notebook download: remove index files and use a single tar file at the top of the tutorials page instead?
- Resolve content duplication between tutorials / RST 
- Write RST pages for new sub-packages (Axel, Régis)
- Add documentation on `RegionGeom` and `RegionNDMap` (Axel)
- Further improve IRF documentation
- User contributed notebooks?


## Features
- Model management functionality, such as `Models.select()` and `Parameters.freeze(type="spatial")`, lets 
- Unified flux points handling (see PIG 22)
- Implement `EDispEnergyScaleModel`?

### Feedback from HAWC 
- Better support for HPX maps
- Assymteric PSF
- IRFs in zenith bins

## Feedback from CTA GPS
- TS estimation using an `Estimator` or documentation (see above)?
- Remove `BackgroundModel` and support the use case via `TemplateSpatialModel` (see above)?
- Keep model in `MapDataset.cutout()` (see above)
 

## Bugs and Fixes
- TBD

