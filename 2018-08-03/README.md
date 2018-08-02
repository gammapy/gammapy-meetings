# Gammapy Telcon

* Friday, August 3, 2018 at 10 am
* CTA eZuce, no password.  The connection details are [here](ezuce.txt)

# Agenda

## Christoph: Introduction

* Again, a ton of activity in the past week.
  See merged pull requests: https://github.com/gammapy/gammapy/pulse
* SkyImage and SkyCube removed from Gammapy master
  https://groups.google.com/forum/#!topic/gammapy/OEMpw-zyDaI
* Read and try out the new tutorials to learn about the new maps and modeling:
  http://docs.gammapy.org/dev/tutorials.html#notebooks
* Now shaking out the bugs and adding missing features.
  Still not ready for v0.8, see https://github.com/gammapy/gammapy/milestone/11
  Devs: try to help, so that this can go out next week.
* MapMaker and corresponding functions better improved.
  Background maps fixed just now - please re-run!
  See http://docs.gammapy.org/dev/notebooks/analysis_3d.html
  and http://docs.gammapy.org/dev/api/gammapy.cube.MapMaker.html
* Next steps: debug PSF, support 2 Gaussian models, support DiffuseMapCube,
  default parameter step init so that `set_parameter_errors` gets superfluous,
  evaluate models on bounding boxes for great profit (time is money!),
  continue bug fixes and cleanup ...

## Sabina: simulating and fitting small sources

* Using Gammapy to evaluate CTA PSFs

## 3D analyses from CTA DC-1

* See https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks
* Roberta: J1702
* Roberta: Cas A
* Bruno: AGN

## Gammapy developments

* See [open pull requests](https://github.com/gammapy/gammapy/pulls)
* See [v0.8 milestone](https://github.com/gammapy/gammapy/milestone/11)
* What is needed for v0.8, what can be deferred to v0.9?

Specific things to discuss:

* Volunteer to code DiffuseSkyCube today? [GH 1629](https://github.com/gammapy/gammapy/issues/1629)
* Volunteer to write spectrum obs grouping tutorial? [GH 1577](https://github.com/gammapy/gammapy/issues/1577)
* No progress yet on background models, see [GH 1516](https://github.com/gammapy/gammapy/issues/1516)
