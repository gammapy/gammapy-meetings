# Discussion notes model handling
Wednesday, Nov 25th 16h30


## What to do with the BackgroundModel?
1. Remove `BackgroundModel` and handle the case with `SkyModel(spatial_model=TemplateSpatialModel(), apply_irf={"edisp": False, "psf": False, "exposure": False})`
The problem is, that the latter case is possibly anyway, but untestedt and it's unclear whether it already works.
2. Rename to e.g. `DataModel`, but then the case `SkyModel(spatial_model=TemplateSpatialModel(), apply_irf={"edisp": False, "psf": False, "exposure": False})`m should probably be forbidden...


## Model bookeeping in `.to_image()`, `.to_spectrum_dataset()` etc.
- Right now we rely on `.npred_background()` in `MapDataset.to_image()`, `MapDataset.to_spectrum_dataset()` etc, This is non ideal, as it requires redefining and re-setting model parameters, e.g. https://github.com/gammapy/gammapy/blob/master/gammapy/estimators/flux.py#L164
- There are a few possible options:
  - Rely on `.background` instead and reset the model as a whole
  - Rely on `.background` and copy (?) over the model, while adpating the dataset name for the `FoVBackgroundModel`
  - Rely on `.npred_background` and reset the `FoVBackgroundModel`?
