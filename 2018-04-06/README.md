# Gammapy Telcon

* Friday, April 6, 2018 at 11 am
* CTA eZuce, password "gammapyregular".  The connection details are [here](ConnectionDetails.txt)

# Agenda
* Software (CD)
  * Regis is working on 3D analysis with `gammapy.maps`.
    So far only [gammapy.cube.fill_map_counts](http://docs.gammapy.org/dev/api/gammapy.cube.fill_map_counts.html)
    is available, we didn't get very far yet.
  * One reason is that Gammapy development still isn't very active, but another is
    that we're still spending some time to improve `gammapy.maps`
    (see e.g. [GH 1357](https://github.com/gammapy/gammapy/pull/1357) or [GH 1346](https://github.com/gammapy/gammapy/pull/1346)).
    But even more time to improve and fix the "classical analysis" that we have
    (many issues and small pull requests in the past weeks), and finding / fixing issues simply takes time.
  * 3D analysis remains our main focus of development, with Regis implementing the "prepare" step,
    and Johannes and I will work on the "fit" step intensely next week.
  * Contributing to Gammapy development is of course possible, there are many small tasks.
    If you have time, please stay on after the call to talk to Regis and me, or email us.
  * E.g. some developments we need ASAP that are fairly well-defined and can be done in one pull request
    are adding a unit attribute to maps (see [GH 1206](https://github.com/gammapy/gammapy/issues/1206)),
    or map slicing / cutout (see [GH 1329](https://github.com/gammapy/gammapy/issues/1329));
    those are the main missing features for `gammapy.maps` for new 3D analysis code.
    Another development that's fairly well-defined and limited in scope is to add
    a first version of PSF kernel classes, as described in [GH 1048](https://github.com/gammapy/gammapy/issues/1048) and also in [GH 1216](https://github.com/gammapy/gammapy/issues/1216). These are just some examples, there are many other tasks, see https://github.com/gammapy/gammapy/issues and https://github.com/gammapy/gammapy/pulls .
  * One point I'd like to discuss today (probably best at the end, in a smaller group)
    is where exactly PSF and EDISP normalisation should be applied.
    See [GH 1359](https://github.com/gammapy/gammapy/pull/1359) for some comments on where
    to normalise the PSF.
* DC1 analysis:
  * TeV J1224+212: BK and Catherine Boisson [link](https://github.com/gammasky/cta-analyses/blob/master/agn_light_curve/TeV_J1224p212.ipynb)
* Planned presentations
* Next regular call: April 27th

## Reminder

* Gammapy docs: http://docs.gammapy.org
* Gammapy webpage: http://gammapy.org/
* Gammapy development: github.com/gammapy/gammapy

Next Gammapy meetings: http://gammapy.org/news.html

See http://gammapy.org/contact.html for contact info, e.g. mailing list
for announcements or questions, Slack for help or to join development, ...
