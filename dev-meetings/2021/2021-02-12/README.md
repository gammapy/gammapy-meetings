# Gammapy Developer Meeting

* Friday, Feb 12h, 2020 at 10 am
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)
# Agenda

* [Gammapy pulse from last week](https://github.com/gammapy/gammapy/pulse)
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
* Short report by everyone, what they have worked on during the past week 

* Norm bounds handling https://github.com/gammapy/gammapy/pull/3234 (Quentin)
* "GADF" format for RegionNDMap (https://github.com/gammapy/gammapy/pull/3231, https://github.com/open-gamma-ray-astro/gamma-astro-data-formats/pull/170) (Axel)
* Extended source tutorial https://github.com/gammapy/gammapy/pull/3230 (Laura)
* Model renormalisation https://github.com/gammapy/gammapy/pull/3229 (Quentin)
* More thoughts by Axel:
     - Implement model integration / oversampling
     - Implement models consistently in TAN projection? And rely on "analytical" (scipy.special) integrals?
     - Keep `SphericalGaussianSpatialModel` and `SphericalDiskSpatialModel`?
     - The use case of fitting small sources (extension close to bin size) is more frequent, then fitting > 1 deg sources?
     
 * Anything else? 