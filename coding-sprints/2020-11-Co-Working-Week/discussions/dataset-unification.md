# Discussion notes: dataset unification 
Tuesday 25th, 10h00

## Overview

Main API question: fully unify `SpectrumDataset` and `MapDataset` and handle 1D anlysis with `MapDataset` and `RegionGeom`?
- See PR https://github.com/gammapy/gammapy/pull/3131
- See also https://github.com/gammapy/gammapy/pull/3131#issuecomment-731741951

Pros:
- Fully unified API, just one API to learn, however the difference in API between `SpectrumDataset` and `MapDataset` will be small anyway...
- Possibility to handle PSF and morphology containment correction
- Reduced maintenance effort


Cons:
- Risk of confusing users, with to much (complex) functionality? Like "why can I define a spatial model for a spectral analysis", why is there a PSF defined for a spectral analysis?
- Higher effort for documentation, need to explain users well how it works.

There are some other consequences:
- Forbid e.g. using a `MapDataset` and `RegionGeom` with `TSMapEstimator` or `ExcessMapEstimator`
- In general we need to support `RegionGeom` for IRF maps on `MapDataset` anyway, to handle spatially non-varying IRFs
