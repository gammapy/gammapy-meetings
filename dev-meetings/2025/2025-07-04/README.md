# Gammapy Developer Meeting 
 * Friday, July 04, 2025, at 2 pm (CET) - 15:14 pm
 * Gammapy Developer Meeting on Zoom (direct link on Slack)
 * Attendees: Régis Terrier (R.T.), Atreyee Sinha (A.S.), Tomas Bylund (B.S.), Samantha Wong (S.W.), Katharina Egg (K.E.), Mireia Nievas Rosillo (M.N.R.), Leander Schlegel (L.S.)

# Agenda

* Time for codefreeze (branch that contains v2, stop introducing features):   
AS: Before September, R.T.: Decide on time next week. Initially next Friday, prob. postponed.

* Contrib. Samantha Wong (S.W.):
RT: Tutorial content fine, move new function to utils.regions. 
SW: Could make function flexible, but needed or better specific? 
RT: Not decided if instrument specific functions into GP, so far not. Rely on regions for the function instead of utils. Extract_bright_star_region_list? 
SW: Try to implement it today!
A.S. question to R.T. regarding this: 
S.W.: Regular exclusion code (notebook), extra function. For crab scenario very bright star falls in region.
Try up to finish everything today in order for codefreeze.

## Information

## Recurring items

R.T.: Did we assign someone for recurring items yet?

### Open issues

