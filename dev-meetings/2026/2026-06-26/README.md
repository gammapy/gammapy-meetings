# Gammapy Developer Meeting 
 * Friday, June 26, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information

- **New lead developer**: The main website has been updated to reflect Kirsty arrival.
- **Gammapy paper**: Sent to all co-authors with a deadline of **July 3rd** for comments. A couple of minor comments already received. Discussion around making the citation appear as "Gammapy team" in BibTeX/ADS — this is technically possible (as done by HESS and MAGIC collaborations). To be addressed after July 3rd.
- **Dark matter activity**: Alexandro is busy this week but will attend the dev call next week to present ongoing work and clarify direction.

## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

- Several unrelated test failures observed, traced to recent releases of **Astropy** (v8+) and **SciPy**, both breaking things:
  - SciPy broke observation clustering (a function was removed without deprecation warning).
  - Astropy v8 broke string formatting of catalogue entries.
- Workaround: pinned to previous versions for now; underlying issues still need fixing.
- The "dev versions" CI job (which should have caught this early) was set to `allow_failure` and apparently not monitored — needs investigation.
- **macOS-specific failure** on Kirsty's energy-dependent estimator PR: one value differs significantly (250 vs 190) on Python 3.13/3.14 with macOS latest. Cannot be reproduced locally. **Mac users are asked to run the branch locally to help debug.**

## Validation & benchmark

## Ongoing projects

### Map Dataset Downsampling 
- Katharina presented a PR to extend `MapDataset.downsample()` to support axes beyond spatial (energy true, energy reco, etc.).
- Key fixes included in the PR:
  - IRF map downsampling was incorrectly summing over energy true — now correctly averages.
  - For energy reco: sums; for spatial and energy true: averages.
- **Decision**: For now, only support **energy true** as an additional axis name; throw an explicit error for unsupported axes rather than silently doing nothing.
- Docstring needs a full rewrite (currently confusing).
- A second follow-up PR could address non-integer downsampling factors (leftover bins) — possibly via reprojection.
- PR remains a draft; tests for new axis behavior to be added.

### Region 0.12 Compatibility Issue (Gammapy 2.1)
- Fabio identified that Gammapy 2.1 specifies `regions >= 0.9` in `pyproject.toml`, meaning a fresh install today picks up `regions 0.12`, which breaks things (private function import removed without deprecation).
- The dev version is unaffected, and 2.2 will not have this problem.
- **No 2.1.1 release planned**, but documentation/environment file should warn users to pin `regions < 0.12` (and possibly SciPy/Astropy versions).
- **Lesson**: avoid importing private functions from external libraries.

### Multi-Region Analysis PR (`#6006`)
- Atreyee updated this long-standing PR; it is now ready for review.

## Any other business

- **Gammapy paper links**: Consensus to update paper references from 2.0 → **2.0.1** (minor bug-fix release); no need to explicitly mention bug fixes in the paper text.
- **Nested model TS evaluation bug** (found at CTA school): Kirsty has not had time to investigate yet; delta-TS was not varying as expected when comparing point source vs. extended source models with an Asimov dataset. Still on the to-do list.
- **User statistics badge** (inspired by Astropy's GitHub README): Fabio found a Python script (requires ADS + GitHub tokens) that auto-generates citation/PR/contributor stats as a PNG via CI, see [astropy repo_stats](https://github.com/astropy/repo_stats). A **low-priority issue** will be created to track implementing something similar for Gammapy.
- **LACT using GammaPy**: A PhD student's seminar confirmed Gammapy is being used for LACT source simulations (SS 433 study). 

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6745](https://github.com/gammapy/gammapy/pull/6745) Gamma Ray Line spectra implementation - None
* [#6744](https://github.com/gammapy/gammapy/pull/6744) Dark Matter module - Refactor and test enhance of the spectra class - None
* [#6743](https://github.com/gammapy/gammapy/pull/6743) Dark Matter module - Enhancement of the JFactor calculation - None
* [#6741](https://github.com/gammapy/gammapy/pull/6741) Dark Matter module - Implementation of the log-normal nuisance approach. - None
* [#6740](https://github.com/gammapy/gammapy/pull/6740) Fix `MapDataset.downsample` and `IRFMap.downsample` - Katharina Egg
* [#6735](https://github.com/gammapy/gammapy/pull/6735) ASDF serialization for `MapAxes` class - Basmala Hekal
* [#6731](https://github.com/gammapy/gammapy/pull/6731) ci: run tests using pixi - Natthan Pigoux

### PRs merged last week (less than 8 days ago): 
* [#6742](https://github.com/gammapy/gammapy/pull/6742) Backport PR #6734 on branch v2.0.x (Fix docstring of make_concentric_annulus_sky_regions) - Lumberbot (aka Jack)
* [#6738](https://github.com/gammapy/gammapy/pull/6738) Backport PR #6737 on branch v2.0.x (Pin dependencies to fix CI) - Lumberbot (aka Jack)
* [#6737](https://github.com/gammapy/gammapy/pull/6737) Pin dependencies to fix CI - Régis Terrier
* [#6734](https://github.com/gammapy/gammapy/pull/6734) Fix docstring of make_concentric_annulus_sky_regions - Fabio Acero
* [#6723](https://github.com/gammapy/gammapy/pull/6723) Refactor of Spectra class and test - None
* [#6722](https://github.com/gammapy/gammapy/pull/6722) ASDF serialization for `TimeMapAxis`  and `LabelMapAxis` classes - Basmala Hekal

### issues opened last week (less than 8 days ago): 
* [#6746](https://github.com/gammapy/gammapy/issues/6746) astropy region 0.12 causing issues in gammapy/utils/regions.py - Fabio Acero
* [#6739](https://github.com/gammapy/gammapy/issues/6739) `MapDataset.downsample` and `IRFMap.downsample` only work for spatial and energy axes - Katharina Egg
* [#6736](https://github.com/gammapy/gammapy/issues/6736) CI issues with astropy 8.0 and scipy 1.18 - Régis Terrier
* [#6733](https://github.com/gammapy/gammapy/issues/6733) Docstring update in make_concentric_annulus_sky_regions - Fabio Acero
* [#6732](https://github.com/gammapy/gammapy/issues/6732) Pin os version explicitely instead of `latest` - Daniel Morcuende

 report created at 26/06/2026, 10:25:34
