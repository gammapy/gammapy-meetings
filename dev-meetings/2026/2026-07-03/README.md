# Gammapy Developer Meeting 
 * Friday, July 03, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information

- A discussion took place earlier about the Technical Coordination Committee (TCC); a summary of that discussion is planned for next week's call.
- Comments on the Gammapy paper were due by today; some feedback has already come in, more may arrive over the weekend.
  - Action: read and comment paper before early next week (all).

## Validation & benchmark

## Dark matter module discussion

Alex (PhD student, Universidad Complutense de Madrid, visiting Paris to work with Daniel) and Júlia (PhD student, USP Brazil, currently at Universidad Autónoma de Madrid) gave updates on ongoing DM work. The DM group holds its own monthly meetings (next general one in September, online) to review PRs/issues; a dedicated meeting on integrating the Clumpy software into Gammapy is scheduled for July 7 at 3:30pm — the link will be shared on the dev Slack channel.

#### PR #6660 – Primary flux refactor (merged)
  - Adds support for computing DM spectra from two built-in sources (COSMICS and PPPC4) plus a user-supplied custom file.
  - Régis raised that this makes the PrimaryFlux class behave more like a model factory than a standard spectral model, which has implications for serialization (parameters can change post-serialization, so the current record isn't fully reliable).
  - Agreed: open a separate issue to discuss with the full DM team whether primary flux/mapping logic needs a longer-term redesign
    (e.g. requiring a     converter/helper function or a fixed convention for custom tables), rather than changing it now.

- Parameter naming refactor (mass → Mdm, etc.)
  - Discussed in a large, already-long PR; agreed to split this into a separate PR for the naming change (Quentin, Kirsty).
    Régis flagged that renaming a model parameter breaks backward compatibility for serialized/model files — deprecation handling and dual read-support (old and new names) will be needed.
  - Decision: hold off on urgent renaming; better to batch all parameter-name changes together if/when the primary-flux logic itself is revisited.
  - Related: the J-factor / to_dict also needs updating consistently if names change.


#### PR #6744 – Parameter validation
- Introduces a shared/private validator class to check spectral model parameters (e.g. redshift), since previously there was no validation (redshift wasn't a  "real" parameter, just a dictionary attribute).
- Discussion of whether redshift/particle mass should become actual Parameter objects — concluded no, since they're fixed (not fit); only the flux/cross-section scale is genuinely fit.
- Alex will check serialization/backward-compatibility implications before this is re-reviewed.


#### J-factor issues (Julia)

- The JFactor class had significant bugs: it worked only for small angles near the Galactic Center, with a hardcoded distance-to-GC and integration limit.
- One PR (angular parameterization fix) is merged; another PR by Alex (fixing the hardcoded GC distance) is in progress and now has a merge conflict with Júlia's change.
- Júlia will wait for Alex's distance-parameter PR to merge before opening her next PR, which addresses integration-limit edge cases for different pixel positions.
- Newly found bug: central-pixel evaluation fails (log of zero) for maps without an even number of pixels, since the J-factor integrand diverges at the center for steep DM profiles. Proposed fix: subdivide the central pixel to avoid evaluating exactly at the center. Not yet discussed with the full DM group; open as a follow-up issue.
  - Régis flagged it's worth checking whether this central-pixel issue is DM-specific or a broader map-integration issue.

#### COSMICS vs PPPC4 default spectra

- An open issue tracks an inconsistency: PPPC4 and COSMICS report spectra binned differently near the kinematic endpoint (PPPC4 uses the bin's max value, COSMICS uses a mid-bin value), causing a discrepancy at the highest-mass bin.
- Not an action item for Gammapy directly — waiting on response from the COSMICS/PPPC4 maintainers (a COSMICS developer is already engaged in the issue thread).


#### Shipping DM reference data

- Open question on whether DM model data (COSMICS/PPPC4 tables, future models) should keep being bundled in gammapy-data, or be handled differently (e.g.   downloaded on demand), given growing requests to support more external models (EBL, DM, etc.) and concerns about test speed and long-term maintenance.
- Régis suggested a possible longer-term option: spin the DM/Astro sub-package into a semi-standalone package depending on Gammapy, which could simplify community contributions.
- Quentin proposed defining a Gammapy-specific data format/convention that external contributors must follow to be included, rather than accepting arbitrary formats.
- No decision made; flagged as a broader design/policy question to revisit as the DM group's needs evolve.

#### DM validation

- Régis noted that the existing coverage-validation framework could be extended to validate DM-related computations (e.g. the J-factor line-of-sight integration bug fixed recently by Júlia was found this way), and encouraged the DM team to think about adding regression/sanity checks of this kind.


## Sensitivity Estimator (PR #6758 — Atreyee)

- New, lightweight SensitivityEstimator built purely from IRFs (no counts map needed), aimed at users who want quick sensitivity curves (e.g. for joint/Cherenkov-array sensitivity comparisons) without running a full analysis via the flux point estimator.
- Discussion on whether to also support integral sensitivity (vs. only differential): Régis noted it's not trivial to derive analytically from differential sensitivity, since it requires going back to per-bin counts; questioned how meaningful integral sensitivity really is today given better IRFs/differential sensitivity tools.
- Discussion on exposing the Asimov dataset as a public/documented feature — useful for forecasting detectability or planning observations before unblinding data, but needs proper documentation/tutorial or a paper reference before being broadly exposed; agreed no changes needed right now, but worth considering as a documented use case later.
- Question of whether this new estimator could eventually replace the older SensitivityEstimator: Quentin suggested simplifying the implementation to just build an Asimov dataset and call the flux point estimator (a few lines), though this conflicts with supporting integral/cumulative sensitivity. Régis noted that cumulative/joint sensitivity is hard with the current map data structure (bins must be contiguous, and flux maps are fundamentally tied to the map geometry).
- Decision: keep PR open, continue iterating; not necessarily targeted for the 2.2 release given remaining open design questions (minimum counts handling — per dataset vs. per bin — and reproducing old-estimator behavior for the single-observation case).


## Validation / Coverage Framework (Régis)

- Update on the ongoing "coverage validation" work in gammapy-benchmarks: runs flux-point estimation on many fake datasets to check statistical coverage and where it breaks down.
- New addition: sensitivity validation — compares expected sensitivity (from Asimov dataset) against Monte Carlo toy simulations for 1D and 3D cases, shown via example plots (median significance vs. simulated realizations, with an uncertainty band).
- Results shown were in good agreement for higher-statistics cases (e.g. 10h observation); lower-statistics/short-observation cases show larger deviations, as expected.
- Fabio Acero asked whether this reproduces the known failure mode described in the Gammapy paper (low-statistics regime); Régis will test with the exact configuration used to generate that paper's figure to confirm reproducibility.
- This framework could be extended to validate other estimators similarly (confirming that simulation and estimator results are consistent, or fail in the expected regime).

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6771](https://github.com/gammapy/gammapy/pull/6771) ASDF serialization for RegionGeom - Basmala Hekal
* [#6762](https://github.com/gammapy/gammapy/pull/6762) Fix MapDatasetOnOff._to_asimov_dataset to use nominal background instead of marginalised estimate - Atreyee Sinha
* [#6761](https://github.com/gammapy/gammapy/pull/6761) ASDF serialization for HpxGeom - Basmala Hekal
* [#6758](https://github.com/gammapy/gammapy/pull/6758) Add a joint sensitivity estimator - Atreyee Sinha
* [#6756](https://github.com/gammapy/gammapy/pull/6756) Add unit support to the violins plot used with the FluxCollection - Laura Olivera-Nieto
* [#6752](https://github.com/gammapy/gammapy/pull/6752) Clarify sensitivity calculation behaviour - Atreyee Sinha
* [#6751](https://github.com/gammapy/gammapy/pull/6751) ASDF serialization for WcsGeom - Basmala Hekal
* [#6745](https://github.com/gammapy/gammapy/pull/6745) Gamma Ray Line spectra implementation - None
* [#6744](https://github.com/gammapy/gammapy/pull/6744) Dark Matter module - Refactor and test enhance of the spectra class - None

### PRs merged last week (less than 8 days ago): 
* [#6770](https://github.com/gammapy/gammapy/pull/6770) Backport PR #6757 on branch v2.0.x (Use physical impact parameter in JFactory LoS integral) - Lumberbot (aka Jack)
* [#6767](https://github.com/gammapy/gammapy/pull/6767) Bump stefanzweifel/git-auto-commit-action from 7.1.0 to 7.2.0 - None
* [#6766](https://github.com/gammapy/gammapy/pull/6766) Bump actions/checkout from 6 to 7 - None
* [#6765](https://github.com/gammapy/gammapy/pull/6765) Bump astral-sh/setup-uv from 8.1.0 to 8.2.0 - None
* [#6764](https://github.com/gammapy/gammapy/pull/6764) Bump codecov/codecov-action from 6 to 7 - None
* [#6763](https://github.com/gammapy/gammapy/pull/6763) Bump actions/cache from 5 to 6 - None
* [#6759](https://github.com/gammapy/gammapy/pull/6759) Backport PR #6748 on branch v2.0.x (Add gammapy-data to devdeps ci) - Lumberbot (aka Jack)
* [#6757](https://github.com/gammapy/gammapy/pull/6757) Use physical impact parameter in JFactory LoS integral - Júlia Mamprim
* [#6755](https://github.com/gammapy/gammapy/pull/6755) Backport PR #6750 on branch v2.0.x (Fix bug causing selection of dimmest sources instead of brightest.) - Lumberbot (aka Jack)
* [#6750](https://github.com/gammapy/gammapy/pull/6750) Fix bug causing selection of dimmest sources instead of brightest. - Nicki Bond
* [#6748](https://github.com/gammapy/gammapy/pull/6748) Add gammapy-data to devdeps ci - Régis Terrier
* [#6735](https://github.com/gammapy/gammapy/pull/6735) ASDF serialization for `MapAxes` class - Basmala Hekal
* [#6660](https://github.com/gammapy/gammapy/pull/6660) Dark Matter Module - Include the option of adding custom DM spectra source - file based #6638 - None

### issues opened last week (less than 8 days ago): 
* [#6769](https://github.com/gammapy/gammapy/issues/6769) Handle central pixels in JFactory radial integration - Júlia Mamprim
* [#6768](https://github.com/gammapy/gammapy/issues/6768) Dark Matter Module - Enhancement of user tutorials - None
* [#6760](https://github.com/gammapy/gammapy/issues/6760) Check JFactory line-of-sight integration branch decomposition - Júlia Mamprim
* [#6754](https://github.com/gammapy/gammapy/issues/6754) JFactory uses tan(theta) instead of the physical impact parameter sin(theta) as lower radial bound - Júlia Mamprim
* [#6753](https://github.com/gammapy/gammapy/issues/6753) Dark Matter Module - Local density and GC distance - tgirault
* [#6747](https://github.com/gammapy/gammapy/issues/6747) Have a cool badge like astropy (tracking contributors, PR, citations, etc) - Fabio Acero
* [#6746](https://github.com/gammapy/gammapy/issues/6746) astropy region 0.12 causing issues in gammapy/utils/regions.py - Fabio Acero

 report created at 03/07/2026, 10:08:26
