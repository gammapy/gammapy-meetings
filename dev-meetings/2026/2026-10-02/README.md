# Gammapy Developer Meeting 
 * Friday, October 02, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

Attendees: 

# Agenda
## General information

### Report about user call
	- few attendance - reached 20
   - Need to distribute info better next times
 - Talks:
  	- 3D usage for pile-up of Swift 
	  - UL talks 
 - what have we learned about ULs?
			- bug: if confidence fails success is still True
			- documentation issue: stat-scan values not used for UL
				 - might clarify tutorial
			- 1 sided or 2 sided intervals might not be consistent everywhere
			- some brazilian flag plot for SED could be useful


## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

## Validation & benchmark

## Ongoing projects

### DM project

#### HDM spectra in gammapy (Sruthi)
	- Objective: Introduce support for Heavy Dark Matter models in Gammapy
 - photon yield depends on DM model
	  - currently implementation relies on PrimaryFlux using AtProductionGamma file
	- [HDMspectra](https://github.com/nickrodd/HDMSpectra) package uses data stored in hdf5
		 - has its own interpolator
	- option 1: build a AtProductionGamma file manually
		 - pb: many more channels than other DM spectra
	- option 2: call the HDMSpectra interpolator
		 - pb: add a dependency
		 - pb: list all allowed channels is different 
	- QR: how efficient is calling the interpolator (called at each evaluation)?
		 - vectorized energy call
	- QR: try option 1 with the script in gammapy-data public 
		 - file size?
	- decision: test file size after conversion and take decision afterwards

#### discussion about priors needed for DM
	- #6880: not a lognormal prior but a gaussian in log space
		- gaussian prior for the log of a parameter
		- not a real pdf 
	- Question: need to clarify usage and the publicity?
		- never explicitly called, keep private

 ### Energy dependent region
	- becomes complex for serialization
	- close PR but revert serialization commits
	- Marie: similar usage in BaccMod
	- decision: don't go for serialization
		 - check if other solutions could work

### Format validation & IO
- simplified validator classes.
- PIG should be ready by next week

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6879](https://github.com/gammapy/gammapy/pull/6879) Backport PR #6867 on branch v2.0.x (Fix memory blowup when computing covariance of many-parameter models) - Lumberbot (aka Jack)
* [#6876](https://github.com/gammapy/gammapy/pull/6876) Put the J/D-factor prior on `factor` instead of `scale`, and fix `LogNormalPrior` centring - Alexander Cerviño Cortínez
* [#6872](https://github.com/gammapy/gammapy/pull/6872) Introduce EDispPlotter and EDispKernelPlotter classes - Ahmed Mahmoud
* [#6868](https://github.com/gammapy/gammapy/pull/6868) Add EffectiveAreaPlotter - Rahma Wael

### PRs merged last week (less than 8 days ago): 
* [#6878](https://github.com/gammapy/gammapy/pull/6878) Bump astral-sh/setup-uv from 10.0.1 to 10.2.0 - None
* [#6874](https://github.com/gammapy/gammapy/pull/6874) Fix missing  requires_dependency("healpy") in tests - Quentin Remy
* [#6873](https://github.com/gammapy/gammapy/pull/6873) Uncouple `make_effective_livetime_map` from other maker util function - Tomas Bylund
* [#6867](https://github.com/gammapy/gammapy/pull/6867) Fix memory blowup when computing covariance of many-parameter models - Ahmed Mahmoud
* [#6861](https://github.com/gammapy/gammapy/pull/6861) Fix separation warning - Tomas Bylund
* [#6851](https://github.com/gammapy/gammapy/pull/6851) Adapt documentation errors - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6877](https://github.com/gammapy/gammapy/issues/6877) Add a tutorial to showcase the FluxCollectionEstimator - Fabio Acero
* [#6875](https://github.com/gammapy/gammapy/issues/6875) Add CTAO prod6 IRFs - Kirsty Feijen
* [#6871](https://github.com/gammapy/gammapy/issues/6871) Minos confidence fit not reporting failure in FluxPoint upper-limit - Fabio Acero
* [#6870](https://github.com/gammapy/gammapy/issues/6870) Correct notebook - Atreyee Sinha
* [#6869](https://github.com/gammapy/gammapy/issues/6869) [SAT Use Cases] Compile table with currently supported use cases with evidence - Daniel Morcuende

 report created at 02/10/2026, 07:56:32
