# Gammapy Developer Meeting 
 * Friday, August 08, 2025, at 2 pm (CET) 14:08-14:50
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

Attendees: Kirsty Feijen (KF), Katharina Egg (KE), Axel Donath (AD), Quentin Remy (QR), Leander Schlegel (LS)

# Agenda

QR: We have merged most of PR for 2.0, not much left besides documentation.

QR opens discussion about open PR:



#6055 "Change location and details of rad max tutorial":
-------------

KF reports: Added introduction like we did with last tutorials, but not clear what should stay in there, because a lot more than just a MAGIC tutorial. 
QR: No problem, if full analysis in MAGIC tutorial (VERITAS has full analysis too).
KF: Basically just added introduction part to tutorial.
QR: "How-to" for this maybe not needed? KF: "How-to" is really big already, if we add too much, people will maybe not look anymore.

QR: Other PR only infrastructure.

#6010 Changelog 2.0
----------
AD: Resolved most things already, maybe for bugfixes we should tell exactly, what details are, so people can see if they are affected or not.
Left some inline comments, summary reads good now, that was most important part.

#5939 "Update Citation.cff for v2.0"
------
QR: We can do this after the branching.


#6048 "Update minimal dependencies for 2.0"
------
QR: Maybe we could test if it works with latest version of Matplotlib and ??? now, if it does, it is okay.



QR opens discussion of the remaining issues:

#6020 "Move MAGIC tutorial to Data Exploration"
-----
KF: What is analysis 2?
QR: It is the "Low-level API"-tutorial.
KF: If we leave high-level interface, we should also leave low-level interface and come back for 2.1.
QR: Do it after v2.0, Maybe we could add a link at the end, showing other tutorials that use HESS-data, would be a way to show, how to do the full analysis. QR writes comment in issue.

#5775 "Add conditions for multiple selections in DataStore.obs_table"
-----
QR: Should miss just simple thing, can be fixed easily. 

#5737 "Adapt SensitivityEstimator to Cowan approach"
------
AD: I can briefly comment, was only put in place like prelim. safety-measure, as not much experience at the time. One would (???) need to change to different criteria, that e.g. E-axis is aligned to certain degree, should be solvable.
QR: I checked alignment of E-axis already, but fluxpoint in certain bin with different meaning of ??? does not make sense.
AD agrees. We were rather cautious with this. Could be loosened a bit.
QR: We could have option "strict"=True/False to allow this, or not. I would postpone this for 2.1.


#5422 "Consider other types of sample interpolation"
------
QR: Could we postpone this also, AD?
AD: Yes, is absolutely no priority, I explored this about 1.5 years ago, noticed it could make eventsampling more efficient, but so far, no one complained about speed. You can always take fine binning and it is okay.
Idea is, you can change from nearest neighbour to linear interpolation and can then use wider bin.
QR: Postponed to 2.1.

#5713 "Adapt reoptimize option for FluxPointsEstimator?"
------
QR: Is for the user to determine what is relevant for the analysis. Postponed for 2.1.


#5282 "Simplify the Sensitivity Estimator Notebook"
------
QR: Not clear if this is only rel. to documentation or if this requires more in the code as well? We can wait for AS to discuss it.

#5344 "Task list for Sensitivity Estimation"
------
QR: Can postpone it, as related to other PR. ???


#4563: "Improve error traceback for DatasetsMaker"
------
QR: We can postpone this one as well. 
Not sure we can keep job in multiprocessing, if other job failed, do you know, if there is option for this, AD? (???)
AD: We could use ray for multiprocessing? QR: Yes both, ray and multiprocessing, ray optionally, and it does not repeat error message. Has more options if something failed, than multiprocessing, but have not looked into it.


#4780 "Support multiple time intervals in gammapy.data.ObservationFilter"
------
QR: Is a large feature, postponed to 2.1.

#4511 "Introducing logics in ObservationFilter"
-------
QR: Postponed to 2.1, as related to obs-filtering.

#4451 "Improve error message when loading using the wrong class"
--------
QR: Will require something to validate format of FITS-file. Postponed to 2.1.
AD: There is a universal solution for both. Typically we should be very forgiving on read. We can improve on case-by-case basis. Typically we first check on filename-ending, if it is valid fileformat for class. Then go step by step and check, if actual filecontent is suitable. I commented already on it. We can only do it on case-by-case basis.


#5349 "Always apply GTI filtering on EventList"
-----
QR: We discussed with BK and ???. Ensure, that no events outside of GTI. I think, issue can stay open, but likely we dont need to do it. Checking that all events in GTI, every time, is not efficient, better beforehand.

#5002 "Use CREF<N> keyword to determine axis order of GADF IRF components"
------
QR: Postponed to 2.1, as there are many small variances of GADF, we have to be sure it works for all of them.


QR: That is all for 2.0, we probably do branch on Monday and finish little things that are remaining. AOB?:
------

- LS: Question regarding PR #5954 "Separate internal Eventlist data model from gadf format": Should keyword arguments, like e.g. format, be passed through from read()@EventList to read()@EventListReader?
QR: Yes should be done, even if no problem for now, as only one format supported.
LS agrees to do PR for it.


- KF: #6063 "Should it be observation or observations in ObservationsEventsSampler.run".
 I opened this issue to clarify. QR: Yes, "s" is missing. KF: Ok, should be "observations", just wanted to check, I will change docstring. 
