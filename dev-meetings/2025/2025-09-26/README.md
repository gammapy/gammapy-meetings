# Gammapy Developer Meeting 
 * Friday, September 26, 2025, at 2 pm (CET) approx. 14:00-15:30
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Leander Schlegel (LS), Tomas Bylund (TB), Quentin Remy (QR),  Bruno Khelifi (BK), Atreyee Sinha (AS), Kirsty Feijen (KF), Katharina Egg (KE), Nathan Pigoux (NP), Régis Terrier (RT), Fabio Pintore (FP)

# Agenda

## User call September 22
Around 43 attendants, some people have contacted AS expressing interest in working on the Dark Matter module, AS have added them to the slack. Stefan Fröse reached out, but independent to the call.

Some users have asked if it is now safe to do Fermi analysis with Gammapy, as previous versions warned it is not safe/preliminary.  Probably we were overcautious and it is more safe now. We should advertise that we now have Fermidataset-reader. Maybe add a notice to the Fermi tutorial to highlight new capabilities.

Find new date and topic for next call. There are four-five new users interested in working on Dark Matter.

## Feedback SAT-SDC-Gammapy meeting
The data for the SDC is now planned to be released at the end of 2026 (delayed again).

Objective was to discuss requirements for future CTAO-SDC releases to gammapy and use-cases. David Green works on general view on science- and analysis use-cases. Draft list of use-cases exists. RT confident there should be no problems to fulfil the analysis requirements once finalised.

