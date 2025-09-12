# Gammapy Developer Meeting
 * Friday, September 12, 2025, at 2 pm (CET)  (14:06-15:25)
 * Gammapy Developer Meeting on Zoom (direct link on Slack)
 
 Attendees: Régis Terrier (RT), Hanna (H), Matthias Fuessling (MF), Atreyee Sinha (AS), Fabio Pintore (FP), Tomas Bylund (TB), Aritra Gupta (AG), Kirsty Feijen (KF), Leander Schlegel (LS), Axel Donath (AD), Claudio Galelli (CG), Daniel Morcuende (DM)
 
# Agenda
## General information

### Priorities for 2.1
AG and RT have started looking over the list of open issues and tried to organise it. A wiki [page](https://github.com/gammapy/gammapy/wiki/Projects-and-priorities-after-2.0) has been created to organise the work called "Project and priorities after 2.0".

RT:
Initial proposal lists five projects as urgent:

Separation of internal data model and data formats
---------
Effort started in version 1.0 but still not completely done. For the Observation Table we have a prototype by LS. We need proper reader/writer for the interface.

Implementing Bayesian frameworks in GP (mostly finishing existing efforts)
-----------

Sensitivity estimation (mostly finishing existing efforts) (AS)
-------------

Metadata  (TB)
-------------
We still need full propagation of metadata.
      
Visualisations
------------
Not clear if really urgent, but we can probably refactor and simplify. Separate plotting code from core of the code, maybe we can come up with a better design in general. An example prototype exists.


After that six projects are listed as not so urgent:
    
Model refactoring
------------
Long standing issue of moving away of current MapEvaluator, maybe most complex piece of code in Gammapy. Make it more readable and flexible for design of fit-statistics. Associated to this, question of API. Prototype by AD exists.
Penalties and priors
We have already discussed different penalties, in June with Lucas Gréaux. Maybe some clarification is important, specific usage like regularization might require some fit-statistic penalties. There is a PR on how to implement it. Needs to be done, but not needed for first ???-release.

Geometry based fitting (AS, CG)
-------------------
Way to gather temporal and time resolved / space resolved analysis. Work by Claudio to build a container, left a s prototype, not worked on since a few month, we should revive it and do some decisions on what we want to do on this. Use cases: Time resolved study of variable source, .... the cases don't share the same geometry but  the same problematic.


Unbinned analysis (TB)
----------------
Giacomo and Tim (???) both worked on writing a PIG. Prototype exists. Main outcome was if we want to redo typical  analysis in unbinned way, a lot of computational effort has to be paid, but not much is gained. E.G. 3D unbanned model evaluation. Probably really important regarding time domain analysis. We don't take time axis into account clearly, split into datasets and use GTI (???). The way to go would be to have approach that is focused to some specific use cases, try to make progress this way. TB is looking into it.
Dark matter utilities
We have a number of issues and things that lack behind, need to build a working group to follow up and progress.

Then there are many further issues not connected to particular sub packages, which have not been listed in detail.

This is the first approach to prioritize. We should discuss, is anything missing, what do you think would be important and if you are interested in certain points.
AS: Thanks RT for this. We realized looking at doc, that this is a point, where we have achieved everything we intended for 2.0, credit goes to KF, she took initiative to do one topic. If "Not so urgent", not for 2.1 but we should plan it, as no of these things can happen in 6 month cycle.
RT: One thing not mentioned is DevOps, which is a long standing issue

#### Metadata
TB: About metadata: there is the CTAO build-meeting coming up. Did you plan to ask people building science data portal, what they require? Some sort of coordination with SDC  task-force?
RT states that  there is a definite need for more feedback on what is really required.

RT: I think we are blocked by the fact, that we don't know what we need to have in the end. E.g. what do we want to stack as metadata, what to keep, what to transfer to flux-points objects. Not very clear. Also discussion on what is provenance and what is metadata. We need to get further feedback.
MF agrees that a coordination meeting is needed.
MF: Meeting is pending for SDC with David Green and we should organize it next week or the week after and lets go through all the points that need to be fixed for 2.1.

- RT will get in touch with David Green (DG) and try to organise a meeting next Friday with DG, Gammapy and MF, with the goal of establishing what blocking questions about metadata exist and trying to get them resolved.
The Science Data Portal will be brought in at a later stage

#### Priority discussion
RT: If important things missing or not correct assigned please comment.
TB: Five urgent projects are maybe too many to fit in one dev-cycle, maybe we need to further prioritize. Are there PIG open but not featured?
AS: 4 open PIG and all are listed. Senistivity Estimation we are almost there. Separation of internal data format would be good to have in 2.1, to not keep it longer. But for the rest we have decision on what to do.
KF: Agree, even though 5 points, some are minimal.

AS: Maybe Handbook of Gammaray astronomy. We do not know what it would mean, which journal/book. AD do you think it is a good/feasible idea?
AD: KF mentioned X-ray data (Gamma-ray primer like they have with X-ray), is a very good idea. X-ray primer very good reference, doing something like this. Recently there was a book ... chapter on data analysis, probably not complete, could be some reference.
AS: Maybe nice to have also something related to how Gamapy evolves. Instead of having one static pdf, something you can update, something citable and updatable? Can be more than Gammapy and include details about IRFs, etc. 
RT: Regarding CTAO school, we could suggest something as a way to prepare already some gammaray primer, maybe could organize something in CTAO. Maybe to have a place were these things a really explained.
KF: https://cxc.harvard.edu(cdo/xray_primer.pdf

FP leaves.





### Dark matter
AG: I looked at some DM stuff from Gammapy and have some queries and confusions. May I share my screen?
#5734
I played around with Gammapy utilities and checked if definitions are on the same page, took PPPC paper (arXiv 1012.4515). There are some benchmark points in paper and I checked them against Gammapy.

- For annihilation they use eq. 34 and scale density with r_sun,  they have a table on p.35. First I wanted to check, that Theta is equal to Theta in the Gammapy code. I check it and they match up.
- Paper from H.E.S.S. (arXiv 1607.08142) has some J-factor calculations, table on p.10.  I have code where I try to do the PPPC stuff and compare to Gammapy. For small angle, the difference is order 0.1,0.2. More or less match at order of mag. level. But for angle 0-1,0-2 degree, then there is a huge discrepancy between both codes. Not clear why. Rectangular region B x L. Finding a lot of discrepancies and went through the code. In PR #5296, utils.py, l.63. For the angle between GC and point of annihilation and observer (???) simplifying assumption of rightangle (???) triangle done, that may explain differences. 
RT: That is interesting and good to see you have already ideas, where it is coming from. But probably we can't discuss it in detail here. Interesting approach to try to understand what is correct and what is not. Some kind of validation of the package to see if it reproduces results from PPPC paper. is a good approach. Maybe you could create a wiki-page on this or a global issue on this. Probably creating a set of validating calculations, that could be automatized. We have unit tests, but they do not necessarily check validity of assumptions.
AS: Maybe you could summarize your findings in the Issue, that would be very helpful.
RT: If issues are deeper in the code, maybe call with people who contributed to this code could be helpful. Then we could try to understand all the assumptions. Maybe a dedicated session in the coming weeks, once we find people who did the code. Stefan Fröse made some additions on this, maybe we can discuss with him. Also Judith (PhD student at the time).
DM: I spoke with Judith one year ago and she was interested trying to followup on DM in Gammapy, but do not know the status. Maybe we can contact her and see if interested in followup. I will write her.
RT to AG: Maybe script to compare base-branch and modified branch is clearest solution. AS agrees to help.
RT: Probably we can discuss in a few weeks on the status.




RT: We managed to get more organized. Discussion on open PR in Dev-Call are maybe not the best way, as they take maybe too much time and are not of interest to everyone. Instead maybe concentrate on projects and discuss specific issues, but not whole list of PRs. First thing, associate PR to specific project (technical part) and we need to have people committed to some projects (human part). Not clear how to do it, one possibility: Create one issue to gather elements and people assign to it, then create projects.
Maybe calls become unproductive if not many people discuss. Opinions and propositions abut this?

TB: List of projects, useful for many people, maybe not for one single person. Write down who is in a project and structure how a project organizes itself. First thing to do, ??? to be in a project.
RT: Yes we can create a page with list of projects, the one per project and people are listed there.
TB: We should try to collect agenda items ahead of meeting. Tried to write down fixed points, but are not alway relevant for every meeting.
RT: Maybe call in advance for contributions, e.g. Thursday sending a message to everyone asking for contributions?
TB: At least before lunch we could ask people if they are stuck with something/have something. the bigger the problem, the more time in advance needed.
AS: We had this plan but not in the end did not filled the agenda and stuck with autogeneration with PRs.
TB: I created a PR to put at least fixed point s on agenda every time.
RT: Yes, I commented is a good idea. I think we still need people to say in advance that they want to say something about specific issue/aspect of their project.
AS: Is list boring or useful?
TB: If just want to get overview summarize instead of list? right now it gest very long. Agree with DM, if you have something and need help with it, it is good to go over the issue. Or ask everyone, are you stuck or not, review would be quick. Dont know if there is perfect solution.
RT: In general we need to discuss new issues, to make sure they are clearly identified, assigned to someone or a project. For PRs it depends if someone is assigned to it. 

AD leaves.

RT: We should have assigning for PR also, is not intended to be the same person that opened the PR, but someone to make sure everything is addressed. 
RT: We can iterate between us devs and do not need to rediscuss during meeting and could focus on more important points. Maybe we can go through people here?
TB: For me it is the Metadata.
LS: For me the Separation of the internal data model and formats.
AS: I will Finish sensitivity I already started, finish maybe geombased fitting. CG do you have time to iterate on the container?
CG: Not sure but is possible. AS: I can take over your fit container PR and you can comment? CG: Yes absolutely.
By the way, since I missed some calls, what is situation with recipes, everything is okay, can I do something?
RT: We are still stuck, had possible solution but was requiring breaking most of the system.  Probably we can do something simpler. 
AS: What is main issue with recipes?
RT: System makes incremental change and when there are several, it breaks. Not easy to deal with the various environments. Has been possible to update a few.
AS: CG has Notebook on recipes?
CG: Yes exactly, wanted to open PR on recipes but stopped to ask first what is situation. CG shares screen.
Finally pushed direct interface to gammapy. But if not possible to update recipe, can at least highlight on my GitHub how to do it.
DM (comment): Use pixi for recipes?
KF (comment): I mean things do not update correctly, i.e. for the mcmc we updated in Oct 2024 but it did not update.
RT: You are right, if we have project on the side that exposes doc (???), difficult to maintain. We need to have simple solution as close a spossibel tot he one we have, not two different pipelines to build docs. 
If there are people, we could try to work on it during September on one Friday. I can create a pool for this on slack and we see if people are available.

RT: AOB?
AS: Next user call is next Monday.
RT: We could send reminder on general channel. We have to discuss what we present for the gammapy team besides demonstration tutorials (???). AS: I can make some slides, keep it very short. RT: 10 min? As agrees.

RT ends the meeting.

## Open issues
DM: Opened issue #174, the issue needs more details.


# Automatic activity report

### PRs opened last week (less than 8 days ago):
* [#6137](https://github.com/gammapy/gammapy/pull/6137) Adapt size_factor value for error - Kirsty Feijen
* [#6136](https://github.com/gammapy/gammapy/pull/6136) Add source to FPE in upper limits tutorial - Kirsty Feijen
* [#6130](https://github.com/gammapy/gammapy/pull/6130) Add towncrier - Kirsty Feijen

### PRs merged last week (less than 8 days ago):
* [#6134](https://github.com/gammapy/gammapy/pull/6134) Add energy dependent tool paper - Kirsty Feijen
* [#6120](https://github.com/gammapy/gammapy/pull/6120) Remove some unnecessary `xfail` commands in tests - Kirsty Feijen
* [#6093](https://github.com/gammapy/gammapy/pull/6093) Suppress pydantic warnings - Kirsty Feijen
* [#6027](https://github.com/gammapy/gammapy/pull/6027) Correct setup in tutorialjupytexttests.yml - Daniel Morcuende

### issues opened last week (less than 8 days ago):
* [#6135](https://github.com/gammapy/gammapy/issues/6135) Should we allow FluxPoint computation from different instruments - Atreyee Sinha
* [#6133](https://github.com/gammapy/gammapy/issues/6133) MAINT: remove numpy upper limit - Brigitta Sipőcz
* [#6132](https://github.com/gammapy/gammapy/issues/6132) Exposure not set on PSF_map and EDISP map for HAWC analysis - Atreyee Sinha
* [#6131](https://github.com/gammapy/gammapy/issues/6131) Input from CTAO on the priorities for the SDC preparation - Daniel Morcuende
* [#6129](https://github.com/gammapy/gammapy/issues/6129) Move project setup and metadata to `pyproject.toml` - Daniel Morcuende

 report created at 12/09/2025, 13:58:26%       
