# Gammapy Developer Meeting 
 * Friday, October 10, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Quentin Remy (QR), Tomas Bylund (TB),  Leander Schlegel (LS), Kirsty Feijen (KF),  Régis Terrier (RT),  Axel Donath (AD), Aritra Gupta (AG), Daniel Morcuende (DM), Fabio Pintore (FP),  Katharina Egg (KE),  Atreyee Sinha (AS), Bruno Khélifi (BK), Claudio Galelli (CG), Matthias Fuessling (MF)

# Agenda
## General information

### Presentation of Plotters PIG (AS)

[#5726](https://github.com/gammapy/gammapy/pull/5726)"[PIG] Introduce Plotter classes" documents a suggestion for how to separate out plotting code into more general plot routines instead of keeping them integrated in the gammapy core classes. 
As an example of how current setup causes problems, a user had the idea to create an entirely new dataset class simply to modify the plotting function, this is not ideal.

The idea is to create new, dedicated plotter classes, that are in charge of visualising the core dataclasses.

One downside is that a new way of plotting will be a big change for the users, since plotting is very important use case.

AD and TB give positive feedback. 
KE asks if change is only for datasets or also plotting functionality. AS answers that it affects both.

AD mentions the MapPanelPlotter function. Idea is to rather plot multiple maps with same config by reusing a plotter object, instead of creating a new plotter class for each of these plots.

## Open issues

## Bugs

[#6182](https://github.com/gammapy/gammapy/issues/6182) "Problems with temporal model" is reopened.

[#5985](https://github.com/gammapy/gammapy/issues/5985) "RADECSYS is deprecated" was solved by updating the metadata accordingly.

[#6143](https://github.com/gammapy/gammapy/issues/6143) "RegionGeom.from_regions throw errors with some list of regions containing regions distant from each other" is discussed (AS). RT suggests that list of RegionGeom could be needed. TB mentions a possibly related problem where doing cutouts when regions don't overlap gives poor errors.
AS will add general docstring highlighting that regions are intended to be used only within a limited area on the sphere, and will not work properly if the regions are far from each other.

[#5946](https://github.com/gammapy/gammapy/issues/5946) "For HAWC, ObservationTable.select_sky_circle crashes". This method is not appropriate for a drift-scan type telescope like HAWC, so it is not surprising it doesn't work. As there is no pointing radec, we should check if there is a good error message. A proper selection method would at minimum require a datetime along with the sky direction.
Decision to keep it on wishlist and change to "feature-request" and "cleanup".

[#5928](https://github.com/gammapy/gammapy/issues/5928) "Bug in linear IRF Interpolation near boundary" A complicated problem to solve with its roots in how the IRFs are defined: the problem is that at the edge of the IRF range weird things can happen but no safe range is defined on the IRFs. Having IRFs in bins, meaning they cover a range of values is problematic as it mixes a range of different situations and will lead to systematics. Clear example is effective area in the center offsets, where a hole shows up at higher energies. BK thinks it is better to create IRFs using simulations done at fixed parameter values, what he calls "nodes", instead.
RT suggests that solution could be, to create mask during MapDataset-creation, which excludes last half of IRF bin. Label changed to "feature", timescale is longer.

## Documentation

## DevOps

### small discussion on towncrier PR #6130
Idea of the PR is that towncrier can make the changelog, if fragments are provided for the PR.
KF reports the PR is almost ready. Decisions need to be made, what to write in documentation. 
Discussion about order of steps and about what to do with PRs between feature freeze and release, e.g. bugfixes.
Open question if own filename can be defined when using towncrier. 
RT suggests that a solution like in astropy (global changelog and small piece on top for each release) could be an idea.
There is also PR #6173 that adds towncrier fragments that correspond with some recent PRs that will be needed to make the changelog for 2.1

### Sonarcube code quality check
DM has created PR #6150 that adds a sonarcube integration on the repo that will run the code quality check after all other CI steps have completed. DM has run the checks on his own fork and generated an example report, it's a bit long right now, so they expect some tuning regarding what issues to flag will be required. Evens so, gammapy passes the code quality gates.
Next step is to review and merge and afterwards see if update/adaption is done.

### Pre-commit fixes
NP has created PR #6185 to add some options to the CI that ensures the pre-commit hook always run. Because these pre-commit steps weren't always run, there is a bunch of files that will be need to be touched to fix mainly white-space issues.


## Validation & benchmark

## Ongoing projects

## Any other business

KF asks about how to handle PR #6137, where it is not clear to handle the argument `size_factor` in different situations because it doesn't have a single well defined meaning. Further discussion will be held on github.

AS will create poll in dev channel for dedicated dark matter meeting.

KF asks for time of next bugfix-release. RT answers it is not yet planned. AS asks if the fixes done since v2.0. are minor enough to not make a bugfix-release urgently and RT confirms that they are rather minor. KF brings up that an earlier release would be better. Will be decided in the coming weeks. 

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6187](https://github.com/gammapy/gammapy/pull/6187) Unbinned likelihood analysis  - None
* [#6185](https://github.com/gammapy/gammapy/pull/6185) add common pre-commit hooks - npigoux
* [#6184](https://github.com/gammapy/gammapy/pull/6184) fix: run pre-commit on all files - npigoux

### PRs merged last week (less than 8 days ago): 
* [#6191](https://github.com/gammapy/gammapy/pull/6191) Backport PR #6189 on branch v2.0.x (Replace deprecated keyword by RADESYSa) - Lumberbot (aka Jack)
* [#6190](https://github.com/gammapy/gammapy/pull/6190) Backport PR #6182 on branch v2.0.x (Correct PhaseCurveTemporalModel integration bug) - Lumberbot (aka Jack)
* [#6189](https://github.com/gammapy/gammapy/pull/6189) Replace deprecated keyword by RADESYSa - Leander Schlegel
* [#6188](https://github.com/gammapy/gammapy/pull/6188) Allow for RunTime warning in NaN for test_pwn - Kirsty Feijen
* [#6182](https://github.com/gammapy/gammapy/pull/6182) Correct PhaseCurveTemporalModel integration bug - Régis Terrier

### issues opened last week (less than 8 days ago): 
* [#6186](https://github.com/gammapy/gammapy/issues/6186) Add models of Galactic absorption - Bruno Khélifi
* [#6183](https://github.com/gammapy/gammapy/issues/6183) pre-commit was not run on all files - npigoux

 report created at 10/10/2025, 07:23:08
