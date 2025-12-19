# Gammapy Developer Meeting 
 * Friday, December 19, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information

### Feedback of v2.0.1 release - A.S
- A release candidate was done this time
- No serious issue. But 
	- towncrier fragments are not specific to a version. Need to produce changelog on target branch and commit result on main (and backport). Not ideal. 
	- bugfix release isntructions incomplete. A.S. has opened a PR to clarify
	- Zenodo webhook failed again. Zenodo support contacted. 
- gammapy-documentation was cleaned up. But the artefact is still more than 2 GB.
- validation was successfully run. Benchmark profiling failed for unclear reasons.
- Discussion on a possible action to trigger validation when a release trigger is sent

### Next user call
- A.S. will organize one for end January. Will contact people after the break. The proposed topic could be background creation and handling.

### Gamma-ray analysis primer?
- The previous point triggers a discussion on how to communicate on good practices beyond what is in the doc. 
- M.F. recalls the proposed gamma-ray primer document. The coming SDC release could be a nice milestone for a first version.
- Gammapy team has already numerous elements. We need to have a careful look, discuss opinions and contact people that could contribute. R.T. will organize a dedicated meeting in January.
- Q.R. shows that current LLMs already provide very good discussions on what to be done for an analysis. We have to adapt content and efforts to this situation.




## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

## Validation & benchmark

### Prototype validation for confidence interval coverage 
- R.T presents a draft of validation script for `gammapy-benchmarks` to check if the coverage of flux points confidence intervals is valid for different situations [#178](https://github.com/gammapy/gammapy-benchmarks/pull/178)
- This will help understand in which cases  the error and UL evaluation is uncertain and requires more advanced tools

## Ongoing projects

### Regularized Flux Points  for multiple sources
- Q.R. discusses new prototype PR using penalized fit statistics to estimate "flux points" for a set of sources
	- [[Prototype] Multi-source regularized flux points](https://github.com/gammapy/gammapy/pull/6296)
- Allows to obtain combined flux points for different components in a source. Q.R. reminds that our flux points, being independently extracted will have similar fluctuations in overlapping components making their combination unreliable.
- The algorithm needs tuning of the penalty weight hyper-parameter
- Result is a model enveloppe more than flux points

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6294](https://github.com/gammapy/gammapy/pull/6294) Fix some typos in source finding tutorial - Daniel Morcuende
* [#6281](https://github.com/gammapy/gammapy/pull/6281) infra: setup pixi configuration - Natthan Pigoux
* [#6280](https://github.com/gammapy/gammapy/pull/6280) Simplify drift pointing mode with built-in broadcasting in astropy>=6 - Daniel Morcuende

### PRs merged last week (less than 8 days ago): 
* [#6293](https://github.com/gammapy/gammapy/pull/6293) Backport PR #6292 on branch v2.0.x (Update index.rst for 2.0.1) - Lumberbot (aka Jack)
* [#6292](https://github.com/gammapy/gammapy/pull/6292) Update index.rst for 2.0.1 - Atreyee Sinha
* [#6291](https://github.com/gammapy/gammapy/pull/6291) V2.0.x cherrypick release notes - Régis Terrier
* [#6290](https://github.com/gammapy/gammapy/pull/6290) Backport PR #6289 on branch v2.0.x (Update codemeta.py to use pyproject.toml) - Lumberbot (aka Jack)
* [#6289](https://github.com/gammapy/gammapy/pull/6289) Update codemeta.py to use pyproject.toml - Régis Terrier
* [#6288](https://github.com/gammapy/gammapy/pull/6288) Backport PR #6285 on branch v2.0.x (Add Changelog 2.0.1) - Lumberbot (aka Jack)
* [#6286](https://github.com/gammapy/gammapy/pull/6286) Fix typo for towncrier workflow - Atreyee Sinha
* [#6285](https://github.com/gammapy/gammapy/pull/6285) Add Changelog 2.0.1 - Atreyee Sinha
* [#6284](https://github.com/gammapy/gammapy/pull/6284) Backport PR #6270 on branch v2.0.x (Add optional normalization on phasecurve models) - Lumberbot (aka Jack)
* [#6283](https://github.com/gammapy/gammapy/pull/6283) Backport PR #6274 on branch v2.0.x (Correct documentation before bug release) - Lumberbot (aka Jack)
* [#6282](https://github.com/gammapy/gammapy/pull/6282) Backport PR #6272 on branch v2.0.x (Add docs on RegionGeom.from_regions) - Lumberbot (aka Jack)
* [#6279](https://github.com/gammapy/gammapy/pull/6279) Backport PR #6176 on branch v2.0.x (infra: drop setup cfg for pyproject) - Régis Terrier
* [#6278](https://github.com/gammapy/gammapy/pull/6278) Backport PR #6223 on branch v2.0.x (Simplify the generation script for contributors for the release procedure) - Lumberbot (aka Jack)
* [#6277](https://github.com/gammapy/gammapy/pull/6277) Backport PR #6254 on branch v2.0.x (Fix map stacking for non float type) - Lumberbot (aka Jack)
* [#6276](https://github.com/gammapy/gammapy/pull/6276) Backport PR #6273 on branch v2.0.x (Add missing space in docstring to fix rendering of link) - Lumberbot (aka Jack)
* [#6275](https://github.com/gammapy/gammapy/pull/6275) Backport PR #6248 on branch v2.0.x (Add check for map type in TemplateSpatialModel) - Lumberbot (aka Jack)
* [#6274](https://github.com/gammapy/gammapy/pull/6274) Correct documentation before bug release - Kirsty Feijen
* [#6273](https://github.com/gammapy/gammapy/pull/6273) Add missing space in docstring to fix rendering of link - Daniel Morcuende
* [#6272](https://github.com/gammapy/gammapy/pull/6272) Add docs on RegionGeom.from_regions - Atreyee Sinha
* [#6271](https://github.com/gammapy/gammapy/pull/6271) Backport PR #6252 on branch v2.0.x (Fix plot_error for models evaluated with not finite values) - Régis Terrier
* [#6270](https://github.com/gammapy/gammapy/pull/6270) Add optional normalization on phasecurve models - Régis Terrier
* [#6269](https://github.com/gammapy/gammapy/pull/6269) Correct CI workflow on v2.0.x to force downloading datasets from 2.0 release - Régis Terrier
* [#6268](https://github.com/gammapy/gammapy/pull/6268) Backport PR #6265 on branch v2.0.x (Adapt estimator tutorial and add warning for lin interp) - Lumberbot (aka Jack)
* [#6267](https://github.com/gammapy/gammapy/pull/6267) Backport PR #6251 on branch v2.0.x (Resolves issues associated to plot_error) - Lumberbot (aka Jack)
* [#6254](https://github.com/gammapy/gammapy/pull/6254) Fix map stacking for non float type - Quentin Remy
* [#6252](https://github.com/gammapy/gammapy/pull/6252) Fix plot_error for models evaluated with not finite values - Quentin Remy
* [#6248](https://github.com/gammapy/gammapy/pull/6248) Add check for map type in TemplateSpatialModel - Régis Terrier
* [#6223](https://github.com/gammapy/gammapy/pull/6223) Simplify the generation script for contributors for the release procedure - Kirsty Feijen
* [#6176](https://github.com/gammapy/gammapy/pull/6176) infra: drop setup cfg for pyproject - Natthan Pigoux

### issues opened last week (less than 8 days ago): 
* [#6287](https://github.com/gammapy/gammapy/issues/6287) Enable versions for towncrier fragments - Atreyee Sinha

 report created at 19/12/2025, 07:27:20
