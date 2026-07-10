# Gammapy Developer Meeting 
 * Friday, July 10, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information

### MACE Experiment Update (Atreyee)
The MACE collaboration (Major Atmospheric Cherenkov Experiment) has contacted Atreyee about using Gammapy and is working toward DL3 production. Atreyee has prepared an on-off analysis tutorial for them and suggested it could also serve SDC/CTA requirements which aligns with the 2.2 roadmap goal of adding an on-off-specific tutorial (not using reflected-region background). Atreyee is also considering building a dedicated off/background maker tool.

### Gammapy-mwl (Fabio Acero)

- First release candidate for gammapy-mwl has been made, using GitHub's trusted-publisher mechanism for PyPI releases (rather than a manually managed token), which worked smoothly.
- Package is installable via `pip install gammapy-mwl` for testing.
- Still missing: README, documentation, and example notebooks — none currently exist. Plan is to build a directory of example Jupyter notebooks (spectrum loading, absorbed power-law/Naima fits) rather than a full Sphinx docs site, targeting completion before end of summer/September.
- Discussion on how to handle multi-wavelength test data (XMM, Chandra, ROSITA, Swift spectra), which aren't shipped with pip install. Options     considered: users clone the repo (~30MB), use their own data, or add an optional PyPI extras-style data package (à la Gammapy's optional dependencies). Fabio will look into feasibility.
- Plan to revive/consolidate the (currently non-functional) Gammapy recipes repository as a lightweight home for smaller examples/backup tutorials.

### 2.2 Release Timeline
- Originally targeted for October; realistically now aiming for November, accounting for a quiet August and a Gammapy school in early November that may further delay the release. ~40 open roadmap items remain (mixed priority); contributors were asked to review their assigned issues and update statuses.

## [Open issues](https://github.com/gammapy/gammapy/issues)

