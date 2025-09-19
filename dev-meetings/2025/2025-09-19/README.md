# Gammapy Developer Meeting 
 * Friday, September 19, 2025, at 2 pm (CET) approx: 14:00-15:40
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Leander Schlegel (LS), Tomas Bylund (TB), Kirsty Feijen (KF), Daniel Morcuende (DM), Régis Terrier (RT), Hanna Stapel (HS),  Aritra Gupta (AG), Quentin Remy (QR), Nathan Pigoux (NP), Atreyee Sinha (AS)
 
# Agenda

## News
### SAT-SDC-Gammapy discussion on Friday Sept 26th. 9:30 CEST
Will have a meeting to coordinate with the Science Analysis Tools - Science Data Challenge team, especially to clarify the timeline for when a new format will need to be supported. Also need to clarify if they need us to add support for further use cases. Could be helpful, to prepare list questions, e.g. in dev-channel.
New model connected to VODF, but not clear to which extent.


### gammapy-recipes working session on Friday Oct 3th, 10am CEST
Meeting to get overview over the issues and coordinate how to solve them. One big challenge is to manage the diverse environments used in the various gammapy-recipes, perhaps pixi could be used to help this.

## Preparation of user call
AS shares slides. As most people do know gammapy already, no general introduction planned. Brief introduction of the new features (sensitivity calculation for analysis, full-vectorized error bar calculation, ...), Improved documentation, Outlook on plans for upcoming user calls on more specialised topics.

RT points out that as current release is new milestone, amount of work between LST 1.0 and 2.0 could be shown, incl. list of people that contributed. Also effort in meantime could be included, like the work on new datamodel.

A discussion about the possibility of asking for user input on the priorities for further features. However, not entirely simple to have right balance. 
RT summarises the message should be: that we are prioritising among too many features being requested, and if people want something on low priority they are encouraged to contribute code themselves. But users can contact us to receive support and guidance
There will be a tutorial on bayesian sampling by Fabio Pintore and one on Fermi-analysis by QR.

## Minutes
RT: We should make summary for the minutes-taking after discussions.

## Meeting structure
RT: TB, LS and me discussed about dev-call. We spend too much time on specific PR and could instead go in detail on specific PR, if needed. Important is that things are assigned, that reviews are being made and issues being tackled. Three main tasks: bug tracking, devops, documentation. For task, one person could give update. We could turn with sharing the dev-meeting in the future.

## Reports
RT has created several github projects to organise the bug tracking, the devops issues, and the documentation work.

### [Bug Tracker](https://github.com/orgs/gammapy/projects/36/views/1)

* [#6143](https://github.com/gammapy/gammapy/issues/6143) is assigned to AS
* [#6138](https://github.com/gammapy/gammapy/issues/6138) is assigned to RT
* [#6127](https://github.com/gammapy/gammapy/issues/6127) reclassified as a infra issue and moved to devops topic
* [#6118](https://github.com/gammapy/gammapy/issues/6118) reclassified as cleanup, connected to gammapy.maps, put into wishlist milestone
* [#6117](https://github.com/gammapy/gammapy/issues/6117) is assigned to KF, moved to documentation topic

### [DevOps](https://github.com/orgs/gammapy/projects/31)
#### Using sonarcube for quality assurance
DM is working on adding a sonarcube workflow to the gammapy existing CI system. Hopefully done by next week.

#### Discussion on how we want to proceed with towncrier (Draft PR #6130). 
By making developers create changelog files following a specific format, towncrier can automatically generate a well formatted changelog, including grouping several changes into sections. 

KF reports: Implementation will try to follow as closely as possible how the manually created changelogs currently look. For each PR, now rst-file has to be added. Naming-scheme: "Number of PR . Name. rst", e.g.: "1.infrastructure.rst".
KF thinks there needs to be some discussion on how we want to group changes, as this determines the naming scheme developers have to follow.
QR asks about case of multiple tags on an PR: either the developer decides which single tag to use when naming the rst-file, or you add several files, but it is not clear that actually works.

RT summarises: We stick with 'improvement'-, 'bugfix'-, 'performance'- entries as currently, decided that should have changelog workflow 

Feature, bug, api change are all labels that will require a changelog, all others will need changelogs as needed.

### [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## Report on DM
AG gives update on #174 "Validate dark matter analysis". Two standard references: PPPC4, MicrOmegaAs, give more or less same results. Add additional utilities to existing modules. Rough outline of what we could do.
Update on #6102: Maybe reason for discrepancy is, that approximation of right angle triangle not fulfilled. Will check if this is main reason for discrepancy and update.

## Backports 
QR and RT agree that backports should be done also for documentation, to avoid problems later when PRs touch documentation. We have to be careful with notable changes in docs. Do not forget to change milestone of open PR on target branch, so that they are counted properly, e.g. 2.1 -> 2.0.1. If PR already merged, comment "@meeseeksdev back port to [BRANCHNAME]". 

## Towncrier
Fragments have to be there on 2.0.x branch, have to take decision soon. Examples for fragment in e.g. astropy. KF adds links.

## AOB
- KF is planning on creating PR for more tests for Sensitivity.

### PRs opened last week (less than 8 days ago): 
* [#6146](https://github.com/gammapy/gammapy/pull/6146) Remove dev docs dispatch workflow - Régis Terrier
* [#6145](https://github.com/gammapy/gammapy/pull/6145) Remove numpy upper limit version constraint in requirements - Daniel Morcuende
* [#6142](https://github.com/gammapy/gammapy/pull/6142) Add further information about fitting to the Low Level Analysis tutorial - Kirsty Feijen
* [#6141](https://github.com/gammapy/gammapy/pull/6141) Add sensitivity for other quantities of the flux maps - Kirsty Feijen

### PRs merged last week (less than 8 days ago): 
* [#6120](https://github.com/gammapy/gammapy/pull/6120) Remove some unnecessary `xfail` commands in tests - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6144](https://github.com/gammapy/gammapy/issues/6144) Guideline for Codereview in Developer Guide - Leander Schlegel
* [#6143](https://github.com/gammapy/gammapy/issues/6143) RegionGeom.from_regions throw errors with some list of regions containing regions distant from each other - Mathieu de Bony (AS self assigned)
* [#6140](https://github.com/gammapy/gammapy/issues/6140) Addition of sensitivity for other quantities - Kirsty Feijen
* [#6138](https://github.com/gammapy/gammapy/issues/6138) Problems with temporal model. - None

 report created at 19/09/2025, 07:23:00
