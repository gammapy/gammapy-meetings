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
  * [Rio CTA collaboration meeting  M](https://cta.cta-observatory.org/indico/sessionDisplay.py?sessionId=40&confId=1218#20170515)
    * See Stefan's presentation on timeline and communication of news and issues
      ( https://forge.in2p3.fr/projects/data-challenge-1-dc-1 )
* First large set of 1DC test files available since two days ago (Tuesday, May 30):
  * Go to https://owncloud.cta-observatory.org , log in with your CTA username / password (same as CTA sharepoint), and download tarballs from the `1dc.south` folder. It is possible to use wget.
  * This is not the final 1DC data release,
    that will probably happen sometime in June.
    I don't know if there will be simulated data from the north array or not,
    and if the small issue with EDISP ROOT -> FITS converter and
    off-axis response have been resolved or not. I'll send some comments
    on the files and these questions to Stefan / Jürgen tomorrow.
  * Very few docs (or only outdated docs) at this point concerning data and sky models. This will come in the coming days / weeks. Best overview are the slides from Stefan and Jürgen from Rio.
  * I had a very quick look yesterday:
    * PSF model changed (from Gauss -> King profile).
      Trying to read and plot the new PSF I get interpolation errors with Gammapy, probably because of how we handle missing PSF info in low energy bins (below the safe energy threshold).
      Have to look / fix the `gammapy.irf.PSFKing` class.
      If someone wants to do this task or help, let me know.
    * Still have to create and upload the observation index file, to make
      data access convenient with Gammapy. I'll do this today or tomorrow latest.
  * So what should you do?
    * if you want to help debugging IRFs and code: download the `1dc.south` files now,
      try to run analyses using Gammapy or ctools and report or even fix issues.
    * if you want to do science analyses: wait a bit until mid or late June
      until issues with the files and codes have been ironed out and docs written, i.e. the final 1DC data release as well as the upcoming Gammapy 0.7 release.
    * if you're mostly interested in science analysis and don't want to help
    with debugging IRFs and code, wait for the official 1DC release, probably in mid or end of June!

## Christoph: Gammapy update

* tbd

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
