# Gammapy Developer Meeting 
 * Friday, September 04, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

Attendees: 

# Agenda
## General information

## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

## Validation & benchmark

## Ongoing projects

### Dark Matter project Update

Reported by: Alex 

- Ongoing corrections/changes in PRs (mainly tutorials), driven by review feedback.
- One PR is merged; the larger one still needs changes.
- Additionally open PR from Julia regarding central-pixel handling in J-factor calculation — still under discussion.
- No major new developments since the last call; team was largely on summer holidays.
- The monthly DM sub-group meeting has not yet been organized. No date set yet.

### ASDF Serialization Update

Reported by: Basmala 

- Merged: Good Time Intervals (GTI) serialization.
- Currently open: IRFMap serialization PR.
- Remaining scope: FluxPoints, FluxPointsDataset, MapDataset/MapDatasetOnOff, and Models.

- Decisions taken:
  - Priority order agreed: MapDataset / MapDatasetOnOff → Models are the most important pieces (arguably more important than FluxPoint datasets).
  - For Models serialization: do not build a converter per model type (too many model types); instead, rely on generic dictionary-based serialization of models.
  - For the IRFMap PR: add at least one or two tests using WcsGeom in addition to the existing RegionGeom-only tests (not necessary for every geometry type, but at least one alternate geometry should be covered).


### [#6838](https://github.com/gammapy/gammapy/pull/6838) Catalog Deprecation Policy (2FHL / Fermi Catalogs)

- Discussion: Atreyee raised that the 4FHL PR also proposes removing/deleting the 2FHL catalog files outright, rather than deprecating them. This conflicts with standard deprecation practice (deprecate = keep code/files but warn; here files would be deleted, making the deprecation warning meaningless).

- Context raised: Gammapy does not support all historical catalog releases indefinitely, due to distribution size concerns.
  FHL catalogs have inconsistent characteristics across versions. A 5th FHL catalog is expected soon, and a new low-energy Fermi catalog is also in preparation.

- Decisions taken:
  - None finalized. The inconsistency needs resolving: if a catalog is marked deprecated, its underlying files must be kept (you cannot deprecate something you've deleted). To be discussed and decided within PR discussion.

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6838](https://github.com/gammapy/gammapy/pull/6838) [catalogs] Add Fourth Fermi-LAT Catalog of High-Energy Sources (4FHL) - Michele Peresano

### PRs merged last week (less than 8 days ago): 
* [#6836](https://github.com/gammapy/gammapy/pull/6836) Bump astral-sh/setup-uv from 9.0.0 to 10.0.1 - None
* [#6832](https://github.com/gammapy/gammapy/pull/6832) Add slack notification for failure of workflows - Kirsty Feijen
* [#6831](https://github.com/gammapy/gammapy/pull/6831)  ASDF serialization for GTI  - Basmala Hekal
* [#6830](https://github.com/gammapy/gammapy/pull/6830) ASDF serialization for Maps - Basmala Hekal
* [#6825](https://github.com/gammapy/gammapy/pull/6825) Unification of Dark Matter Spectral classes - Alexander Cerviño Cortínez

### issues opened last week (less than 8 days ago): 
* [#6837](https://github.com/gammapy/gammapy/issues/6837) ASDF serialization for MapDataset and MapDatasetOnOff classes - Basmala Hekal

 report created at 04/09/2026, 12:03:30
