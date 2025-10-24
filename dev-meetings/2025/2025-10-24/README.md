# Gammapy Developer Meeting 
 * Friday, October 24, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Tomas Bylund (TB),  Claudio Galelli (CG), Kirsty Feijen (KF),  Daniel Morcuende (DM),  Régis Terrier (RT),  Matthias Fuessling (MF),  Atreyee Sinha (AS), Bruno Khélifi (BK), Lisa Nikolić (LN), Abhishek Abhishek (AA), Katharina Egg (KE), Mireia Nievas Rosillo (MNR), Quentin Remy (QR),

# Agenda
## General information

### Fixing date for DM user call
Weak response to the poll, several people said they would not fill out the poll but would try to connect whenever it happened. No past contributors would be able to attend to proposed date. 

The call is postponed.

### Implementing a  Asymmetric Gaussian Temporal Model 
LN and AA has created an implementation for a new temporal model to use for AGN flares, with new shape and able to fit several flares in the same light curve.

However, there is already a generalised gaussian model that could match the shape. 

In gammapy the preferred way of making more complex models is by composing several model components rather than creating entirely new models. However, temporal model has poor support for that type of composition. AS suggest creating new tutorial to show this.

(BK highlights the danger of making fits on flux points instead of the dl3 data)

RT suggests that LN and AA check whether the existing GeneralisedGaussian serves their needs, as well as trying adding more sky models for each flare to fit multiple flares. RT suggests that if successful they create a notebook that could be used as a tutorial demonstrating this use case.

Some discussion about adding a new method that allows for masking some time bins without having to create new datasets.

## [Open issues](https://github.com/gammapy/gammapy/issues)
No update

## [Bugs](https://github.com/orgs/gammapy/projects/36)
No update

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)
No update

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

### Towncrier 
- Still need final reviews [#6130](https://github.com/gammapy/gammapy/pull/6130) RT will make final review today
- Need reviews for the fragments, and we probably have more since this! [#6173](https://github.com/gammapy/gammapy/pull/6173) To be reviewed after #6130 is merged

### Sonarcube
No update

### Gammapy Recipes
Main building blocks for getting it working again are there, still needs some work to get the sphinx related parts going again.

### Python 3.14
DM tried running gammapy with 3.14 and encountered some problems, so suggests adding this version to the CI to check it properly.
RT notes that the conda builds are also failing for 3.14

### dev-deps breaking
The CI job phydon-devdeps has been failing the last few days for reasons that are not understood yet. 
RT: Need to understand this before making the bug release 

### Pre-commit and pypproject.toml
Should merge the pre-commit job before the pyproject PR. 

Adjust the pre-commit PR so the pre-commit runs on all files only periodically and not on every PR.

## Validation & benchmark

## Ongoing projects

## Any other business
### decision needs to made about the API for the `size_factor` [#6137](https://github.com/gammapy/gammapy/pull/6137) There is terrible confusion about what this argument really does, AS tried to explain it and after prompting from RT for examples KF agrees to write some. 

### Unbinned analysis drafts
Need to have a discussion about the existing drafts for adding unbinned analysis. RT will try to contact Guillaume to see when they are available to talke, which will determine if discussion happens on seperate call or at the weekly dev-call.

### Priority for next release
For CTAO some metadata need to be cleaned up but otherwise no strong outside constraints. 
The Science Data Portal will probably create constraints for the High level interface; RT will create a draft PIG and send it to QR for review. 

For other points there prioritisation work has not been concluded.

### Meeting secretary
An assistant secretary will be determined at the start of next meeting.

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6198](https://github.com/gammapy/gammapy/pull/6198) Update integrate_project_irf_on_geom to also support EffectiveAreas - Tomas Bylund
* [#6197](https://github.com/gammapy/gammapy/pull/6197) add axis_name argument and test - Fabio PINTORE

### PRs merged last week (less than 8 days ago): 
* [#6179](https://github.com/gammapy/gammapy/pull/6179) Add Checklist for Codereview in Developer Guide - Leander Schlegel

### issues opened last week (less than 8 days ago): 
* [#6201](https://github.com/gammapy/gammapy/issues/6201) Run CI also on python 3.14 - Daniel Morcuende
* [#6200](https://github.com/gammapy/gammapy/issues/6200) Introduce AsymmetricGaussianTemporalModel - None
* [#6199](https://github.com/gammapy/gammapy/issues/6199) Not all makers/utils have unit tests - Tomas Bylund
* [#6196](https://github.com/gammapy/gammapy/issues/6196) `FluxPoints.plot_ts_profiles` does not plot a lightcurve when there is only one time bin - Fabio PINTORE
* [#6195](https://github.com/gammapy/gammapy/issues/6195) Error from CompoundSpectralModel.evaluate() args for TemplateNDSpectralModel. - Tora T H Arnesen

 report created at 24/10/2025, 07:23:50

