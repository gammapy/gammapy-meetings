# Gammapy Developer Meeting 
 * Friday, July 17, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Régis Terrier, Bruno Khélifi, Daniel Morcuende (CTAO), Quentin Remy, Basmala Hekal, Alex Cerviño, Maxime Regeard, Katharina Egg, Atreyee Sinha, Matthias Fuessling (CTAO), Maxime Regeard.

# Agenda

## General information

### CTAO data volume calculations
- Daniel asked the team to review CTAO's data volume calculation notes and check whether a new SDC dataset version resolved previously raised comments. - Régis noted Marie had run a full analysis on the data with no major issues reported, but metadata should still be checked. Bruno flagged IRF
  (instrument response function) smoothness as something to verify, though he'll be traveling to a conference and can't guarantee bandwidth. Régis aimed to give feedback on both the data volume document and the dataset by mid-next-week.

### Next Gammapy user call
- Tentatively planned for September/early October, timed around the Gammapy 2.0 paper release — potential demo topics include MCMC sampling vs. minimization paths and upper-limit handling.
  
## Validation & benchmark

### Science use case validation/verification framework
- Régis is starting a new part of the Gammapy benchmark/validation repository focused on science use case verification (as opposed to unit tests) — e.g. flux point coverage, isolated source detection/characterization, transient fitting. The approach: simulate/sample data many times, run the analysis workflow, and check the resulting distributions (e.g. pull distributions) fall within expected statistical bounds. He showed a draft branch/PR with a working example (isolated source detection) and noted the tests were largely written by an AI coding assistant, which sped things up considerably. Open question for the group: is this the right way to structure and automate this kind of validation. To be discussed further, possibly next week.

## Ongoing projects

### ASDF serialization (Basmala Hekal)
- Basmala demoed her work serializing Gammapy Map objects (WCS and HpxNDMap) to ASDF format, including metadata, geometry, units, and Astropy quantities/time objects, with support for compressing large arrays into binary blocks. Open PRs cover WCSNDMap and HpxNDMap serialization. HEALPix partial-sky maps required extra care due to GADF convention subtleties. Quentin asked whether it could read FITS files not originally written by Gammapy — Basmala believes yes, since the WCS/FITS serialization already exists in ASDF. Next step: serializing higher-level objects (map datasets).

### Dark Matter
- Alex : no major blockers, several PRs pending review from others; a single unified class for annihilation and decay cases is planned but will likely wait until after the summer break due to time constraints.
- General agreement to finish reviewing and merge pending PRs progressively to avoid overlapping changes.

