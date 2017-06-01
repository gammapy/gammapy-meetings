# Gammapy Telcon

* Thursday, June 1, 2017 at 11 am
* CTA eZuce, password "dcgammapy" -> anyone interested welcome to join!

# Agenda

* Christoph (Roberta not available today): CTA 1DC update
* Christoph: Gammapy update
* Bruno: next steps
* All: questions and discussion

## Reminder

* Gammapy docs: https://gammapy.readthedocs.io/en/latest/
* Gammapy tutorials: https://nbviewer.jupyter.org/github/gammapy/gammapy-extra/blob/master/index.ipynb
* We use the Gammapy mailing list for announcements:
  https://groups.google.com/forum/#!forum/gammapy
  If you're interested but not signed up yet, do it now!
* You can also join the (non-public) Gammapy Slack if you want
  to chat about your questions / analysis or join Gammapy development.

## Christoph: CTA 1DC update

* [CTA 1DC wiki page](https://forge.in2p3.fr/projects/data-challenge-1-dc-1/wiki)
  (supposed to be the central place with information, but hasn't been updated
  in the past months, not very useful at this point)
* Instead, for intro / overview on 1DC, see the slides from the Milano and Rio CTA meetings:
  * [Milano CTA PHYS WG meeting March 6](https://cta.cta-observatory.org/indico/sessionDisplay.py?sessionId=1&confId=1300#20170306)
  * [Rio CTA collaboration meeting  May 15](https://cta.cta-observatory.org/indico/sessionDisplay.py?sessionId=40&confId=1218#20170515)
    * See Stefan's presentation on timeline.
      * He suggests to sign up for "news" and report "issues" for 1DC here:
        https://forge.in2p3.fr/projects/data-challenge-1-dc-1
    * See Jürgen's presentation for data content / distribution of 1DC.
* First large set of 1DC test files available since two days ago (Tuesday, May 30):
  * Go to https://owncloud.cta-observatory.org , log in with your CTA username / password (same as CTA sharepoint), and download tarballs from the `1dc.south` folder. It is possible to use wget.
  * This is not the final 1DC data release,
    that will probably happen sometime in June.
    * I don't know if there will be simulated data from the north array or not,
    and if the small issue with EDISP ROOT -> FITS converter and
    off-axis response have been resolved or not. I'll send some comments
    on the files and these questions to Stefan / Jürgen tomorrow.
  * Very few docs (or only outdated docs) at this point concerning data and sky models. This will come in the coming days / weeks. Best overview are the slides from Stefan and Jürgen from Rio.
  * I had a very quick look yesterday:
    * PSF model changed (from Gauss -> King profile).
      * Trying to read and plot the new PSF I get interpolation errors with Gammapy, probably because of how we handle missing PSF info in low energy bins (below the safe energy threshold).
      Have to look / fix the `gammapy.irf.PSFKing` class.
      If someone wants to do this task or help, let me know.
    * Still have to create and upload the observation index file, to make
      data access convenient with Gammapy. I'll do this today or tomorrow latest.
  * So what should you do?
    * if you want to help debugging IRFs and code: download the `1dc.south` files now,
      try to run analyses using Gammapy or ctools and report or even fix issues.
    * if you want to do science analyses: wait a bit until mid or late June
      until issues with the files and codes have been ironed out and docs written, i.e. the final 1DC data release as well as the upcoming Gammapy 0.7 release.

## Christoph: Gammapy update

* Gammapy 0.6 release May 9 (see [announcement](https://groups.google.com/forum/#!topic/gammapy/Q-SyHYpERPM))
  * Lot's of new features, see ["What's new"](http://docs.gammapy.org/en/latest/changelog.html#april-28-2017)
* Now started working on Gammapy 0.7:
  * Release will be soon, in mid or end of June.
  * Main goal is to support CTA 1DC analysis
  * But of course any fixes & features welcome,
    e.g. Matthew is working on the HEALPix maps
    and I'm working on the `gamma-cat` code.
  * Roberta is working on a CTA example doing 3D simulation / fitting
  * Bruno and Julien are working on sensitivity computation
  * Yesterday I updated the [CTA data analysis](https://nbviewer.jupyter.org/github/gammapy/gammapy-extra/blob/master/notebooks/cta_data_analysis.ipynb) example notebook
  (minor fixes, and added automatic testing to make sure it keeps working).
  A while ago, Axel added a section showing how to do source detection
  using peak finding with TS maps.
* Unfortunately, the documentation build is broken at the moment,
  so the online docs don't reflect the changes from the past two weeks.
  * In principle Readthedocs very nice, a free cloud docs build / hosting service, where the docs auto-update on any change in `master`.
    But there have been problems with the conda install before and now again.
    Supposed to be fixed next week.
    If not, I'll move the docs build to a server at MPIK.
* Next high-priority steps for the coming ~ week:
  * Prepare obs index files for `1dc.south`
  * Look at CTA King profile PSF issue and fix `gammapy.irf.KingPSF` if needed.
  * Run some analyses with new `1dc.south` and see if we can
    recover morphology / spectral parameters of some bright sources correctly
  * Prepare more examples / docs how to do CTA analysis and simulation.
    to have something ready at the time of the 1DC release.
* Large development efforts for the coming ~ month:
  * Finish developments in `gammapy.maps` for WCS-based and HEALPix-based maps.
  * Finish the change to Gammapy modeling to use `gammapy.utils.modeling`
    also for spatial and 3D models.
  * Support 3D background model class
  * Support energy-dependent on region for 1D spectral analysis
    and point-like response (used by MAGIC & partly CTA)
  * ... many other things ... lot's of work and developments needed -> help welcome!
  * Write a short Gammapy paper!

## Bruno: next steps

* Next Gammapy telcon in early July?
  * Everyone: please consider presenting something!
    If you have managed to get results, or are stuck with issues
    with Gammapy analyses, we want to hear from you!
  * Doesn't have to be focused on CTA-1DC, all Gammapy-related topics are welcome.
* A Gammapy f2f meeting in summer or fall?
  * Or use the ASWG bootcamp meeting (DESY Zeuthen, June 20-23) to talk?
  * There might be a CTA PHYS f2f meeting with a CTA-DC session in HD
    or Erlangen in September, that could also be a chance to talk and
    work together.
