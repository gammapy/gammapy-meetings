# Gammapy Developer Meeting 
 * Friday, January 30, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Tomas Bylund (TB), Livia Silva Rocha (LR), Daniel Morcuende (DM), Kirsty Feijen (KF), Atreyee Sinha (AS), Katharina Egg (KE), Quentin Remy (QR), Bruno Khelifi (BK), Regis Terrier (RT), Fabio Pintore (FP)

# Agenda
## General information

Paper status for the eROSITA validation with gammapy -- in draft mode (HESS courtesy review will occur soon). Plans to distribute within the gammapy devs.

SDC pre-simulations: a look from gammapy people might be needed to check the files

AS will present gammapy v2.0 at MuMENTA

### Next user call 
- Slow progress on planning, no volunteers found so far. 
- Dark matter user call does not seem possible at this time. They are still working on things.
- We could instead wait and present 2.1 in March after the release
- Plan is to discuss with Sophie about BAccMod on Monday
- Idea to showcase scripts for doing various science to the broader audience
- Fabio's student has done some work with CHANDRA -- plan to ask further and see if one of his team will present in the next call

### Unbinned analysis

Further discussions are occurring on this matter after the introduction of a number of PRs from Guillaume. 

### Workflow package

QR has made a number of updates. Some questions are raised regarding `Product` implementation and how to have some separation of concerns regarding containers and parallelism.


### Gammapy v2.1 discussions
We should discuss what we need/want for 2.1 as the deadline is fast approaching:

