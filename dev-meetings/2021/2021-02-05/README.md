# Gammapy Developer Meeting

* Friday, Feb 5th, 2020 at 10 am
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* [Gammapy pulse from last week](https://github.com/gammapy/gammapy/pulse)
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
* Short report by everyone, what they have worked on during the past week 

* Modelling tutorial https://github.com/gammapy/gammapy/pull/3216 (Atreyee)
* Update on the `FluxMap` container https://github.com/gammapy/gammapy/pull/3075 (Régis)
* Shell2SpatialModel https://github.com/gammapy/gammapy/pull/3222 (Quentin)
* Handling of empty bins in background: https://github.com/gammapy/gammapy/pull/3219, see https://github.com/gammapy/gammapy/issues/2432 as well (Quentin, Axel)
* Handling of `CompoundRegion` vs list of `Region` (Axel)
* Handling of `RegionNDMap.get_spectrum()` or `PSFMap.to_region_nd_map()` (Axel)
* Introduce `PSFKernel.plot()` or make `PSFKernel` directly a `Map`?
* Allow strings as Quantity? (Axel)
    - Proposal: only allow strings where a scalar value is expected, when array input is supported, expect directly a Quantity
