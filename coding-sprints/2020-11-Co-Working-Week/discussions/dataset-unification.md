# Discussion notes: dataset unification 
Tuesday 25th, 10h00

## Overview

Main API question: fully unify `SpectrumDataset` and `MapDataset` and handle 1D anlysis with `MapDataset` and `RegionGeom`?
- See PR https://github.com/gammapy/gammapy/pull/3131
- See also https://github.com/gammapy/gammapy/pull/3131#issuecomment-731741951

Pros:
- Fully unified API, just one API to learn, however the difference in API between `SpectrumDataset` and `MapDataset` will be small anyway...
- Possibility to handle PSF and morphology containment correction "on the fly" if a PSF an spatial model are defined
- Reduced maintenance effort
- One would likely remove the `SpectrumDatasetMaker` as well...


Cons:
- Risk of confusing users, with to much (complex) functionality? Like "why can I define a spatial model for a spectral analysis", why is there a PSF defined for a spectral analysis?
- Higher effort for documentation, need to explain users well how it works.

There are some other consequences:
- Forbid e.g. using a `MapDataset` and `RegionGeom` with `TSMapEstimator` or `ExcessMapEstimator`
- In general we need to support `RegionGeom` for IRF maps on `MapDataset` anyway, to handle spatially non-varying IRFs

## Notes
- There is specific functionality for 1D and it will always remain:
  - Serialisation, e.g. OGIP format
  - Plotting, like `.plot_fit()`
  - 
  
- Moving code to a common base class is "safe" and can be done without much extra effort. 
- Need documentation on the `RegionGeom`!


Unrelated: 
- How to handle kwargs forwarding? Régis doesn't like the `kwargs_spatial` and `kwargs_spectral` -> 2nd discussion session on Thursday...
- Implement more general grouping scheme?