### Dependency Pinning & CI 
- A new issue [#6775](https://github.com/gammapy/gammapy/issues/6775) was raised connected to the regions package causing Gammapy 2.1's dev-dependency CI to fail, reviving the question of whether to pin upper bounds on dependency versions for releases.
- Consensus leaning toward pinning versions per release (e.g., cap NumPy/AstroPy at known-compatible versions) given Gammapy's ~6-month release cadence, revisiting the policy in ~5 years if needed.
- Root cause of the current CI failure: dev-CI tests weren't running with data before, so breaking changes went undetected; now that versions are pinned, AstroPy still isn't resolving to the intended constrained version (NumPy and SciPy pin correctly). The regions package likely needs to be added to the pinning constraints too. To be investigated before the 2.2 release see [#6787](https://github.com/gammapy/gammapy/issues/6787).

## Bugs

### Energy-Dependent Morphology Estimator PR (Kirsty's PR #6640)

- Atreyee, Maxime, and Quentin discussed test instability: significance (TS/sigma) values differ substantially across platforms (Mac vs. Windows vs. Linux) when using multiple datasets, traced to instability in the covariance matrix computed via MINUIT's approximate (Migrad) method rather than its explicit covariance routine.
- Discrepancy is more severe for larger delta-TS values; single-dataset tests pass fine, only the multi-dataset case fails.
- Suggestions raised: try MINUIT fit strategy 2 (didn't resolve it), check iteration/call counts between platforms, and — as a longer-term fix — use Asimov datasets for tests to get more numerically stable, reproducible reference values.
- Segued into a related question of making Gammapy's (currently private/internal) Asimov dataset utilities public, with documentation — Régis has a draft notebook and will propose an API update.

## Ongoing projects

### ASDF Serialization (Basmala, GSoC)

- RegionGeom WCS/HDU serialization merged. Key challenge: SkyRegion has no native ASDF/AstroPy serialization.
- Solution (agreed with Régis and Kirsty): serialize regions as DS9-format strings (as a list, to support compound regions), parsed back to SkyRegion on load. Tested round-trip for circle, point, and rectangle sky regions.
Régis noted this differs from the FITS approach (which serializes WCS + pixel region) but is a reasonable simpler alternative given the uncertain documentation quality of the DS9 format.
- Next steps: NDMap serialization, targeted before the GSoC mid-evaluation (July 24), followed by dataset and model serialization, aiming to have full map ASDF serialization working before end of month.

### Dark Matter Analysis Tutorials (Alex, with input from Daniel)

Alex presented three draft tutorials splitting up a previously monolithic one:
- Basics tutorial: covers dark matter spatial density profiles, J-factor/D-factor computation (annihilation vs. decay), spectral models (PPPC4, Cosmix, custom input files), and resulting flux maps. Régis raised a question about unit consistency between the spatial (J-factor, e.g. GeV²/cm⁵) and spectral (e.g. cm³/s/GeV) components; Daniel and Quentin clarified that Gammapy only requires the combined sky model to yield correct flux units — individual spatial/spectral factorizations can vary, similar to how diffuse-emission models split column density vs. emissivity.
- Data management tutorial: covers simulating with/without a signal, Asimov vs. Monte Carlo simulation, and 1D vs. 3D analysis approaches. Atreyee felt this content largely duplicates general (non-dark-matter-specific) Gammapy tutorials and suggested moving generic material into the main documentation, keeping only dark-matter-specific parts. Quentin suggested it could be useful for schools if trimmed. Alex agreed to review existing 1D/3D simulation tutorials to see what's genuinely missing before deciding what to keep.
- Full end-to-end analysis tutorial: simulates data, tests for a signal via likelihood ratio, computes upper limits (profile likelihood, single point or scanned over mass) or, if a signal is found, upper/lower limits — plus "Brazilian plot"–style sensitivity bands (1σ/2σ) via repeated realizations. Discussion points:

- Whether to use ParameterEstimator's (currently undocumented/internal) stat-scan option instead of manual profiling — Quentin noted it is exposed in the docs.
- One-sided vs. two-sided sigma-to-confidence conversion for upper limits needs clarifying in the tutorial.
- Runtime: the Brazilian-plot generation (many simulated realizations) is too slow for CI — agreed to precompute and embed as a static plot rather than running it live in the notebook.
- Atreyee asked whether this duplicates the new sensitivity estimator; Régis clarified it's methodologically different (distribution of expected upper limits vs. minimal flux for an N-sigma detection) — to be discussed further on the PR.
- Data: Alex needs to upload a signal-free dwarf-spheroidal-like simulated dataset to gammapy-data; Atreyee confirmed there's no licensing issue since it would be generated from CTA IRFs already in gammapy-data, and asked that the generation script be included alongside the output for reproducibility (Régis agreed).
- Quentin raised whether the tutorial's scope depends on an unresolved architectural decision: whether dark matter functionality stays inside core Gammapy or moves to a separate package (e.g. gammapy-multiwavelength-style sub-package). If separate, the tutorial can stay fully self-contained; if it stays in core, there's more duplication to resolve with existing tutorials.
- This full analysis tutorial is understood to be a requirement for the SDC (per David Green), so it's expected to be included for the 2.2 release regardless, with restructuring/relocation to be revisited later.
- Separately, Quentin questioned whether Alex's dark-matter regression/validation test PR belongs in Gammapy proper or in a gammapy-benchmarks/validation repository, since it doesn't add coverage but instead validates that a full analysis yields physically sensible results. Régis suggested it's a good candidate for a future validation, potentially also relevant to CTA use-case validation more broadly — to be discussed further on the PR.
- General discussion also touched on whether "select nested models" functionality is well-documented, with a suggestion to potentially add a dedicated hypothesis-testing notebook (deferred given Gammapy already has ~50 tutorials — Régis flagged a broader need to reassess tutorial scope/documentation strategy).

### License Checker PR (Maxime)
Adds an automated license-header check, currently run as a pre-release step (not full CI/pre-commit) and scoped to Python files that are git-tracked (updated per Bruno/Patrick's review). Open question of whether to extend the check to documentation files (.rst, etc.) — unresolved; no clarity yet on whether docs currently carry license headers. PR considered ready to merge; a follow-up issue may be opened regarding documentation licensing.

## Any other business

- Régis: away until ~July 24, back end of August.
- Quentin: around for the whole summer.
- Atreyee: around as well.
- Smaller-committee meetings expected to continue through summer; next call planned for the following week.

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6785](https://github.com/gammapy/gammapy/pull/6785) Fix shape issues in the FluxCollectionEstimator - Quentin Remy
* [#6783](https://github.com/gammapy/gammapy/pull/6783) Dark Matter module: Updated Dark Matter tutorial v2.1 of Gammapy - OBSERVATION SIMULATION Tutorial - None
* [#6782](https://github.com/gammapy/gammapy/pull/6782) Dark Matter module: Updated Dark Matter tutorial v2.1 of Gammapy - BASICS Tutorial - None
* [#6779](https://github.com/gammapy/gammapy/pull/6779) Inclusion of regression test for a Dark Matter Module - None
* [#6777](https://github.com/gammapy/gammapy/pull/6777) Dark Matter module documentation upgrade - None
* [#6774](https://github.com/gammapy/gammapy/pull/6774) Dark Matter module: Updated Dark Matter tutorial v2.1 of Gammapy - Full analysis Tutorial - None
* [#6773](https://github.com/gammapy/gammapy/pull/6773) License checker - Maxime Regeard
* [#6771](https://github.com/gammapy/gammapy/pull/6771) ASDF serialization for RegionGeom - Basmala Hekal

### PRs merged last week (less than 8 days ago): 
* [#6784](https://github.com/gammapy/gammapy/pull/6784) Harmonise SamplerResult output for Nautilus - Quentin Remy
* [#6776](https://github.com/gammapy/gammapy/pull/6776) Add .mailmap entry to consolidate author identity - None
* [#6770](https://github.com/gammapy/gammapy/pull/6770) Backport PR #6757 on branch v2.0.x (Use physical impact parameter in JFactory LoS integral) - Lumberbot (aka Jack)
* [#6761](https://github.com/gammapy/gammapy/pull/6761) ASDF serialization for HpxGeom - Basmala Hekal
* [#6757](https://github.com/gammapy/gammapy/pull/6757) Use physical impact parameter in JFactory LoS integral - Júlia Mamprim
* [#6756](https://github.com/gammapy/gammapy/pull/6756) Add unit support to the violins plot used with the FluxCollection - Laura Olivera-Nieto
* [#6751](https://github.com/gammapy/gammapy/pull/6751) ASDF serialization for WcsGeom - Basmala Hekal
* [#6668](https://github.com/gammapy/gammapy/pull/6668) Remove MapAxis.to_table() from IRF.to_hdulist - Marie-Sophie Carrasco
* [#6660](https://github.com/gammapy/gammapy/pull/6660) Dark Matter Module - Include the option of adding custom DM spectra source - file based #6638 - None
* [#6653](https://github.com/gammapy/gammapy/pull/6653) Add support for creating a `DataStore` from the results of a ivoa TapQurey - Tomas Bylund
* [#6620](https://github.com/gammapy/gammapy/pull/6620) Replace data by table in ObservationTableReader - Fabio PINTORE

### issues opened last week (less than 8 days ago): 
* [#6781](https://github.com/gammapy/gammapy/issues/6781) Add possibility to create the input flux model based on a mixing of several channels - Daniel Kerszberg
* [#6780](https://github.com/gammapy/gammapy/issues/6780) Single class for Annhilation and Decay cases - Daniel Kerszberg
* [#6778](https://github.com/gammapy/gammapy/issues/6778) Dark Matter module: Make regression tests - None
* [#6775](https://github.com/gammapy/gammapy/issues/6775) [2.1] SVD did not converge during CI tests - Ole Streicher
* [#6772](https://github.com/gammapy/gammapy/issues/6772) Dark Matter Module: Change basic structure about the Primary Flux class - Spectral model to Factory - None
* [#6769](https://github.com/gammapy/gammapy/issues/6769) Handle central pixels in JFactory radial integration - Júlia Mamprim
* [#6768](https://github.com/gammapy/gammapy/issues/6768) Dark Matter Module - Enhancement of user tutorials - None

 report created at 10/07/2026, 10:26:40
