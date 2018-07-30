# Gammapy Telcon

* Friday, July 27, 2018 at 10 am
* CTA eZuce, no password.  The connection details are [here](ezuce.txt)

# Agenda

**Contributions welcome! If you'd like to present of discuss something, add it here or email Christoph**

## Gammapy status and plans

* See [pulse in last week](https://github.com/gammapy/gammapy/pulse/weekly).
* Again a lot of progress in the past week, but still a lot of work before we can release v0.8.
  The goal is to release v0.8 Friday next week, if you can help, please take one of the open issues on that milestone.
* The plan is to finish the SkyImage / SkyCube -> gammapy.maps transition.
  Remove SkyImage, SkyImageList and SkyCube on Monday, before v0.8.
  Most of the work is done, some remains for today & Monday.
* Discuss: code removed for background modeling [GH 1515](https://github.com/gammapy/gammapy/pull/1515), [GH 1513](https://github.com/gammapy/gammapy/pull/1513)
  Note that apart from general cleanup, another reason why I removed it was because it was using the obs grouping classes, which I also would like to remove now (see [GH 1575](https://github.com/gammapy/gammapy/pull/1575)).
  Plan is to bring background model building functionality back ([GH 1516](https://github.com/gammapy/gammapy/pull/1516)). OK to do this for v0.9, or should it be a priority for v0.8, i.e. be done next week?
* Discuss: new data / observation classes, see [GH 1546](https://github.com/gammapy/gammapy/pull/1546)
* Discuss [open pull requests](https://github.com/gammapy/gammapy/pulls)
* Discuss [v0.8 milestone](https://github.com/gammapy/gammapy/milestone/11)


## First 3D analyses from CTA DC-1

* Intro: see [analysis_3d.ipynb](https://github.com/gammapy/gammapy-extra/blob/master/notebooks/analysis_3d.ipynb) and [simulate_3d.ipynb](https://github.com/gammapy/gammapy-extra/blob/master/notebooks/simulate_3d.ipynb)
* Fabio: update on [CTA DC1 - RX J1713](https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks/rx_j1713)
* Status of https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks
  * Ideally each analysis has make.py to produce results in machine-readable format,
  in addition to plots and summary in the README.

## Developer hangout

* See [v0.8 milestone](https://github.com/gammapy/gammapy/milestone/11)
* See [open pull requests](https://github.com/gammapy/gammapy/pulls)
* Distribute developments for next week.
