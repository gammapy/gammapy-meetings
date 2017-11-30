# Gammapy Telcon

* Friday, December 1, 2017 at 11 am
* CTA eZuce, password "gammapyregular" -> anyone interested welcome to join!

# Agenda

* Report of the CC: Bruno
    * Organisation
    * Coding Sprint
        * February 5th, 14h to the 9th, 12h, 2018, and hosted in FACe, Paris.
        * Infos see [here](../2018-02-05).
* Gammapy update: Christoph
    * A few issues that came up from CTA DC-1 analyses have been fixed:
        * GH 1195 - Change IRF extrapolation behaviour
          (was triggered by AGN analysis issue by Bruno & Julien)
        * GH 1220 - Fix flux point computation for non-power-law models
          (was triggered by RXJ spectral analysis issue by Fabio)
        * GH 1204 - Consistently use mode='constant' in convolutions of RingBackgroundEstimator
          (was triggered by RXJ map anlaysis issue by Fabio)
        * GH 1210 - Fix min energy handling in SpectrumEnergyGrouper
          (was triggered by an AGN spectrum simulation issue by Julien)
        * GH 1213 - Memory leak for spectral analysis
          (was triggered by PeVatron spectral analysis issue by Cyril)
    * New features:
        * Integration of Jupyter notebooks with Sphinx docs
          http://docs.gammapy.org/en/latest/notebooks.html
        * Try Gammapy in the browser via Binder
          https://github.com/gammapy/gammapy-extra#binder
        * More work on documentation and webpage ongoing - will be shown in next call.
          Unfortunately http://docs.gammapy.org/en/latest currently isn't up to date because
          of an issue with the build on ReadTheDocs that I don't know how to fix.
        * GH 1211 - Add IRF write methods
          We need one or two people from the Gammapy side working on IRFs!
          The next steps are pretty straight-forward and can be done one small pull request at at time.
          Some tasks listed here: https://github.com/gammapy/gammapy/pull/1211#issuecomment-346834466
    * Next steps:
        * We're (again) almost ready for Gammapy v0.7 release.
            * A few more issues already reported and are being fixed:
              https://github.com/gammapy/gammapy/milestone/10
            * We have several pull requests open, but I think these are some we should try to get in ASAP:
                * Christoph: [GH 93](https://github.com/gammapy/gammapy-extra/pull/93) - Add conda env file for gammapy-tutorial; use it from Dockerfile
                * Bruno: [GH 1140](https://github.com/gammapy/gammapy/pull/1140) - Improve spectral point upper limit options
                * Julien: [GH 1214](https://github.com/gammapy/gammapy/pull/1214) - Add e_reco user binning for point-like simulation
        * There's many things small and large to do in Gammapy.
          If anyone has time to help, but you're not sure where to start, please get in contact
          and we'll team you up with a "mentor" that will help you make a contribution/pull request
          and get it reviewed / merged promptly!
* CTA DC1 analysis coordination : Roberta
    * See https://forge.in2p3.fr/projects/data-challenge-1-dc-1/wiki/Current_capabilities_and_limitations_of_the_analysis_tools
* Analysis of LS I 61 + 303 from the CTA DC1 : Lab
    * See https://github.com/gammasky/cta-analyses/tree/master/folded_light_curve
* Binder : Jose Enrique
    * See https://github.com/gammapy/gammapy-extra#binder
* AoB?

## Reminder

* Gammapy docs: https://gammapy.readthedocs.io/en/latest/
* Gammapy tutorials: https://nbviewer.jupyter.org/github/gammapy/gammapy-extra/blob/master/index.ipynb
* We use the Gammapy mailing list for announcements:
  https://groups.google.com/forum/#!forum/gammapy
  If you're interested but not signed up yet, do it now!
* You can also join the (non-public) Gammapy Slack if you want
  to chat about your questions / analysis or join Gammapy development.