For simulation use-cases there is a known problem with the light curve functionality.
Way normalization is made for phase curve in temporal models might be problematic for large phases. Simplest solution could be optional normalization like for spatial templates.
See Issue [#6138](https://github.com/gammapy/gammapy/pull/6138).
FP will provide simple, clean example for the problem in the Issue.

Because the SDC does not require anything but standard pointing mode, no problem with current limitations on the event sampler or lacking support for drift mode.

Changes to the metadata created when using gammapy for simulating data is foreseen, but nothing concrete yet. 

BK will be part of IRF validation work. There are discussions about adding systematic uncertainty to the IRFs.  

Suggestion is to vary the background normalisation and also of varying the effective area.

Promises that before end of year there will be a document specifying a  GADF-variant specific for the SDC, basically some extra metadata added (SDC Format, consisting of GADF + CTAO metadata). Will be needed for v 2.1. Add of metadata for DL4 and DL5 planned for v.2.2.

SAT will likely use Gammapy release 2.1 in early 2026. RT is confident that we are good in most points, might need effort to support additional model for DL3-data, a preliminary format close to, but different to GADF, that contains additional metadata. Karl Kosack is working on it. Not clear if ready for 2.1 or if it takes longer.

Gammapy devs should expect to review some documentation and tutorials created by CTAO for the Science Data Challenge, currently no date for when that will happen.

Next release early next year, main priority from CTAO is finishing up separation of datamodel and data format. Need writer. Shall already have option to change format. Main difference will be connected to metadata. Minimal change in writer needed to check for metadata.
Ideally Gammapy release 2.2 in Sep/Oct 2026. Here, more work needed, deploying metadata throughout the various products.

TB mentions prospect of real data from CTAO, people will try to analyze real LST data with Gammapy maybe end of the year. RT confident it will work, as LST-1 data already analyzed with Gammapy.

## Projects

### [BugTracker](https://github.com/orgs/gammapy/projects/36/views/1)

[#6164](https://github.com/gammapy/gammapy/pull/6164) Bug caused by missing brackets and this PR fixes it. Code-formatting not done yet, tests need to be adapted/added. KF asks Pierre if he can work further on it and can take over otherwise.

[#6135](https://github.com/gammapy/gammapy/issues/6135) Should we allow the computation of joint fluxpoints using data from several different instruments? Currently it is forbidden because the flux points are made in reconstructed energy, but different instruments can have different responses and so the energies of the different fluxes are not exactly comparable. 
BK stresses potential problems with statistical fits of flux points and suggests, that meaning of flux points for SEDs in contrast to butterfly should be discussed, will discuss with CTAO.

It is decided that the ban on fluxpoints from joint fit with different telescopes is lifted and instead a warning is emitted.

Some ideas of what to replace fluxpoints with were presented, but deciding on what to use instead will need a dedicated project

### [Devops](https://github.com/orgs/gammapy/projects/31)

- Sonarqube integration [#6150](https://github.com/gammapy/gammapy/pull/6150)
No updates.

- Adding Towncrier
Workflow added by KF, works for this PR. Maybe test by adding changelog label and test. Basically ready for review. AS, TB agree that it is good to have towncrier, RT adds milestone 2.1.

- Move to pyproject.toml
[#6129](https://github.com/gammapy/gammapy/issues/6129) No high priority, can stay on whishlist for now.

- Separation of internal data format from GADF
LS works on two PRs, the first one introducing a reader+converter functionality from gadf to the internal format and a second PR, in which this reader+converter will be interfaced from a reworked observation table class, to make the separation of the internal data format and gadf.

- [#6168] https://github.com/gammapy/gammapy/pull/6168 TB, simple quality of life feature to the EventList

### [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

LS went through user guide, small PR #6162 together with KF was merged.

### Other Issues
- [#6165] https://github.com/gammapy/gammapy/issues/6165 New feature request about adding normalisation option to the Reflected Background, but not clear how this is best done. Possibly the user could be asked to provide an initial prototype.

## Prioritisation for 2.1
Need to put priority on the data format.  Plotters will be discussed next week by AS. RT could discuss about Penalties and priors, QR about Bayesian model selection. Sky model will take time. Systematic uncertainty models would be good for 2.2. For unbinned analysis, drafts exist already.

## AOB
Next Friday at 10, shared work on Gammapy recipes in same zoom link.

## Automatic report

### PRs opened last week (less than 8 days ago): 
* [#6164](https://github.com/gammapy/gammapy/pull/6164) Fix division in error calculations for compute_flux_doubling - Pierre Pichard
* [#6162](https://github.com/gammapy/gammapy/pull/6162) Fix small formatting issues in user guide - Leander Schlegel
* [#6158](https://github.com/gammapy/gammapy/pull/6158) Add further test for sensitivity - Kirsty Feijen
* [#6150](https://github.com/gammapy/gammapy/pull/6150) Sonarqube integration - Daniel Morcuende
* [#6147](https://github.com/gammapy/gammapy/pull/6147) Add Logparabola2Spectral model - Quentin Remy

### PRs merged last week (less than 8 days ago): 
* [#6166](https://github.com/gammapy/gammapy/pull/6166) Backport PR #6097 on branch v2.0.x (Update release.rst after 2.0 release) - Lumberbot (aka Jack)
* [#6163](https://github.com/gammapy/gammapy/pull/6163) Backport PR #6155 on branch v2.0.x (Fix blank plot in astro dark matter tutorial) - Lumberbot (aka Jack)
* [#6161](https://github.com/gammapy/gammapy/pull/6161) Backport PR #6156 on branch v2.0.x (Remove extra mask plotting) - Lumberbot (aka Jack)
* [#6160](https://github.com/gammapy/gammapy/pull/6160) Backport PR #6159 on branch v2.0.x (Fix typo in edisp plotting) - Lumberbot (aka Jack)
* [#6159](https://github.com/gammapy/gammapy/pull/6159) Fix typo in edisp plotting - Kirsty Feijen
* [#6157](https://github.com/gammapy/gammapy/pull/6157) Backport PR #6136 on branch v2.0.x (Add source to FPE in upper limits tutorial) - Lumberbot (aka Jack)
* [#6156](https://github.com/gammapy/gammapy/pull/6156) Remove extra mask plotting - Kirsty Feijen
* [#6155](https://github.com/gammapy/gammapy/pull/6155) Fix blank plot in astro dark matter tutorial - Kirsty Feijen
* [#6154](https://github.com/gammapy/gammapy/pull/6154) Backport PR #6119 on branch v2.0.x (Remove `plot_interactive` in 3D analysis tutorial) - Lumberbot (aka Jack)
* [#6153](https://github.com/gammapy/gammapy/pull/6153) Backport PR #6134 on branch v2.0.x (Add energy dependent tool paper) - Lumberbot (aka Jack)
* [#6152](https://github.com/gammapy/gammapy/pull/6152) Backport PR #6115 on branch v2.0.x (Kwargs updates) - Lumberbot (aka Jack)
* [#6151](https://github.com/gammapy/gammapy/pull/6151) Backport PR #6146 on branch v2.0.x (Remove dev docs dispatch workflow) - Lumberbot (aka Jack)
* [#6149](https://github.com/gammapy/gammapy/pull/6149) Backport PR #6141 on branch v2.0.x (Add sensitivity for other quantities of the flux maps) - Lumberbot (aka Jack)
* [#6146](https://github.com/gammapy/gammapy/pull/6146) Remove dev docs dispatch workflow - Régis Terrier
* [#6145](https://github.com/gammapy/gammapy/pull/6145) Remove numpy upper limit version constraint in requirements - Daniel Morcuende
* [#6141](https://github.com/gammapy/gammapy/pull/6141) Add sensitivity for other quantities of the flux maps - Kirsty Feijen
* [#6136](https://github.com/gammapy/gammapy/pull/6136) Add source to FPE in upper limits tutorial - Kirsty Feijen
* [#6115](https://github.com/gammapy/gammapy/pull/6115) Kwargs updates - Kirsty Feijen
* [#6097](https://github.com/gammapy/gammapy/pull/6097) Update release.rst after 2.0 release - Atreyee Sinha

### issues opened last week (less than 8 days ago): 
* [#6165](https://github.com/gammapy/gammapy/issues/6165) Background normalization in ReflectedRegionsBackgroundMaker ? - Julian Sitarek
* [#6144](https://github.com/gammapy/gammapy/issues/6144) Guideline for Codereview in Developer Guide - Leander Schlegel
* [#6143](https://github.com/gammapy/gammapy/issues/6143) RegionGeom.from_regions throw errors with some list of regions containing regions distant from each other - Mathieu de Bony

 report created at 26/09/2025, 07:23:12
