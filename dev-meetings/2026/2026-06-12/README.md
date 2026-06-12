# Gammapy Developer Meeting 
 * Friday, June 12, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information


## [Open issues](https://github.com/gammapy/gammapy/issues)

- Sensitivity estimator NaN failures [#6719](https://github.com/gammapy/gammapy/issues/6719) 
  The SensitivityEstimator intermittently produces NaNs in v2.1 when predicted counts are negative. Likely related to minimizer bounds not being well-defined
  in that regime. Quentin will investigate.
- Dataset read/write backward compatibility issue [#6716](https://github.com/gammapy/gammapy/issues/6716)
  Tomas reported that datasets written with v2.1 cannot be read with v2.0, due to the switch from OGip to GADF format as default.
  This is a known issue with no clean fix yet, linked to the heterogeneous nature of Datasets. Régis flagged it for v2.2 and noted a clear decision is needed.

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

- Sherpa build dependencies PR [#6717](https://github.com/gammapy/gammapy/pull/6717)
  A PR adding bison, flex, and make to the dev environment was discussed. These are needed to compile Sherpa from source (no Numpy 2.x wheels on PyPI). Consensus: this is primarily a
  local reproducibility improvement, not a CI concern. The broader question of whether to maintain Sherpa as an optional backend was raised — it appears rarely used, and may be worth
  deprecating long-term.
  
## Validation & benchmark

- Next week: Discussion on validation and checks needed for the v2.2 in view of CTAO CDR.

## Ongoing projects
- Metadata serialization PR (Marie) [#6720](https://github.com/gammapy/gammapy/pull/6720)
  Marie presented a draft PR addressing metadata (Creator) serialization across serializable products.
  The proposal introduces a helper function add_creator_metadata to centralize metadata handling, starting with IRF products. Discussion points:
  IRFs were not originally considered Gammapy-generated products, but their growing use in I/O justifies adding metadata support. 
  Régis suggested keeping the scope focused on IRFs for now, and deferring a more general metadata-passing mechanism (supporting arbitrary metadata objects beyond Creator) to a future PR.
  The to_hdu_list signature should not receive the Creator as an option yet, to avoid inconsistency.
  Tests for metadata serialization should live alongside the product's own tests, not in a separate centralized test file — unit tests cover
  the metadata object itself, integration tests cover per-product serialization compliance.
  
- MapAxes ASDF serialization PR (Basmala) [#6706](https://github.com/gammapy/gammapy/pull/6706)
  Basmala confirmed the PR now only contains MapAxes, with TimeMapAxes deferred to a separate PR. Agreement to merge once the converter file is renamed to reflect axes-only scope.
  Converters for axes, WCS maps, and region maps should each live in their own file within the ASDF I/O folder.

- Unbinned analysis draft PRs - raised by Quentin
  Several draft PRs from Guillaume were reviewed. Key concerns:
    - The unbinned geometry PR creates one axis per photon, which was deemed architecturally problematic.
    - The statistics PR (defining a new stat class) was considered the most mergeable in isolation. (Quentin)
    - The overall PRs lack a concrete science use case driving the implementation, and the design choices are not always well-motivated (Tomas)
  Decision: a dedicated meeting should be organized (Tomas to schedule, likely after the summer) to agree on a clear design and implementation order before further review effort is spent.

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6720](https://github.com/gammapy/gammapy/pull/6720) Check if serialized product contains creator metadata - Marie-Sophie Carrasco
* [#6717](https://github.com/gammapy/gammapy/pull/6717) Fix the dev environment for the sherpa build - Bruno Khélifi

### PRs merged last week (less than 8 days ago): 
* [#6718](https://github.com/gammapy/gammapy/pull/6718) Fix badges in the README - Bruno Khélifi
* [#6715](https://github.com/gammapy/gammapy/pull/6715) Backport PR #6685 on branch v2.0.x (Fix default behavior of sum_over_energy_groups=False case in ExcessMapEstimator) - Lumberbot (aka Jack)

### issues opened last week (less than 8 days ago): 
* [#6719](https://github.com/gammapy/gammapy/issues/6719) Sensitivity estimator returning NaN value in v2.1 and dev - Fabio Acero
* [#6716](https://github.com/gammapy/gammapy/issues/6716) Gammapy 2.01 cannot read dataset written with gammapy 2.1 - Tomas Bylund

 report created at 12/06/2026, 11:04:38
