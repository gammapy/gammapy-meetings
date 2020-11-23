# Discussion topics and coding projects (no particular order...):

## General
- Finish open PRs: https://github.com/gammapy/gammapy/pulls 
- Prototype for a real time analysis?
- Decide on final API changes
- Move from Travis-CI to github actions

##API
- Merge `SpectrumDataset` and `MapDataset`?
- Make `Fit` class configurable, so that users can choose backends for flux points estimation.
- Remove support for `EDispKernel` in `MapDataset`
- Remove `BackgroundModel` and support the use case via `TemplateSpatialModel`?
- Model book-keeping in `MapDataset.to_image()`, `MapDataset.to_spectrum_dataset()` etc. methods. Should we rely on `.npred_background()`? 

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

## Bugs and Fixes
- TBD

