# Gammapy Developer Meeting 
 * Friday, October 17, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Quentin Remy (QR), Tomas Bylund (TB),  Katharina Egg (KE),  Kirsty Feijen (KF),  Daniel Morcuende (DM), Fabio Pintore (FP),  Claudio Galelli (CG), Natthan PIGOUX (NP)

# Agenda
## New PRs
* [#6194](https://github.com/gammapy/gammapy/pull/6194) Add fix to skip making cutouts if observation is far away from target, a crash happens in the HLI if a run is too far away from the target region. KF is surprised the crash happens at all since, expecting the offset_max maker to take care of it. QR suggest using a try catch instead of an explicit if test. 
* [#6193](https://github.com/gammapy/gammapy/pull/6193) Unbinned 1d analysis using reflected background 
QR thinks it would be good to have a call with all people working on Unbinned analysis as there is already another recent draft PR. 


## Open issues
* [#6195](https://github.com/gammapy/gammapy/issues/6195) Error from CompoundSpectralModel.evaluate() args for TemplateNDSpectralModel.  Assigned to QR

## Bugs
https://github.com/orgs/gammapy/projects/36

## Documentation
https://github.com/orgs/gammapy/projects/27/views/2

Ready for merge:
https://github.com/gammapy/gammapy/pull/6179

## DevOps
https://github.com/orgs/gammapy/projects/31/views/1
### Towncrier
Just needs a final review, then people shoud look at the draft fragments for the PRs merged since latest release.
Also need to update the `github_summary.py` file now that towncrier will be used to generate the changelog

### Sonarcube
DM reports that the integration is close to being finished 

### Moving away from setup.cfg
PR #6176 implements the move to pyproject.toml style, needs review


## Validation & benchmark

## Ongoing projects

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6194](https://github.com/gammapy/gammapy/pull/6194) Add fix to skip making cutouts if observation is far away from target… - Tomas Bylund
* [#6193](https://github.com/gammapy/gammapy/pull/6193) Unbinned 1d analysis using reflected background - Tomas Bylund

### PRs merged last week (less than 8 days ago): 
* [#6191](https://github.com/gammapy/gammapy/pull/6191) Backport PR #6189 on branch v2.0.x (Replace deprecated keyword by RADESYSa) - Lumberbot (aka Jack)
* [#6190](https://github.com/gammapy/gammapy/pull/6190) Backport PR #6182 on branch v2.0.x (Correct PhaseCurveTemporalModel integration bug) - Lumberbot (aka Jack)
* [#6189](https://github.com/gammapy/gammapy/pull/6189) Replace deprecated keyword by RADESYSa - Leander Schlegel
* [#6188](https://github.com/gammapy/gammapy/pull/6188) Allow for RunTime warning in NaN for test_pwn - Kirsty Feijen
* [#6182](https://github.com/gammapy/gammapy/pull/6182) Correct PhaseCurveTemporalModel integration bug - Régis Terrier

### issues opened last week (less than 8 days ago): 
* [#6195](https://github.com/gammapy/gammapy/issues/6195) Error from CompoundSpectralModel.evaluate() args for TemplateNDSpectralModel. - Tora T H Arnesen
* [#6192](https://github.com/gammapy/gammapy/issues/6192) Adjust `github_summary.py` to allow for only the generation of `Contributors` - Kirsty Feijen

 report created at 17/10/2025, 07:23:54