1. Issue: `EnergyDependentEstimator` test class not properly initialized, corrected by A.S., merged today by R.T. 
2. Issue: Deprecation, R.T.: PR already open for deprecation, still work todo in this PR -> but issue can be removed.
3. Issue: Repetitive wording of recurring exercises, A.S. did PR to remove this section. -> can be closed.
4. Issue: TSMapEstimator failing, Q.R. open PR to solve it, wait for Lauras feedback. A.S. tested it, Q.R. iterated, seems to work -> R.T. Wait for Lauras confirmation.
5: Issue [#5948](https://github.com/gammapy/gammapy/issues/5948) : already discussed, not relevant for now

### Bugs

A.S. made list showing the status. Question regarding which bugs to fix dependent on label, R.T. proposes to postpone [#5549](https://github.com/gammapy/gammapy/issues/5549) since simulations for data challenge should take place in first part of 2026, thereby solve later ok. A.S. asks Fabio to confirm.

BUG [#5783](https://github.com/gammapy/gammapy/issues/5783)
T.B.: Standard flux units? R.T. For plotting yes, but not for writing table. -> solution to add it here, T.B. assigned.

BUG [#5906](https://github.com/gammapy/gammapy/issues/5906) Negative models/amplitudes and flux points
A.S.: Open PR with warning if index is negative, for now. R.T.: Alternative, evaluate spectral model of interest at center of energyrange to check if pos. or neg.

R.T.: On good track, just check when to solve, next week or later.

### Documentation

R.T.: Documentation PR merging will take a lot of time -> assign PRs to different people. Assigned is not the person opening the PR, but a reviewer checking that everything works (CI, etc) and merges in the end.

Assignees:
- "Tutorial cleanup" parts 1,2,3 (#5966,#5967,#5968): A.S.
- "Fix for #5943" (#5943): R.T.
- "simple fix to problem with EventList printing" (#5923) :A.S. (Issue discussed with R.T., T.B.)
- "Add tutorial for non-detected sources" (#5969) : R.T.
- "Energy edges instead of center for aeff-max in SafeMaskMaker" (#5960): T.B.
- ! "Adapt tutorial order" (#5949) -> postponed to assign!
- "Tutorial setup command line option" (#5941): R.T.
- "ci: allow to ci to skep ci step using PR labels" (#5938): R.T.
- "Update of the user guide documentation of Modeling and Fitting" #5936 :T.B. 

- Issue? : A.S.
(corresponding PR from R.T. discussed in more detail)

- Fit Statistics penalty: a decision must be taken here. do we merge?
- DM Issue -> postponed. A.S.: Colleague could maybe do PR for it, maybe for v2.1.

### DevOps

- nothing specific for now

### Validation & benchmark

- nothing specific for now

### Ongoing projects:
    - sensitivity: tutorial is missing. IS it required for v2.0. Do we postpone?
    - HLI: What can go in, what do we postpone for later?
    - MWL

## Any other Business

#Adding people on slack
A.S.: How to add people on Slack? R.T.: What could be the principle? A.S.: Someone from GP needs to invite. R.T.: Alternative with email address to write to for being added? Create contact-address for GP. A.S. agrees. R.T.: Discuss with B.K.

## Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#5969](https://github.com/gammapy/gammapy/pull/5969) Add tutorial for non-detected sources - Atreyee Sinha
* [#5968](https://github.com/gammapy/gammapy/pull/5968) Part 3 - Tutorial cleanup - Kirsty Feijen
* [#5967](https://github.com/gammapy/gammapy/pull/5967) Part 2 - Tutorial cleanup - Kirsty Feijen
* [#5966](https://github.com/gammapy/gammapy/pull/5966) Part 1 - Tutorial cleanup - Kirsty Feijen
* [#5965](https://github.com/gammapy/gammapy/pull/5965) fix typo in makers tutorial - Fabio Acero
* [#5964](https://github.com/gammapy/gammapy/pull/5964) Fix for Issue #5943 - Leander Schlegel
* [#5961](https://github.com/gammapy/gammapy/pull/5961) Adding description to peek - Kirsty Feijen
* [#5960](https://github.com/gammapy/gammapy/pull/5960) Energy edges instead of center for `aeff-max` in `SafeMaskMaker` - Kirsty Feijen
* [#5959](https://github.com/gammapy/gammapy/pull/5959) Adapt SafeMaskMaker docstring - Kirsty Feijen
* [#5958](https://github.com/gammapy/gammapy/pull/5958) Fix TSmapEstimator pad_width - Quentin Remy
* [#5957](https://github.com/gammapy/gammapy/pull/5957) Fix  #5951 - Atreyee Sinha
* [#5956](https://github.com/gammapy/gammapy/pull/5956) Fix tests of EnergyDependentMorphologyEstimator - Atreyee Sinha
* [#5954](https://github.com/gammapy/gammapy/pull/5954) Separate internal Eventlist data model from gadf format - Régis Terrier
* [#5949](https://github.com/gammapy/gammapy/pull/5949) Adapt tutorial order - Kirsty Feijen

### PRs merged last week (less than 8 days ago): 
* [#5963](https://github.com/gammapy/gammapy/pull/5963) Bump OpenAstronomy/github-actions-workflows from 1 to 2 - None
* [#5962](https://github.com/gammapy/gammapy/pull/5962) Bump stefanzweifel/git-auto-commit-action from 5.2.0 to 6.0.1 - None
* [#5953](https://github.com/gammapy/gammapy/pull/5953) Fix sampler tests - Quentin Remy
* [#5894](https://github.com/gammapy/gammapy/pull/5894) Adapt plot function default labels - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#5955](https://github.com/gammapy/gammapy/issues/5955) `test_energydependentmorphology.py` not getting executed during pytest - Atreyee Sinha
* [#5952](https://github.com/gammapy/gammapy/issues/5952) Is the deprecation warning in Observation.create supposed to be there? - Kirsty Feijen
* [#5951](https://github.com/gammapy/gammapy/issues/5951) Repetitive wording of "Exercises" in Spectral Analysis tutorial - Pierre Pichard
* [#5950](https://github.com/gammapy/gammapy/issues/5950) TSMapEstimator fails for some values of sigma with using a GaussianSpatialModel - Laura Olivera-Nieto
* [#5948](https://github.com/gammapy/gammapy/issues/5948) Check and update dependencies automatically - Daniel Morcuende

 report created at 04/07/2025, 07:26:06
