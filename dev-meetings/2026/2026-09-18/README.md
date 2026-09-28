# Gammapy Developer Meeting 
 * Friday, September 18, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

Attendees: 

# Agenda
## General information

### User call

- Tuesday 29 September, 15:00 Paris time (initially announced as "Monday 29th", then corrected). Fabio will present upper limits, plus something on gammapy multi-wavelength.
Team report at the user call: Atreyee will give it (~5 min). Content: next release being finalized, the new known-issues mechanism, Gammapy paper submitted.

### Face-to-face meetings
Option A — 9–10 November (after the CADS school): small group. Proposed focus: roadmap priorities and validation. 
Option B — 2–4 December:  Proposed focus: gammapy multi-wavelength, interoperability, FAIR aspects — beyond the release/validation timeline.

Decided: Both meetings are complementary and can be held; no objections to the proposed split. Pending: Create a short page for each.

### SDC (Science Data Challenge)

#### Steering committee meeting
- SDC cookbooks/notebooks (dark matter among them) are being finalized, 5–6 notebooks will come to the Gammapy team for review in the coming weeks.
- Timeline: official SDC release targeted around December → data production, documentation, datasets, data portal all ready before then. 

#### Validation / verification for the release
- Matthias: this is a common effort. Work to do: centralize existing validation/benchmarking material; process the detailed review of the science-analysis use-case document; separate low-level vs high-level use cases; map use cases to tests / documentation / notebooks → verification report covering at least the SDC-supported subset. SDC notebooks can serve as additional material.

## Ongoing projects

### Plotter conversion project

- Several simple, independent first issues opened.
- Decided: Developed on the side, not replacing current plotting before the release; swap in a future release once tested.
- Open PR on axis initialisation showed plotting code is scattered (e.g. axis formatting living in MapAxis) → further clean-up to be revisited so the project is complete.

### ASDF serialization

Two open PRs:
- Models: single converter built on existing to_dict/from_dict; covariance (normally in a separate file) handled inside the converter; one general schema for all model types;
  tested on SkyModel and combined spectral models; template model (needs a FITS file) handled specially. Last review round still to address.
- MapDataset / MapDatasetOnOff: converters in one file; metadata (MapDatasetMetadata) serialized as a dict; counts, exposure, background etc. tagged to existing map serializations.
  Problems testing with gammapy-data datasets: legacy objects (e.g. PSF map with a RegionGeom without a region); a FITS numpy boolean rejected by ASDF (expects Python bool).

Discussion:
- Régis: FAIR-compliant ASDF will eventually need schemas for metadata too; longer-term decision. Also a candidate for DL4/DL5 products; user-testing phase needed.
- Bruno: ASDF (schema ↔ class link, like ROOT streamers) brings flexibility and provenance → question to raise within CTAO (data model group).
- Matthias: FITS is currently required in CTAO but not frozen; adopting another format needs analysis of DPPS production with IRFs and IVOA usage; relation to VODF should be explored. A report   could be the basis to approach CTAO.
- Atreyee: file sizes vs FITS? ASDF allows per-array compression; re-run the CTAO DL4/DL5 data-volume calculation once merged. 

### Astropy separation warning 

- PR #6861 fixes Astropy complaints about coordinate separation calculations; the PR documents where they arise. Reviews requested.
- Discussion on drifting observations deferred to a later call.

### Sensitivity estimator NaN bug (Atreyee)
- PR fixes NaNs present in dev and 2.1 but not 2.0 (confirmed with Fabio's script). Root cause: a function introduced in 2.1 replaced the previous CountsStatistic-based internal computation. -
- Second issue: scanned parameter range based on n_sigma too narrow when n_sigma_ul/n_sigma_sensitivity is larger → root finding fails.
 
- Decided: Clipping approach acceptable for now; Atreyee to use Parameter.n_sigma internally. Open: General policy for returning ΔTS (zeroing tiny absolute differences).
  
## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6862](https://github.com/gammapy/gammapy/pull/6862) Fix Sensitivity estimator returning NaN - Atreyee Sinha
* [#6861](https://github.com/gammapy/gammapy/pull/6861) Fix separation warning - Tomas Bylund
* [#6860](https://github.com/gammapy/gammapy/pull/6860) Add RadMaxPlotter and test - None
* [#6851](https://github.com/gammapy/gammapy/pull/6851) Adapt documentation errors - Kirsty Feijen
* [#6850](https://github.com/gammapy/gammapy/pull/6850) ASDF: serialization for Models - Basmala Hekal
* [#6849](https://github.com/gammapy/gammapy/pull/6849) ASDF: serialization for MapDataset and MapDatasetOnOff - Basmala Hekal

### PRs merged last week (less than 8 days ago): 
* [#6859](https://github.com/gammapy/gammapy/pull/6859) Expose PIG31 - Kirsty Feijen
* [#6852](https://github.com/gammapy/gammapy/pull/6852) Adjust wording for datasets.write to be clearer for user - Kirsty Feijen
* [#6845](https://github.com/gammapy/gammapy/pull/6845) Introduce BasePlotter class - Régis Terrier
* [#6833](https://github.com/gammapy/gammapy/pull/6833)  ASDF: serialization for IRFMap classes - Basmala Hekal

### issues opened last week (less than 8 days ago): 
* [#6858](https://github.com/gammapy/gammapy/issues/6858) Untested file - Atreyee Sinha
* [#6857](https://github.com/gammapy/gammapy/issues/6857) Introduce RadMaxPlotter class - Régis Terrier
* [#6856](https://github.com/gammapy/gammapy/issues/6856) Introduce EdispPlotter and EdispKernelPlotter classes - Régis Terrier
* [#6855](https://github.com/gammapy/gammapy/issues/6855) Introduce EffectiveAreaPlotter - Régis Terrier
* [#6854](https://github.com/gammapy/gammapy/issues/6854) Introduce BackgroundPlotter - Régis Terrier
* [#6853](https://github.com/gammapy/gammapy/issues/6853) Incorrect PSF table containment fraction for large rad values - Régis Terrier
* [#6847](https://github.com/gammapy/gammapy/issues/6847) EventList.peek(): x-axis labels overlap on Energy [TeV] panels - Sarah
* [#6846](https://github.com/gammapy/gammapy/issues/6846) Additional options for the Plotter class - Kirsty Feijen

 report created at 18/09/2026, 12:09:55
