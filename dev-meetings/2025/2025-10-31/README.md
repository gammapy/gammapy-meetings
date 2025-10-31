# Gammapy Developer Meeting 
 * Friday, October 31, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Régis Terrier (RT), Tomas Bylund (TB), Atreyee Sinha (AS), Fabio Pintore (FP), Katharina Egg (KE), Aritra (A ), Quentin Remy (QR),

# Agenda
## General information

### Benchmarks and validations actions fail
AS reports the failure for LST1 data download happening sometimes, Gets resolved on rerunning the actions.
 RT mentions we need better method instead of downloading from zenodo

### Minutes
Look into options for zoom AI note taking

### Pre-commit
- After PR on pre-commit was merged, you might need to run `pre-commit clean` followed by `pre-commit install` locally to be able to commit changes to a branch locally.

## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

- Issue #6204 
(connected to Nukri's reported error on slack for BrokenPowerLaw)
QR: Do as we do for naima,  ``  kwargs = {name: q for name, q in zip(self.default_parameters.names, args)}``

For bpl, line 1412 cond<energy breaks. 
Energy needs to be broadcasted to have same dim as the parameters.

RT: Are we lacking tests to catch these issues?
TestSpectralModelErrorPropagation Needs to test for all SpectralModels in Registry systematically. Assigned QR.

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

None

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

- [#6205](https://github.com/gammapy/gammapy/pull/6202): Apply codespell, a PR that runs codespell on the repo and caught many typos, we should probably ensure codespell is run more frequently
- Test version of CTAO SAT in progress on gitlab.


## Validation & benchmark

## Ongoing projects

## Any other business

Unbinned analysis discussion on 19th Nov at 14:00 CET

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6203](https://github.com/gammapy/gammapy/pull/6203) Add __repr__ method to Geom - Tomas Bylund

### PRs merged last week (less than 8 days ago): 
* [#6202](https://github.com/gammapy/gammapy/pull/6202) Backport PR #6185 on branch v2.0.x (add common pre-commit hooks) - Lumberbot (aka Jack)
* [#6197](https://github.com/gammapy/gammapy/pull/6197) add axis_name argument and test - Fabio PINTORE
* [#6185](https://github.com/gammapy/gammapy/pull/6185) add common pre-commit hooks - npigoux

### issues opened last week (less than 8 days ago): 
* [#6204](https://github.com/gammapy/gammapy/issues/6204) plot_error fails with TemplateNDSpectralModel - Régis Terrier
* [#6201](https://github.com/gammapy/gammapy/issues/6201) Run CI also on python 3.14 - Daniel Morcuende
* [#6200](https://github.com/gammapy/gammapy/issues/6200) Introduce AsymmetricGaussianTemporalModel - None

 report created at 31/10/2025, 07:23:22

