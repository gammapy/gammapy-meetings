# Gammapy Developer Meeting 
 * Friday, July 24, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information

## [Open issues](https://github.com/gammapy/gammapy/issues)

### GADF float precision (DL3 products) [#6795](https://github.com/gammapy/gammapy/issues/6795)

- Karl found that CTAO test data is written as float64 instead of the GADF-mandated float32 (except time/event ID columns).
- Agreed Gammapy should enforce this strictly. Root cause: event lists are no longer in-memory objects that map 1:1 to the GADF format, so the old event-list checker validation was lost. 
- Marie is prototyping a Pydantic-based validation layer (separating I/O from data products, similar to the ASDF approach) to enforce header/metadata/column correctness — likely too much work for the 2.2 release but in progress.

### Elliptical shell model proposal [#6793](https://github.com/gammapy/gammapy/issues/6793)

- An APC intern (Elise) needs an elliptical shell model for her science case and has a working prototype.
- Discussion on whether to extend the existing shell model (adding ellipticity params, frozen/defaulted for backward compatibility) vs. creating a new dedicated model.
- Key concern: adding parameters changes the covariance matrix shape, breaking backward compatibility with saved fits (precedent: same issue occurred when lon/lat were added to the disk model). Possible work around by dropping off-diagonal covariance terms and reconstructing from errors — lossy and not ideal.
- Raised the broader question of a formal backward-compatibility policy for models (e.g., version-tied guarantees), and whether the covariance matrix serialization format itself should be revisited (possibly move away from plaintext, consider FITS or ASDF; store only free-parameter covariance and reconstruct full matrix from parameter freeze/thaw state on read).
  
## [Bugs](https://github.com/orgs/gammapy/projects/36)

- Kirsty flagged strange Asimov-dataset test failures (nonsensical ΔTS values) for an energy-dependent morphology test dataset — unresolved, Atreyee will investigate; test currently relies on a loosened tolerance due to cross-platform (Mac/Linux/Windows) inconsistencies, which the team agrees isn't a good long-term solution.

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

## Validation & benchmark

### CTAO CDR – science use case verification framework

- Régis presented a (partly AI-assisted) prototype for a science-case verification framework, generalizing the existing flux-point coverage validation into a standalone structure.
- Currently covers: flux point coverage/sensitivity, isolated source detection, transient characterization (fast-rise/exponential-decay light curve fitting), and source component separation (flux disentangling of two overlapping sources).
- Common structure: build observation → build dataset → build model → run workflow N times via multiprocessing → aggregate results into JSON → run pass/fail checks (e.g., pull distributions within expected sigma range) → tag as verified.
- Open questions raised by the team: is this maintainable long-term or a one-off CDR deliverable (possibly kept in a separate repo)? Which use cases are actually worth this level of verification (isolated source detection seen as low-value; energy-dependent morphology and flux collection seen as more valuable)? Should outputs include plots/visual explanations of what's being tested, not just pass/fail? Daniel suggested modeling it after other CTAO software verification approaches (tabulated use cases, steps, and pass criteria). No firm decision — team agreed to think it over given the short CDR timeline.

## Ongoing projects

### ASDF serialization: Region/WCS maps & serialization

- Basmala's region/WCS maps work has been merged; type conservation (Boolean vs integer maps) now works correctly through serialization.
- Remaining gap: region geometry doesn't currently round-trip DS9-format regions properly (metadata causes input→output mismatches).
- Proposed fix: strip metadata from region objects since Gammapy doesn't use it (though visual metadata for plotting styling might be worth keeping).
- 
## Any other business



### Plotter PIG
- agreed to mark as accepted and move to implementation (Atreyee to merge/mark accepted, double-check PIG numbering first).

### AI-generated PR / contribution policy

- Discussion of a low-effort AI-generated PR (bounding-box-to-region conversion bug for point/sky regions) that used a fragile try/except-based fix rather than a real solution; Atreyee noted she got several different explanations/answers from Claude when probing the same issue.
- Team decided: not mergeable as-is; ask contributor for a simpler, properly tested fix (avoid catching LinAlgError); Quentin will investigate a simpler patch himself and possibly close/replace the PR.
- Broader concern about rising volume of AI-assisted/"vibe-coded" contributions from people with no real connection to the project or field, contributing against the stated policy (must discuss with maintainers before opening a PR). Traced to an issue from a Debian packager (Ollie) who told another contributor to "just open a PR."
- Decisions: close this specific PR with an explanation; consider adding an AGENTS.md-style file defining coding/style/test conventions for AI agents? Consider an automated welcome/guidelines message for first-time contributors? Possibly revisit the authorship policy given it may be encouraging low-value PRs.

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6796](https://github.com/gammapy/gammapy/pull/6796) Fix SVD convergence error in RegionGeom._rectangle_bbox - Tanishq Jain
* [#6794](https://github.com/gammapy/gammapy/pull/6794) ASDF serialization for RegionNDMap class - Basmala Hekal

### PRs merged last week (less than 8 days ago): 
* [#6791](https://github.com/gammapy/gammapy/pull/6791) ASDF serialization for HpxNDMap class - Basmala Hekal
* [#6790](https://github.com/gammapy/gammapy/pull/6790) ASDF serialization for WcsNDMap class - Basmala Hekal
* [#6741](https://github.com/gammapy/gammapy/pull/6741) Dark Matter module - Implementation of the log-normal nuisance approach. - None

### issues opened last week (less than 8 days ago): 
* [#6795](https://github.com/gammapy/gammapy/issues/6795) Enforce GADF specs when writing simulated DL3 files - Daniel Morcuende
* [#6793](https://github.com/gammapy/gammapy/issues/6793) Add new shell spatial model - None
* [#6792](https://github.com/gammapy/gammapy/issues/6792) Fix problem with RegionGeomConverter in ASDF - Basmala Hekal

 report created at 24/07/2026, 09:24:51
