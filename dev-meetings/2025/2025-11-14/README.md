# Gammapy Developer Meeting 
 * Friday, November 14, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 
Katarina Egg (KE), Kirsty Feijen (KF), Aritra Gupta (AG), Daniel Morcuende (DM), Quentin Remy (QR), Atreyee Sinha (AS), Régis Terrier (RT)

# Agenda
## General information
- next week several dark matter package users will attend and present their plans
- towncrier PR has been merged. Now we need to ensure it is working. And also to include any missing fragments [#6173](https://github.com/gammapy/gammapy/pull/6173)
  - All changes don't have their fragments yet. Need to add them.
  - Must separate bugs from features to allow proper backporting.
- Decision to go for the v2.0.1 bugfix release on Dec 15. Meeting planned at 10 am CET.
  
## Open issues

## Bugs
- Sorting bugs for the coming bugfix.
- Discussion about [#6194](https://github.com/gammapy/gammapy/pull/6194).
  - The role of the `SafeMaskMaker` is discussed. It can protect agianst the issue, but this might depend on the order of calls to observations
  - Should `DatasetsMaker` skip silently an observation outside geometry or fail? Currently list should have the same size to perform re-ordering of Datasets in multi-rpocessing.
  
## Documentation

* small PR from BK [#6213](https://github.com/gammapy/gammapy/pull/6213), but that is all

## DevOps
- pre-commit: now that we apply it only on modified files, we need a monthly check. Should it open a PR with the changes? See issue [#6219](https://github.com/gammapy/gammapy/issues/6219)
  
## Validation & benchmark

* KF is working on this [#6192](https://github.com/gammapy/gammapy/issues/6192) and should have a PR today/next week

## Ongoing projects
- Data model and format separation: ObservationTable PR is now merged. Protoype PR is closed.
  
## Any other business
- 
# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6213](https://github.com/gammapy/gammapy/pull/6213) Add a link towards the `npred` computation into the stats user-guide page - Bruno Khélifi
* [#6211](https://github.com/gammapy/gammapy/pull/6211) Multiple OFF regions in `makers.make_theta_squared_table` - Fabio PINTORE

### PRs merged last week (less than 8 days ago): 
* [#6216](https://github.com/gammapy/gammapy/pull/6216) Backport PR #6215 on branch v2.0.x (Solve CI fails caused by new iminuit and pytest version) - Lumberbot (aka Jack)
* [#6215](https://github.com/gammapy/gammapy/pull/6215) Solve CI fails caused by new iminuit and pytest version - Régis Terrier
* [#6214](https://github.com/gammapy/gammapy/pull/6214) Backport PR #6130 on branch v2.0.x (Add towncrier) - Lumberbot (aka Jack)
* [#6170](https://github.com/gammapy/gammapy/pull/6170) Introduce ObservationTableReader and Converter between GADF and internal format - Leander Schlegel
* [#6130](https://github.com/gammapy/gammapy/pull/6130) Add towncrier - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6212](https://github.com/gammapy/gammapy/issues/6212) Add ExclusionMask class for provenance tracking - Tomas Bylund

 report created at 14/11/2025, 07:24:20
