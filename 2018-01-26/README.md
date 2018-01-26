# Gammapy Telcon

* Friday, Junuary 26, 2018 at 11 am
* CTA eZuce, password "gammapyregular".  The connection details are [here](ConnectionDetails.txt)

# Agenda

* CC composition: BK
* Gammapy development update: CD
  * Little activity at the moment. See https://github.com/gammapy/gammapy/pulse/monthly
  * Will do Gammapy 0.7 release some time next week.
    * Only one simple to fix, but important issue that I'd consider a blocker for the release:
      https://github.com/gammapy/gammapy/issues/1266
    * Would also like to spend a few hours to check and clean up install docs and notebooks
* HESS FITS test data release update: CD
  * If you're in HESS and interested in the public FITS test data release,
    please review the release notes document and check the files.
    We'll have a final call today at 1 pm.
    See [here](https://hess-confluence.desy.de/confluence/display/HESS/HESS+FITS+data+-+Meetings#HESSFITSdata-Meetings-2018-01-26)
    for agenda, connection details, latest version of release notes document and files.
    Will circulate in HESS collaboration next week. Either on Monday, or if someone has time to review
    and give feedback in the next days, then incorporate that and circulate mid next week.
  * Once it's out, or even before, we should update many Gammapy tutorials, and also tests, to use the
    good new version of the files instead of buggy files from years ago like we do now.
  * Some more work ongoing with fixes / cleanup for the data format specs, see
    [GH 103](https://github.com/open-gamma-ray-astro/gamma-astro-data-formats/pull/103) and
    [GH 102](https://github.com/open-gamma-ray-astro/gamma-astro-data-formats/issues/102).
* CTA 1DC: CD
  * Best place to get started is http://gammapy.org/cta.html,
    has links to CTA 1DC wiki page and our Gammapy-internal repo.
  * New AGN dataset simulated at 0.5 deg wobble offset.
    See https://forge.in2p3.fr/projects/data-challenge-1-dc-1/wiki/Getting_data (instructions and checksums there are updated)
    * `agn.wobble.tar.gz` (untars into the existing `agn` folder, i.e. replaces those files)
    * You also should update `index.tar.gz` at the same time!
  * No activity / progress on the [cross-check analyses](https://forge.in2p3.fr/projects/data-challenge-1-dc-1/wiki/Current_capabilities_and_limitations_of_the_analysis_tools#Test-casestargets)
    Please analyse 1DC data (for now: classical analysis: 1d spectrum & 2d image) with Gammapy and report what works and doesn't work!
* Coding Sprint: CD, BK
  * Please visit this link: https://github.com/gammapy/gammapy-meetings/tree/master/2018-02-05
* Meetings dates: BK
  * Next regular meeting: the 16th of February
  * We'd like to make good progress with Gammapy development in 2018,
    and do a second coding sprint before the summer break, in June or July,
    probably at MPIK Heidelberg.
    If you might be interested, please fill this form: https://goo.gl/forms/493orc8xrkg1QQYK2

## Reminder

* Gammapy docs: http://docs.gammapy.org
* Gammapy webpage: http://gammapy.org/
* Gammapy development: https://github.com/gammapy/gammapy

Next Gammapy meetings: http://gammapy.org/news.html

See http://gammapy.org/contact.html for contact info, e.g. mailing list
for announcements or questions, Slack for help or to join development, ...
