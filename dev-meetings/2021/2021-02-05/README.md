# Gammapy Developer Meeting

* Friday, Feb 5th, 2020 at 10 am
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* [Gammapy pulse from last week](https://github.com/gammapy/gammapy/pulse)
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
* Short report by everyone, what they have worked on during the past week 

* Handling of CompounRegion vs list of Region
* Handling of `RegionNDMap.get_spectrum()` or `PSFMap.to_region_nd_map()`
* Introduce `PSFKernel.plot()` or make `PSFKernel` directly a `Map`?
* Allow strings as Quantity?
    - Proposal: only allow strings where a scalar value is expected, when array input is supported, expect directly a Quantity