### Add a function to rescale a dataset for a new livetime 
- [6464](https://github.com/gammapy/gammapy/pull/6464)
- Atreyee raised handling of "rescaled" on-off datasets (e.g. rescaling Crab background runs for MAGIC proposals) and where lifetime/exposure updates should live.
- Consensus leaned toward a helper function in dataset.utils rather than a dataset method, for discoverability without accidental misuse.

### New sensitivity estimator
- Add a joint sensitivity estimator [#6758](https://github.com/gammapy/gammapy/pull/6758) (Atreyee)
- The new sensitivity estimator now agrees well with the old one in the significance-dominated regime once Asimov dataset generation for on-off data was fixed; open question is how to handle the background/low-high energy regimes and whether joint (multi-dataset) sensitivity estimation needs new statistical criteria (e.g. minimum gamma-ray counts summed across datasets vs. per-dataset).
- Bruno argued the differential sensitivity curve is essential for spectral measurement use cases, while the integral sensitivity curve remains useful for simple detection questions.
- Régis suggested handling background systematics by sampling a prior on background normalization and generating an envelope of sensitivity curves, and proposed testing this approach for at least the background term.
- Discussion closed with Atreyee planning to continue this work.
  
## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

### Dev environment cleanup
- Discussion of ongoing environment/versioning headaches (Sherpa and NumPy version conflicts most often cited). Ideas raised:
   - Moving toward a more modern environment/package manager (uv or pixi) instead of conda, per an open request from Natthan that still needs testing/decision.
   - Keeping the dev environment spec minimal (only packages not already in pyproject.toml) so pyproject.toml remains the single source of truth for version constraints.

### Sherpa backend support
- Debate on whether to keep supporting Sherpa as a fitting backend.
- Pros raised: Katharina noted Sherpa handles complex multi-component X-ray models better in some multi-wavelength cases.
- Cons: it doesn't compute a covariance matrix, limiting its usefulness (a past user was frustrated by getting no error bars).
- Consensus: open a broader discussion/issue and ask the general user community (and at an upcoming user call) whether people rely on non-default backends, since usage data is currently lacking.
  
## Any other business

### License / documentation policy
- Maxime raised whether license headers should also appear in documentation files, not just source code (following the recently merged automated license-line check).
- Bruno noted there are effectively two categories — code (BSD-3-Clause) and documentation/website content — that need separate, clearly stated policies, possibly via a short "PIG", similar to how a past organizational roadmap was documented.

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6791](https://github.com/gammapy/gammapy/pull/6791) ASDF serialization for HpxNDMap class - Basmala Hekal
* [#6790](https://github.com/gammapy/gammapy/pull/6790) ASDF serialization for WcsNDMap class - Basmala Hekal
* [#6783](https://github.com/gammapy/gammapy/pull/6783) Dark Matter module: Part 2: Update Dark Matter OBSERVATION SIMULATION Tutorial - None
* [#6782](https://github.com/gammapy/gammapy/pull/6782) Dark Matter module: Part 1: Update Dark Matter BASICS Tutorial - None

### PRs merged last week (less than 8 days ago): 
* [#6789](https://github.com/gammapy/gammapy/pull/6789) Backport PR #6762 on branch v2.0.x (Fix MapDatasetOnOff._to_asimov_dataset to use nominal background instead of marginalised estimate) - Lumberbot (aka Jack)
* [#6785](https://github.com/gammapy/gammapy/pull/6785) Fix shape issues in the FluxCollectionEstimator - Quentin Remy
* [#6784](https://github.com/gammapy/gammapy/pull/6784) Harmonise SamplerResult output for Nautilus - Quentin Remy
* [#6773](https://github.com/gammapy/gammapy/pull/6773) License checker - Maxime Regeard
* [#6771](https://github.com/gammapy/gammapy/pull/6771) ASDF serialization for RegionGeom - Basmala Hekal
* [#6762](https://github.com/gammapy/gammapy/pull/6762) Fix MapDatasetOnOff._to_asimov_dataset to use nominal background instead of marginalised estimate - Atreyee Sinha
* [#6761](https://github.com/gammapy/gammapy/pull/6761) ASDF serialization for HpxGeom - Basmala Hekal
* [#6756](https://github.com/gammapy/gammapy/pull/6756) Add unit support to the violins plot used with the FluxCollection - Laura Olivera-Nieto
* [#6653](https://github.com/gammapy/gammapy/pull/6653) Add support for creating a `DataStore` from the results of a ivoa TapQurey - Tomas Bylund
* [#6620](https://github.com/gammapy/gammapy/pull/6620) Replace data by table in ObservationTableReader - Fabio PINTORE

### issues opened last week (less than 8 days ago): 
* [#6788](https://github.com/gammapy/gammapy/issues/6788) License statement policy - Maxime Regeard
* [#6787](https://github.com/gammapy/gammapy/issues/6787) CI not running correctly on dev deps - Atreyee Sinha
* [#6786](https://github.com/gammapy/gammapy/issues/6786) Include scale density not only for the Milky Way - None
* [#6781](https://github.com/gammapy/gammapy/issues/6781) Add possibility to create the input flux model based on a mixing of several channels - Daniel Kerszberg
* [#6780](https://github.com/gammapy/gammapy/issues/6780) Single class for Annhilation and Decay cases - Daniel Kerszberg

 report created at 17/07/2026, 09:13:07
