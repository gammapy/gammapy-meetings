# Gammapy Developer Meeting 
 * Friday, September 25, 2026, at 2 pm (CET) 
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

### Dark Matter

- The DM group met earlier this week and work is progressing. Several DM people may start joining dev calls as implementation decisions arrive; Shruti joins next week.

#### CosmiXs as default spectra.

- Decided (DM group): switch from PPPC to CosmiXs, whose spectra are more complete and up to date. One detail check remains; the code change is trivial.
- The deprecation mechanism in the developer guide covers API-breaking changes but not a change of default behaviour.
- Decided: Alex adds a runtime warning when the default is used (PPPC must then be requested explicitly) plus a docstring note.

#### CLUMPY interface 

- The planned tutorial turned out far too large, so the group will implement a reader instead: CLUMPY outputs aren't standard FITS maps and come in many variants.
- Julia's step-by-step roadmap was accepted on Monday, with incremental PRs rather than one big one. She will also contact the CLUMPY team, who have been unresponsive and may no longer maintain the package.

#### Heavy DM spectra 

- Two options: a custom file with the interpolator in main, or the published HeavyDarkMatter interpolator. Alex favours the published one. Régis flagged the resulting dependency; the HDF5 data file is needed either way. Shruti presents next week.

### Validation and I/O redesign

- Marie: No PIG yet, but a live walkthrough. The old validators broke when data format and data model were separated, and validation is needed for FAIR products.
- Design:
  - A registry per format version (GADF 0.3 today) holding table-column definitions and header keyword specs: dtype, required, conditional rules, allowed values, defaults, and keyword blocks per HDU type. Each new version is a deep copy of the base plus its changes.
  - A FormatValidator wrapping a header and a table validator; it collects their reports, with a strict mode that raises. Single entry point validate_hdus, callable on an HDU file.
DataStore integration: at creation, on demand per observation/HDU/format, and in check. Output is a report plus a summary table (version tested, header and table pass/fail, error count and messages).
  - Deliberately lenient: unknown versions and non-GADF files (e.g. OGIP) are reported and the rest still runs. Format auto-detection exists.
Tested across Gammapy datasets, and already used to help validate SDC data.

- Q&A: supporting a new version or new HDUs means touching only the registry; the same holds for VODF, whose providers could supply the dictionaries. The 0.2/0.3 difference seen in the demo is the pointing keyword rules (RA_PNT/DEC_PNT, changed for alt-az instruments).
- Next: short PIG plus tests, then the reader/writer I/O layer that pulls serialization out of the products and calls validation on read and write. A prototype exists.
- GADF 0.4: a proposal from Max to support 3D IRFs in a minor GADF release, though long term this would belong in VODF. Open: clarify with them; supporting 0.4 would mostly mean adding a registry.  

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6868](https://github.com/gammapy/gammapy/pull/6868) Add EffectiveAreaPlotter - Rahma Wael
* [#6867](https://github.com/gammapy/gammapy/pull/6867) Fix memory blowup when computing covariance of many-parameter models - Ahmed Mahmoud
* [#6864](https://github.com/gammapy/gammapy/pull/6864) correct asimov behaviour of ts_to_sigma/sigma_to_ts - Stefan Fröse

### PRs merged last week (less than 8 days ago): 
* [#6852](https://github.com/gammapy/gammapy/pull/6852) Adjust wording for datasets.write to be clearer for user - Kirsty Feijen
* [#6851](https://github.com/gammapy/gammapy/pull/6851) Adapt documentation errors - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6866](https://github.com/gammapy/gammapy/issues/6866) Broken CI - Kirsty Feijen
* [#6863](https://github.com/gammapy/gammapy/issues/6863) Re-calculate data volume of DL4 DL5 products using ASDF serialization - Daniel Morcuende

 report created at 25/09/2026, 12:06:05
