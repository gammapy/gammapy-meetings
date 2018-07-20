# Gammapy Telcon

* Friday, July, 2018 at 10 am
* CTA eZuce, no password.  The connection details are [here](ezuce.txt)

# Agenda

## Gammapy status and plans

* Gammapy very slow progress in the past year, now development very active. See [pulse in last month](https://github.com/gammapy/gammapy/pulse/monthly).
* Gammapy coding sprint last week at MPIK. See [webpage](https://github.com/gammapy/gammapy-meetings/tree/master/2018-07-09).
* To try to keep the momentum (at least partially), we'll continue with weekly Gammapy calls Fridays 10 am.
* Note that CTA is also very active now. We need a clean and powerful Gammapy package, v1.0 and a paper this fall.
* Concerning cleanup / deprecations:
  * We've been accumulating code for years; see [here](https://www.openhub.net/p/gammapy/analyses/latest/languages_summary); the result was a very messy, unfriendly code base. Dozens of classes that basically aren't needed at all or are duplicated.
  * Bad for users, but also I think one of the reasons development was glacially slow in the past year.
  * We have to clean up and improve. So last week I deleted 10,000 lines of code / tests / docs, the parts that I thought were uncontroversial.
  * Today we should discuss what changes go in v0.8 (hopefully in ~ 1 week) and which we postpone to v0.9 or even later.
  * Note that v0.7 will always be as-is, you can use that. But of course, if you need to upgrade to v0.8 for an analysis, we want to support you. Either keep something or help you rewrite your script to the new code.
    * What to do about the stuff in [gammapy.scripts](http://docs.gammapy.org/0.7/scripts/index.html#module-gammapy.scripts)?
    All added there with "not sure how to do this properly, not much time now, let's just put it there".
    It was always clear that this has to be rewritten / relocated / merged with existing code.
    Removal of `CTASpectrumObservation` and `CTAIrf` ([GH 1517](https://github.com/gammapy/gammapy/pull/1517)) for v0.8 or v.9?
    Should we move `SensitivityEstimator` and `SpectrumAnalysisIACT` to gammapy.spectrum?
    * What about the SkyImage / SkyCube transition? A lot of the rewrite using gammapy.maps is done!
    The main remaining part are the IACT and Fermi-LAT image estimators.
    And the rewrite of the ring background estimation using maps is blocked by the presence of the IACTBasicImageEstimator.
    My suggestion would be to remove the FermiLATBasicImageEstimator now (see [GH 1545](https://github.com/gammapy/gammapy/issues/1545)). Then we update high-level docs and do v0.8 in ~a week.
    Finishing the transition, full removal of SkyImage / SkyCube / IACTBasicImageEstimator will then be in v0.9.
    Note that rewriting script from SkyImage / Skycube to use gammapy.maps is not hard. See [intro_maps.ipynb](https://github.com/gammapy/gammapy-extra/blob/master/notebooks/intro_maps.ipynb). We're happy to help!
* Let's now move on to first 3D and DC1 analyses, and then to the dev hangout and open PRs and issues and the v0.8 milestone.

## CTA DC-1 Analyses

We will start with a status report on CTA DC-1 check analyses.

Please try to have results ready: put scripts or notebooks that write
results in machine-readable format, stored in version control, summarised in README.
In the presentation, please be quick (10 min max) and focus on open issues and questions.

* Roberta (tbc): [CTA DC1 - J1702](https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks/hess_j1702)
* Christoph: [CTA DC1 - AGN](https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks/agn_j1224)
* Fabio: [CTA DC1 - RX J1713](https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks/rx_j1713)
* maybe (tbd): [CTA DC1 - Galactic center](https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks/gc)
* maybe (tbd): [CTA DC1 - Cas A](https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks/cas_a)

## Developer hangout

* https://github.com/gammapy/gammapy/milestone/11


After that, we'll do the weekly Gammapy developer chat (this time on eZuce).

The goal is to produce a good Gammapy v0.8 release ASAP that gives good results for the the CTA DC1 analyses.

* Johannes (tbc): status modeling
* Regis (tbd): status maps
* Christoph: Gammapy v0.8 release (see [Github milestone](https://github.com/gammapy/gammapy/milestone/11))