QR: Is there anything else regarding documentation?
KF: Not in the moment, there would be more time if people come across something.

- AD: Keep some time next week for testing, after we do branch.








Original list:

### Open PRs for v2.0

https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A2.0

### Open issues for v2.0

https://github.com/gammapy/gammapy/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A2.0

### PRs opened last week (less than 8 days ago): 
* [#6067](https://github.com/gammapy/gammapy/pull/6067) Docstring formatting part 3 - Kirsty Feijen
* [#6066](https://github.com/gammapy/gammapy/pull/6066) Fix recompute_ul for masked arrays - Quentin Remy
* [#6061](https://github.com/gammapy/gammapy/pull/6061) Workflow to check the building of wheels nightly - Daniel Morcuende
* [#6056](https://github.com/gammapy/gammapy/pull/6056) Add `make_counts_off_rad_max` to `__all__` - Arnau Aguasca-Cabot
* [#6055](https://github.com/gammapy/gammapy/pull/6055) Change location and details of rad max tutorial - Kirsty Feijen
* [#6048](https://github.com/gammapy/gammapy/pull/6048) Update minimal dependencies for v2.0 - Régis Terrier
* [#6047](https://github.com/gammapy/gammapy/pull/6047) Bump actions/first-interaction from 1 to 2 - None

### PRs merged last week (less than 8 days ago): 
* [#6068](https://github.com/gammapy/gammapy/pull/6068) Add descriptions to peek of dataset functions - Kirsty Feijen
* [#6065](https://github.com/gammapy/gammapy/pull/6065) Docstring formatting part 2 - Kirsty Feijen
* [#6064](https://github.com/gammapy/gammapy/pull/6064) Docstring formatting - Kirsty Feijen
* [#6062](https://github.com/gammapy/gammapy/pull/6062) Doc fails - Kirsty Feijen
* [#6058](https://github.com/gammapy/gammapy/pull/6058) Adapt the docstring for PSF containment - Kirsty Feijen
* [#6057](https://github.com/gammapy/gammapy/pull/6057) Cleanup variable name in `estimate_min_e2dnde`  - Arnau Aguasca-Cabot
* [#6054](https://github.com/gammapy/gammapy/pull/6054) Correct errors in docs build - Kirsty Feijen
* [#6053](https://github.com/gammapy/gammapy/pull/6053) Add mask for PointSkyRegion in geom.region_mask - Atreyee Sinha
* [#6051](https://github.com/gammapy/gammapy/pull/6051) Cleanup VERITAS peek plot - Atreyee Sinha
* [#6050](https://github.com/gammapy/gammapy/pull/6050) Update the Dl4/DL5 doc page about `sherpa` - Bruno Khélifi
* [#6049](https://github.com/gammapy/gammapy/pull/6049) Add info message on geom mismatch - Atreyee Sinha
* [#6046](https://github.com/gammapy/gammapy/pull/6046) Revert "Merge pull request #5992 from bkhelifi/obs_peek" - Quentin Remy
* [#6045](https://github.com/gammapy/gammapy/pull/6045) Revert #5992 - Axel Donath
* [#6044](https://github.com/gammapy/gammapy/pull/6044) Mention NEP29 guideline for python and numpy support in dev docs - Daniel Morcuende
* [#6043](https://github.com/gammapy/gammapy/pull/6043) Fix docstrings - Kirsty Feijen
* [#6039](https://github.com/gammapy/gammapy/pull/6039) Adapt CTAO tutorial with xmltodict - Kirsty Feijen
* [#6038](https://github.com/gammapy/gammapy/pull/6038) Vectorized error evaluation of flux uncertainties based on samples - Quentin Remy
* [#6031](https://github.com/gammapy/gammapy/pull/6031) Exposing `AnalysisConfig` better - Kirsty Feijen
* [#6029](https://github.com/gammapy/gammapy/pull/6029) Standardized implementation prior_stat_sum - Quentin Remy
* [#6005](https://github.com/gammapy/gammapy/pull/6005) Fixing `FluxPoints` docstring - None
* [#6002](https://github.com/gammapy/gammapy/pull/6002) Update of plot functions for the colour bar - Bruno Khélifi
* [#5982](https://github.com/gammapy/gammapy/pull/5982) Add class instance caching for WcsGeom - Quentin Remy
* [#5954](https://github.com/gammapy/gammapy/pull/5954) Separate internal Eventlist data model from gadf format - Régis Terrier
* [#5933](https://github.com/gammapy/gammapy/pull/5933) Add tutorial for computing parameter upper limits - Atreyee Sinha

### issues opened last week (less than 8 days ago): 
* [#6063](https://github.com/gammapy/gammapy/issues/6063) Should it be `observation` or `observations` in `ObservationsEventsSampler.run` - Kirsty Feijen
* [#6060](https://github.com/gammapy/gammapy/issues/6060) Use pixi and uv for packaging, installation and CI setup - Daniel Morcuende
* [#6059](https://github.com/gammapy/gammapy/issues/6059) Cleanup linting/formatting settings usings flake8, isort, black, pydocstyle - Daniel Morcuende
* [#6042](https://github.com/gammapy/gammapy/issues/6042) Implement scheduled nightly build of wheels - Daniel Morcuende
* [#6041](https://github.com/gammapy/gammapy/issues/6041) Evaluate the use of CircleCI - Daniel Morcuende

 report created at 08/08/2025, 07:30:47
