# Discussion notes model handling
Wednesday, Nov 25th 16h30


#### What to do with the BackgroundModel?
1. Remove `BackgroundModel` an handled the case with `SkyModel(spatial_model=TemplateSpatialModel(), apply_irf={"edisp": False, "psf": False, "exposure": False})`
The problem is, that the latter case is possibly anyway, but untestedt and it's unclear whether it already works.
2. Rename to e.g. `DataModel`, but then the case `SkyModel(spatial_model=TemplateSpatialModel(), apply_irf={"edisp": False, "psf": False, "exposure": False})`m should probably be forbidden...
