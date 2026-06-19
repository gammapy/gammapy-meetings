# Gammapy Developer Meeting 
 * Friday, June 19, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information

### Team News
- Kirsty has been approved and welcomed as the team's 4th lead developer (following Axel's departure)

### CTAO Science Data Challenge (Fabio P.)

- Simulations for the North site working well in Gammapy, no bugs found
- South site simulations delayed (~Sept/Oct target) due to missing IRFs and schedule slippage
- Metadata model discussion: the CTAO data products metadata document (led by Karl/data products group) is not yet released due to pending comments
  (incl. from David, related to DL3/DL5 consistency). Fabio's simulated datasets already incorporate updated metadata from prior feedback,
  but this needs to feed back into the official document
  - Bruno raised concerns about being out of the loop on document versions and a possible DL3/DL5 inconsistency he noticed
  - Matthias explained the document process was run in a non-ideal order (test data released before doc finalized) due to deadline pressure
- Plan: provide another subsample with updated metadata for cross-checking before final production
- Discussion on whether a tutorial is needed for DL3 simulation scripts
  — Régis noted existing single-observation DL3 production tutorials likely already cover the main need; broader scheduling-based simulation seen as added complexity not currently necessary

### gammapy-mwl status (Fabio A. & Katharina)

- Closed many issues; CI restored and now includes Sherpa testing (compatible with Sherpa 4.18)
- Test datasets loading correctly across multiple telescopes
- Mireia's tabulated absorption model PR is the last major blocker before a v0.1 release (targeted for summer) — goal is to allow non-thermal analysis entirely without requiring a Sherpa install
- Katharina found a bug: multi-component Sherpa model import doesn't correctly handle models (like APEC) that return integrated flux rather than point flux — needs bin-width correction; she opened an issue
- Bruno emphasized the need for proper references/citations for absorption models and test datasets (e.g., eROSITA data lacks a clear license)
- Régis suggested keeping the script that generates the absorption table (from Sherpa models) for traceability
- Notable achievement: full forward-folding fit combining eROSITA, Fermi, and H.E.S.S. data with Nautilus nested sampling, ~19 free parameters, running in about a day on a cluster; with Naima alone, ~4 hours on 32 cores
- Katharina advocated for promoting Gammapy's sampling/fitting capabilities (vs. BXA/UltraNest in X-ray community) as a draw for X-ray users, citing Gammapy's backend-agnostic design as an advantage

### Gammapy Paper (Kirsty)

- writing complete, most comments addressed; draft to be circulated to co-authors next Wednesday, with submission to A&A targeted for the second week of July
  
## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

- Natthan is testing Pixi as an alternative to tox/conda for CI environments (replicating earlier work done with uv);
  - pixi.lock would be committed to git, updated only when dependencies change
- Régis asked about dataset caching as a related performance improvement — unclear if already implemented
- Broken CI on macOS only: catalog docstring/string-formatting tests failing, likely tied to the macOS 14 runner image change.
- Same/similar platform-specific failures reported independently by Kirsty (energy-dependent feature PR) and Basmala — confirmed to be a systemic macOS CI issue, not isolated bugs
  
## Validation & benchmark

### Validation Framework (Régis)

- Proposing to extend validation beyond "reproduce published results" toward statistical coverage testing:
  - running Monte Carlo simulations to confirm that estimators (flux points, parameter errors, TS maps, sensitivity) achieve correct statistical coverage (e.g., 1σ interval contains truth ~68% of the time)
- Already has a working prototype (extended to 3D case) showing under-coverage in low-count regimes (consistent with findings in the Gammapy 2.0 paper)
- Discussion on producing visual/trend reports tracked across releases (possibly tied to version tags)
- Daniel asked whether this could be tied to release tagging — currently only run on dev version
- Bruno raised a related case: estimating cutoff energy/curvature parameters where parabolic error estimation may be insufficient
- Matthias (CTAO) strongly endorsed continuing this work, seeing value beyond CDR needs into general acceptance testing

- Discussed extending validation to:
  - DL3→DL4 step (not currently tested for coverage)
  - simulated CTAO SDC data (not just synthetic Gammapy simulations)
  - Systematic effects / IRF uncertainties — no generic framework yet exists for perturbing IRFs;
    - Fabio Acero suggested a nuisance-parameter + sampling approach to propagate IRF systematics into posteriors
    - Quentin suggested CTAO's DPPS team could provide IRF samples (e.g., PSF realizations) directly rather than Gammapy regenerating them
   
      
## Ongoing projects

### Dark Matter Module

- Increasing number of PRs/issues from the dark matter contributor group
- Régis: long-term, this could evolve into an affiliated package (e.g., "gammapy-dark-matter"), easing maintenance/review responsibility
— plan to invite them to present their work

### ASDF Serialization (Basmala — GSoC)

- Map axis class serialization merged; TimeMapAxis/LabelMapAxis PR in progress
- Next: NDMap class serialization
- Blocker: region serialization isn't supported yet in ASDF — needs a design discussion before serializing Region/RegionNDMap objects
- Goal: full map serialization to ASDF by mid-July

## Any other business

- Fermipy/Fermitools numpy compatibility: Fabio A. is working on PRs to update Fermitools/Fermipy to NumPy 2.x (currently pinned <2.0 and Python 3.9), to prevent Gammapy/Fermipy dependency divergence as Gammapy drops NumPy <2 support
- A bizarre "70 petabytes of memory" error found by Tomas traced by Quentin to a runaway flux value in event sampling, not a real infrastructure issue
A light curve / temporal model bug currently being retested after a fix from Quentin

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6731](https://github.com/gammapy/gammapy/pull/6731) ci: run tests using pixi - Natthan Pigoux
* [#6723](https://github.com/gammapy/gammapy/pull/6723) Refactor of Spectra class and test; and inclusion of the Gamma Ray Line approach - None
* [#6722](https://github.com/gammapy/gammapy/pull/6722) ASDF serialization for `TimeMapAxis`  and `LabelMapAxis` classes - Basmala Hekal

### PRs merged last week (less than 8 days ago): 
* [#6721](https://github.com/gammapy/gammapy/pull/6721) Fix bug in `FluxCollectionEstimator` for extra frozen models - Kirsty Feijen
* [#6706](https://github.com/gammapy/gammapy/pull/6706) ASDF serialization for  `MapAxis`  class - Basmala Hekal
* [#6589](https://github.com/gammapy/gammapy/pull/6589) Add script for getting contributors - Atreyee Sinha

### issues opened last week (less than 8 days ago): 
* [#6730](https://github.com/gammapy/gammapy/issues/6730) ASDF: Implementation of Phase 3  WcsNDMap, HpxNDMap and RegionNDMap - Basmala Hekal
* [#6729](https://github.com/gammapy/gammapy/issues/6729) ASDF: Investigate Region serialization strategy and implement RegionGeom - Basmala Hekal
* [#6728](https://github.com/gammapy/gammapy/issues/6728) ASDF: Implementaion of phase 2 WcsGeom and HpxGeom classes - Basmala Hekal
* [#6727](https://github.com/gammapy/gammapy/issues/6727) Dark Matter Module - JFactor nuisance - None
* [#6726](https://github.com/gammapy/gammapy/issues/6726) Dark Matter Module - Study the connection with CLUMPY - None
* [#6725](https://github.com/gammapy/gammapy/issues/6725) Dark Matter Module - Check if last energy point is available on CosmiXs - None
* [#6724](https://github.com/gammapy/gammapy/issues/6724) Dark Matter Module - Include HDMSpectra as a spectra source - None

 report created at 19/06/2026, 11:27:02
