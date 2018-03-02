# Gammapy Telcon

* Friday, March 02, 2018 at 11 am
* CTA eZuce, password "gammapyregular".  The connection details are [here](ConnectionDetails.txt)

# Agenda

* Christoph: Gammapy updates
  * Gammapy 0.7 released two days ago
    * See http://docs.gammapy.org/0.7/ and http://docs.gammapy.org/0.7/changelog.html#gammapy-0p7-release
    * Everything should work, please try `pip install -U gammapy`, `conda install gammapy -c conda-forge`,
      or also Macports and try `gammapy info` e.g. `python -c 'import gammapy.detect'`.
      Windows conda packages are not there yet, coming soon, see [here](https://github.com/conda-forge/gammapy-feedstock/pull/1).
      If you find any issues or have questions, let us know!
    * Will be announced on mailing lists on Monday, unless issues are reported.
  * `gammapy.maps` is now used in Fermipy, i.e. Gammapy is a dependency of Fermipy now.
    * See https://github.com/fermiPy/fermipy/pull/192
    * Matthew and I plan to set up some automated testing for that today
  * Development activity in Gammapy is high now: https://github.com/gammapy/gammapy/pulse
    If you want to get involved, please join development via Github, or email Christoph & Regis.
  * Main development focus now: 3D maps and modeling, as well as improving / fixes for 1D spectra
    Many other developments going on, I think the splitting in small development teams (pulsars, binaries, 3D, 1D, ...)
    of one to a few people will work; they can do dedicated calls if needed, and report 5-min summaries in future
    bi-weekly Gammapy calls to give everyone a chance to see what is going on and join where they are interested.
  * From now on, we will do stable releases (0.8, 0.9) much more frequently,
    probably roughly one per month.
    This will help with usage of Gammapy in CTA and everywhere, if you can have stable version numbers
    when reporting results.
* Roberta: updates
  * Next Gammapy regular call will be Friday, March 16, at 11 am
    Will again focus on DC-1 checks, since we need to produce good results for CTA within the next month.
    Need first presentation of classical analysis results on HESS J1702-420 (Roberta) and TeV J1224+212 (Julien? Catherine?).
  * Very optimistically, we will have first 3D analysis results in two weeks;
    if not, then 3D analyses for the DC-1 checks
    will be the focus of the regular Gammapy call in four weeks, on March 30.
  * Next CTA meetings are Barcelona (April 16-20) and Orsay/Paris (May 14-18)
    We asked for a tutorial session for Gammapy.
  * Dedicated call on pulsar analysis with Gammapy & PINT soon.
    If you're interested, please contact Marion Spir-Jacob and fill your availability here now:
    https://framadate.org/w5mnzvPCIMKgBvOD
  * Next Gammapy coding sprint will be July 9-13.
    Location will be Heidelberg or Madrid.
    Please fill https://goo.gl/forms/J7lTzY0oN15lt2xf2 now if you want to join, we will decide soon.
* CTA DC-1 check analysis: Galactic center source (Giovanni De Cesare)
  * https://forge.in2p3.fr/projects/data-challenge-1-dc-1/wiki/DC-1_tool_assessment_-_GC
  * https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks/gc
  * TODO: link to slides
* CTA DC-1 check analysis: RX J1713 (Fabio Acero)
  * https://forge.in2p3.fr/projects/data-challenge-1-dc-1/wiki/DC-1_tool_assessment_-_RX_J1713
  * https://github.com/gammasky/cta-analyses/tree/master/dc-1-checks/rx_j1713
  * Slides?
* Gamma-ray binary analysis with Gammapy (Lab Saha)
  * Dedicated call soon. If you're interested, please fill https://doodle.com/poll/skay6hd94uvmqaz now.
  * TODO: add infos


## Reminder

* Gammapy docs: http://docs.gammapy.org
* Gammapy webpage: http://gammapy.org/
* Gammapy development: github.com/gammapy/gammapy

Next Gammapy meetings: http://gammapy.org/news.html

See http://gammapy.org/contact.html for contact info, e.g. mailing list
for announcements or questions, Slack for help or to join development, ...