[Current issues](https://github.com/gammapy/gammapy/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A2.1)
- [Support for Python 3.14](https://github.com/gammapy/gammapy/issues/6201), DM is still working on this as there are fails due to some infinite loop with cython. The related [PR](https://github.com/gammapy/gammapy/pull/6225), DM says its a bit of a mess as there are so many incompatibilities. Plan is to resolve the matplotlib requirement first.
- [#6287](https://github.com/gammapy/gammapy/issues/6287) already has an associated PR that AS will work on the comments 

[Current PRs](https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A2.1)

- The team went through the PRs to decide which ones can be moved from v2.1

[Plus these](https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A2.0.2)

Make a decision [here](github.com/gammapy/gammapy/pull/6339)
- AS mentions that the point is to obtain the sensitivity of different instruments (i.e. to allow for joint sensitivity)
- RT to say about creating a joint light curve as well
- QR mentions the need to make sure we are not double counting events
- the better option would be to raise the error still but there is an option to override the option (QR)
- we should also document this better and have clearer messages 
- AS wonders if people will continually want joint light curves, RT says it is hard to know but we should make it a conscious decision by the user to allow the computation 
- v2.1 solution is to add an argument (bool) to override this with a docstring that explains clearly that this is an experimental feature (from discussion of RT, KF, BK, QR and QS). 
- v2.2 solution then we can add a tutorial that explains how we can do the joint flux points (from discussion of RT, KF, BK, QR and QS)

    - important to note that the axes must align (therefore it probably won't work in most cases)



## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

Currently 1 related PR: https://github.com/gammapy/gammapy/pull/6295
- And one issue but it should be solved by the corrections in the above: https://github.com/gammapy/gammapy/issues/6287

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

We will keep track of SonarQube on the new issue [#6239](https://github.com/gammapy/gammapy/issues/6239)
- need to make sure we keep track of these, BK will make sure his new PRs are marked as done
- RT suggests that we fix the `blocker` list before the next release

## Validation & benchmark

Multiple fails occurring but RT has been working on this. 

One solution has been the caching of the data (as these are several MB)
- could be reused in other places also
- the workflow will now check the last commit to see if the repo has changed, then the caching will occur (this is defined in `.github/workflows/scheduled.yml`)
- if you don't find the cache it needs to be run and if it does it will just proceed -- this gives significant speed up (10mins vs 25mins)

The next solution by DM is to remove large files which are not being tracked
- ignore the large files and potentially remove them during run time
- RT says we can safely remove the files from the plotting, but are needed for the benchmark

QR will investigate the PRs from DM


## Ongoing projects

## Any other business

AS asks whether the solution in [#6298](https://github.com/gammapy/gammapy/pull/6298) is really correct? RT thinks it is fine and we can proceed. Stefan Frose approved the addition, so it should be fine. 

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6349](https://github.com/gammapy/gammapy/pull/6349) Fix fragments - Kirsty Feijen
* [#6348](https://github.com/gammapy/gammapy/pull/6348) Improve functionalities of makers.make_theta_squared_table - Fabio PINTORE
* [#6340](https://github.com/gammapy/gammapy/pull/6340) Remove deprecations for v2.1 - Kirsty Feijen
* [#6339](https://github.com/gammapy/gammapy/pull/6339) Replace exception for two different telescopes in `FluxPointsEstimator` - Kirsty Feijen
* [#6330](https://github.com/gammapy/gammapy/pull/6330) [PROTOTYPE ]Unbinned TEST (DO NOT MERGE) - None
* [#6329](https://github.com/gammapy/gammapy/pull/6329) Unbinned Analysis : The statistic used for unbinned analysis (7/7) - None
* [#6328](https://github.com/gammapy/gammapy/pull/6328) Unbinned Analysis : Base Makers + reflected background update (6/7) - None
* [#6327](https://github.com/gammapy/gammapy/pull/6327) Unbinned Analysis : Spectral Background interpolated model (5/7) - None
* [#6326](https://github.com/gammapy/gammapy/pull/6326) Unbinned Analysis : Unbinned Evaluator (4/7) - None
* [#6325](https://github.com/gammapy/gammapy/pull/6325)  Unbinned Analysis : Unbinned IRF (3/7) - None
* [#6324](https://github.com/gammapy/gammapy/pull/6324)  Unbinned Analysis : Unbinned geometry / Region and Map (2/7) - None
* [#6323](https://github.com/gammapy/gammapy/pull/6323) Unbinned Analysis  : EventDataset (1/7) - None
* [#6322](https://github.com/gammapy/gammapy/pull/6322) FluxPointsCollection - Quentin Remy

### PRs merged last week (less than 8 days ago): 
* [#6352](https://github.com/gammapy/gammapy/pull/6352) Backport PR #6351 on branch v2.0.x (Update setuptools version in `pyproject.toml build-system`) - Lumberbot (aka Jack)
* [#6351](https://github.com/gammapy/gammapy/pull/6351) Update setuptools version in `pyproject.toml build-system` - Maxime Regeard
* [#6347](https://github.com/gammapy/gammapy/pull/6347) Backport PR #6298 on branch v2.0.x (Fix physics error: Use mass/2 for DM decay spectrum lookup) - Lumberbot (aka Jack)
* [#6346](https://github.com/gammapy/gammapy/pull/6346) Backport PR #6194 on branch v2.0.x (Add fix to skip making cutouts if observation is far away from target…) - Lumberbot (aka Jack)
* [#6344](https://github.com/gammapy/gammapy/pull/6344) Backport PR #6338 on branch v2.0.x (Add missing tests for makers.utils) - Lumberbot (aka Jack)
* [#6343](https://github.com/gammapy/gammapy/pull/6343) Backport PR #6314 on branch v2.0.x (Minor improvement from SonarCube report (3)) - Lumberbot (aka Jack)
* [#6342](https://github.com/gammapy/gammapy/pull/6342) Backport PR #6312 on branch v2.0.x (Minor improvement from SonarCube report) - Lumberbot (aka Jack)
* [#6338](https://github.com/gammapy/gammapy/pull/6338) Add missing tests for makers.utils - Kirsty Feijen
* [#6337](https://github.com/gammapy/gammapy/pull/6337) Add missing fragment file - Kirsty Feijen
* [#6336](https://github.com/gammapy/gammapy/pull/6336) Backport PR #6335 on branch v2.0.x (Update HESS website link) - Lumberbot (aka Jack)
* [#6335](https://github.com/gammapy/gammapy/pull/6335) Update HESS website link - Kirsty Feijen
* [#6334](https://github.com/gammapy/gammapy/pull/6334) Backport PR #6333 on branch v2.0.x (Adapting astropy Parameter usage in gammapy.astro ) - Lumberbot (aka Jack)
* [#6333](https://github.com/gammapy/gammapy/pull/6333) Adapting astropy Parameter usage in gammapy.astro  - Régis Terrier
* [#6332](https://github.com/gammapy/gammapy/pull/6332) Backport PR #6259 on branch v2.0.x (Don't create PSFMap for `SpectrumDataset`) - Lumberbot (aka Jack)
* [#6331](https://github.com/gammapy/gammapy/pull/6331) Backport PR #6318 on branch v2.0.x (Fix issues for the test ubuntu-latest, devdeps) - Lumberbot (aka Jack)
* [#6321](https://github.com/gammapy/gammapy/pull/6321) Fix incorrect docs rendering and the template for towncrier - Kirsty Feijen
* [#6319](https://github.com/gammapy/gammapy/pull/6319) Cleanup related to HAWC on gammapy-data - Kirsty Feijen
* [#6318](https://github.com/gammapy/gammapy/pull/6318) Fix issues for the test ubuntu-latest, devdeps - Bruno Khélifi
* [#6317](https://github.com/gammapy/gammapy/pull/6317) Backport PR #6313 on branch v2.0.x (Minor improvement from SonarCube report (2)) - Lumberbot (aka Jack)
* [#6314](https://github.com/gammapy/gammapy/pull/6314) Minor improvement from SonarCube report (3) - Bruno Khélifi
* [#6312](https://github.com/gammapy/gammapy/pull/6312) Minor improvement from SonarCube report - Bruno Khélifi
* [#6298](https://github.com/gammapy/gammapy/pull/6298) Fix physics error: Use mass/2 for DM decay spectrum lookup - Y. Emre Bahar
* [#6296](https://github.com/gammapy/gammapy/pull/6296) [Prototype] Multi-source regularized flux points - Quentin Remy
* [#6259](https://github.com/gammapy/gammapy/pull/6259) Don't create PSFMap for `SpectrumDataset` - Katharina Egg
* [#6256](https://github.com/gammapy/gammapy/pull/6256) Adds `Datasets` addition functionality - Quentin Remy
* [#6255](https://github.com/gammapy/gammapy/pull/6255) Add sample_parameters_from_covariance method on models. - Quentin Remy
* [#6232](https://github.com/gammapy/gammapy/pull/6232) Dark Matter module: Include the option of using either CosmiXs or PPPC4 as a source for creating the DM spectra - None

### issues opened last week (less than 8 days ago): 
* [#6341](https://github.com/gammapy/gammapy/issues/6341) Consistency in using mixed-case variable naming - Daniel Morcuende

 report created at 30/01/2026, 07:44:02

