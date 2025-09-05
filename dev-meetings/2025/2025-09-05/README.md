# Gammapy Developer Meeting 
 * Friday, September 05, 2025, at 2 pm (CET)  14:05-15:??
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
 
Attendees: Aritra Gupta (AG), Atreyee Sinha (AS), Katharina Egg (KE), Hanna (H), Claudio Galelli (CG), Leander Schlegel (LS), Daniel Morcuende (DM), Kirsty Feijen (KF), Mattias Fuessling (MF), Régis Terrier (RT)
 
# Agenda

AS opens the meeting. Today many can not participate. After 2.0 release, it has been circulated, no complains regarding installation so far, which is good news.

There have been some PRs, one related to towncrier. DM, do you want to comment on yours and Kirsty's infrastructure changes? 

#6121
-------------------------
DM reports: Quality gate. All software projects within CTAO use SonarQube. similar to what codacy does, the quality gate that is currently integrated with gammapy. It should be good to have also Gammapy using SonarQube for consistency with the rest of the projects. Action item: we have a first test with SonarQube, see how it goes, Daniel can help with this. Then compare the quality report with what Codacy reports. CTAO recently purchased a license for SonarQube, developer version, with has some more features. Follow-up discussion: https://github.com/gammapy/gammapy/issues/6121
AS: We have to use the free version? DM: We can use the purchased version, that CTAO recently got. For SAT hosted in GitLab it is done already, but the question is whether to also trigger the check of Gammapy itself.
AS: Is there any conflict?
DM: Have not tested it yet, would not expect any problem with it.
AS: We have to fix, what are the checks. 
DM: For the twoncrier, KF started doing it [in this PR](https://github.com/gammapy/gammapy/pull/6130). Idea is to not do all the changelog manually before each release, but we have a system that for every PR with significant changes, you already describe what is a change and the towncrier integrates it automatically in a changelog. RT later on this: if we want towncrier to make the changelog for 2.1 we should have it at the begining of the development cycle, see discussion below.
AS: Very nice as preparing changelog is significant work usually. Do we have to be more carefully about what we write when doing a PR now?
DM: Yes, every PR now needs a Changelog-section.

AS: Then we merged your PR on Jupytext. 

Workflow "Run tutorials with Jupytext"
----------------------
DM: Runs perfect, takes 20 minutes. Workflow "Run tutorials with Jupytext".
AS: To get this to work we had to remove interactive plotting?
DM: Yes in one case, the others did not gave any problems. The problem was, that the selection of the Jupyter was waiting for a user interaction.
Looking at the FermiLAT tutorial in the gammapy-doc.

Issue #6060
------------------------------------
DM: Related to uv, pixi. First thing would be to move all the content of setup.cfg to pyproject. With this you can use out of the box already the pixi, uv, etc installation.
AS: For conda, pypi need to deploy separately, for uv as well?
DM: It already works with uv, could already install gammapy with it. You can do it, because it is in pypi and installed through pypi. It is being read by pixi and uv.
DM: In #6111 write comment that installation works.


AS: One more issue "Mask safe is plotted twice", we have another similar issue in 2.0 version of our documentation, in the DM tutorial, where we somehow have empty plots, which we never had before.
Was reported on slack, we should fix it or create an issue to fix it.

AS: KF started to do a major cleanup of gammapy tests, was planned for a long time. Looking into #6210. Some of the tests were not failing but marked as x-fails. We have problem with ObservationChecker, either deprecate it or take it out, as we do separation of gadf format from internal format, what LS is also doing now.
Then a test from sherpa was breaking, I tried to do a constrained fit, prob. not correct way of doing it. Best value less then y-min. Good to merge.

AS: General comment about all our open issues. Now RT moved everything to either wishlist or no milestone (?) associated to any of them. RT and me will sit together next week to find good ideas for 2.1 release. Roadmap for 2.0 had very ambitious list of things we wanted to do and we did not make much progress. This time we want to be more concrete/ have more specific projects. Maybe DM; if you want to work more on infrastructure, or everybody has an idea on what they want to work on, to have some directions.
DM: MF mentioned last week, that the standard needed for science data challenge have to be tackled in 2.1, giving priorities to these issues as well. (???)
Looking at label "SAT req.". DM: Probably a bit outdated, were in contact with David Green.
AS: D you have a list?
DM: We have prelim. list of science cases but still have to go through it.
AS: Regarding what gammapy can not do as well?
DM: We have to go through it and I will give an update.
AS: Would be very important.
AS: Is #4644 "Generation of a pdf version of our documentation" supported? DM: Probably yes.

RT joins the meeting.

#6128 "Prototype for a new ObservationTable class"
------------------
LS reports and shows attached jupyter-notebook, with which the class can be tested. The prototype introduces a new internal data format for the observation table and a reader, that can recognize the data format on disk and call a corresponding converter function. This way, the internal table is separated from the gadf format. For now, only a gadf->internal format converter is implemented. In all of gammapy, some tests still, should be able to fix. We wanted to ask, if you have any feedback on the design and the implementation.

AS: Does the code work also for AltAz instruments, as these columns are not specified in internal model?
LS: Yes, they are loaded as optional columns and not modified by the converter, as before.
AS: Would it be good to also implement into the internal model, analog to RADEC, which units they should have?
LS: Yes agree, thank you!
LS: A question I came up with is the reason/relevance of making a unique-table in data_store, which I had to adapt in l.84.
RT, MF, AS dicuss. 
AS: A table containing only one entry should also be supported.
LS: Agree, thank you, I will take care of this.

RT: Question, if in internal model, the OBS_ID is unique, maybe we need separate, unique identifier unequal to the OBS_ID.
MF: For CTAO it is even a problem, in our definition OBS_ID would connect to time of an observation of a single object. But during these observations, you might have different observing conditions and decide to split them, with independent IRFs. Independent to event types, we need to find way (???) what to dow with OBS_ID.
Question came up already, as I have heard, during discussion of VODF. What does the OBS_ID signify? Bruno and Karl redefine the OBS_ID. 
For CTAO, undefined. We have to take care about event times and stable obs times.

RT: In our internal model we need probably one unique identifier, maybe it can match OBS_ID, maybe not. This means, suggested to the presentation of LS, that converter has to do this. Not clear, if two different observations for different ops-types (???). Design choice we have to make. Internal obstable will depend on these kind of choices. In general, my suggestion: We have some observation metadata and ideally the observation table should follow those as much as possible. Currently only obs_id is mandatory entry in the metadata. In the end, maybe it should be the same for the table. But you have a Pointing, RADEC, AltAz, ... This could basically serve as a kind of building block for the datamodel.
AS: Currently we have some functions to create obs table from the event list if it is not present.
RT: Yes from the eventlist, ideally it is directly done from metadata form the observation.
AS: Yes then you dont need to go through  the event list.


Discussion of #6210
-----------------------

AS: Thank you KF for starting th cleanup for gammapy tests. PR #6120 good to merge for me. Main question was ObservationChecker, probably need to address this in separate issue.
RT. In general, we have these checkers, implemented a long time ago. They check that data in memory actually follows GADF-standard. We should change the logic. Those checkers we don't really use. Even the Observation checker should be deprecated, as validation should be done on read. Proper validation on write should be introduced.
AS: They should definitely be deprecated.

#6115 "Kwargs updates", #6114 "When to keep kwargs"
---------------
KF reports: There was an issue, but could not check what was done before (???). When I came across, I noticed in certain cases we had kwargs and args, that were not implemented in actual code. Question of consistency. From my perspective, we should just remove these, confusing for reader to put in, if they dont do anything. Alternative, keep them consistent for API, but either raise warning in case of extra arguments or say they should be ignored.
AS: I think they are there for API-consistency reasons, that as general motivation. Maybe we should add a warning.
KF: For me it is strange, the functions do not even include the kwargs at all.
RT: In general, it can be confusing. It is a design choice, there are pros and cons for both. Here (#6114) not clear if we can have a workflow that follows the other (???). 
AS: In this case yes, but in our modeling we often pass things through model arguments and we have empty kwargs, just kept for consistency. (???) Probably difficult to come out with a clean cleanup.
KF: We probably just have to make a decision. In #6115 not much cleanup needed at all. I did not have time to look into the issue more, but quite simple.

#6108
--------
AS: Strange unit produced. This PR solves it. Will need a review. Probably test should not just check values, but also units. 
RT: We postponed it to 2.1, TB said something was missing.


#6102
--------
AS: KF you change the documentation here?
KF: Yes, was just going through some issues from 2.1, tried to solve some simple ones. In this case, just add some documentation. Copied the logic to the documentation (???). Gave two examples.
AS: AG, you have left a comment here?
AG shares screen. AG: Am a bit confused about definitions of rmin, rmax, usually we do line of sight integral as outlined in comment. Not clear, how cosine rule applied in line with differential dl. Left a comment. I will try to cross-verify results with pppc.
KF: Outside of my area of expertise, please feel free to comment anything you find. I just updated the documentation after we changed the code.
AG: There was a comment from three years back. Would like to see from the geometry, what is meant by rmin, rmax. Not common for j-factor calc. 
AS: We have not made much progress on this in the last 3 years.
AG: Maybe some typos in the formula. I can proceed on my own and try to crosscheck results.
KF: Probably we dont get a reply.
AS: Lets leave it open for a bit more time.
AG: I'll keep working on it and update you.

#6097 "Update release.rst after 2.0 release"
------------
AS: RT can you do a review on this? RT agrees.
RT: We should include .rst into checklist of needed things for release process. Not now, but ideally convert into an issue. I will review.

AS and KF, RT discuss on towncrier. 
----------------------
KF: Potential it might change. 
RT: Main change it introduced, if you create a PR you have to add changelog entry. A dedicated file with a specific line that will be added to the changelog in the end. KF: Called "fragments". 
RT: We have to start very early with this in the new development cycle. We can do it now. Either now or after 2.1.
KF: Then maybe after 2.1?
AS: Needs to be reviewed as well, probably we can try to get into habit of using this. We could see if we use towncrier for the release?
RT: DM commented that towncrier prob. complains if nothing is in. 
AS: #6097 can be merged independently of towncrier.


#6093 "Suppress pedantic warnings"
---------
KF: AD approved it, can go in. We had a line that was repeated twice, changed a few settings and this fixed it.
AS and KF look through it.
AS: I suppose we can merge, I will leave approving review.


AS: Two PR from QR, maybe discuss another time. RT agrees.


#6006 "Add utility function to create a grid of rectangular regions"
-----------------
AS: Was postponed to 2.1. Simple utility functions to have regions in lat and lon grid. I think it is good for a review.
RT: Maybe pixels in. image can be transformed in regions? (???) Another way to see the same problem.
AS: Yes, wanted to do it for subset of the pixels. Do you propose to have each pixel as an independent geom?
RT: No, just in the end you build system in which you have a region for a pixel, convert wcs (???)


#5971
------
AS: Relatively old, was a draft, not sure if it shall go in.

RT: We have to go through the list of open issues, not now, but we should try to organize the open issues. We will meet next week to discuss and try to come up with a number of projects. Maybe we can discuss all this next week.
AS: Yes, we discussed this also a bit in the beginning, DM added SAT-req. for 2.1 release.
RT: Need list of use cases for the SDC. We have to see if we lack something. Simulation wise, I think we should be okay.
AS: Then next week we can have a better plan how to proceed for the next release.


RT: Question from my side, you discussed issues in the documentation. AS answers and agrees too create reminder for the DM issue, that was opened in the help-channel. 


## General information

## Open issues

## Bugs

## Documentation

## DevOps

## Validation & benchmark

## Ongoing projects:

### sensi

### HLI

### MWL

## Any other business

# Automatic activity report
### PRs opened last week (less than 8 days ago): 
* [#6128](https://github.com/gammapy/gammapy/pull/6128) Prototype for a new ObservationTable class - Leander Schlegel
* [#6120](https://github.com/gammapy/gammapy/pull/6120) Remove some unnecessary `xfail` commands in tests - Kirsty Feijen
* [#6116](https://github.com/gammapy/gammapy/pull/6116) Add missing contributor in release notes for v2.0 - Gabriel Emery

### PRs merged last week (less than 8 days ago): 
* [#6126](https://github.com/gammapy/gammapy/pull/6126)  Backport PR #6123 on branch v2.0.x (Bump actions/first-interaction from 2 to 3) - Régis Terrier
* [#6125](https://github.com/gammapy/gammapy/pull/6125) Backport PR #6123 on branch v2.0.x (Bump actions/first-interaction from 2 to 3) - Régis Terrier
* [#6124](https://github.com/gammapy/gammapy/pull/6124) Backport PR #6122 on branch v2.0.x (Bump actions/checkout from 4 to 5) - Lumberbot (aka Jack)
* [#6123](https://github.com/gammapy/gammapy/pull/6123) Bump actions/first-interaction from 2 to 3 - None
* [#6122](https://github.com/gammapy/gammapy/pull/6122) Bump actions/checkout from 4 to 5 - None
* [#6119](https://github.com/gammapy/gammapy/pull/6119) Remove `plot_interactive` in 3D analysis tutorial - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6127](https://github.com/gammapy/gammapy/issues/6127) Fix automatic generation of author list - Atreyee Sinha
* [#6121](https://github.com/gammapy/gammapy/issues/6121) Use SonarQube for quality assurance - Daniel Morcuende
* [#6118](https://github.com/gammapy/gammapy/issues/6118) Inconsisten edge unit/type for MapTimeAxis - Tomas Bylund
* [#6117](https://github.com/gammapy/gammapy/issues/6117) Mask safe plotted twice in residual panel of count distribution plot - Daniel Morcuende

 report created at 05/09/2025, 07:22:44
