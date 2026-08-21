# Gammapy Developer Meeting 
 * Friday, August 21, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information

### How to communicate on known Issues 
- Discussion prompted by a recurring problem where users report an issue that's already been fixed but not yet released (multiple duplicate issues were found, one recently closed by Kirsty).
- Since the fix won't be visible until 2.2 (1–2 months out), the group discussed how to reduce duplicate reports in the meantime.
- Agreed approach: use a pinned GitHub Discussion (versioned, e.g. "v2.1") as a "known issues" page, linked from the issue template and documentation, with an announcement   pinned in the Slack general/help channel.
- Matthias suggested this should scale to cover known issues across multiple Gammapy versions, not just the latest.
- Action items:
  - Create/clean up the pinned discussion for known issues.
  - Open an issue to track adding this step to the release procedure.
  - Post a Slack announcement pointing to the new discussion-based mechanism.

### Regions Library and Spherical Regions
- regions v0.12 introduces spherical regions (independent of WCS), in addition to the existing pixel and sky region types.
- This likely makes Gammapy's own CircleSkyRegion implementation obsolete. It could be deprecated in favor of the upstream spherical circle region, though not necessarily for 2.2 (more likely 2.3+, once regions 0.12 is a safe minimum dependency).
- Broader question raised: should Gammapy adopt spherical regions more generally for region geometries, given they're WCS-independent (current implementation assumes a tangent projection at the region center)? Not all shapes have spherical equivalents (e.g. rectangle), though polygon does.  Some interesting new shapes (e.g. "lune," the intersection of two circles).
- Conversion to pixel regions would still require a WCS, so reflected-region algorithms (which operate on pixel regions) would be largely unaffected for now.

## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

## Validation & benchmark

## Ongoing projects

### Energy-Dependent / Array-Valued Regions
- Quentin revisited the old PR (originally from Axel) on array-valued/energy-dependent regions, motivated by energy-dependent RAD_MAX use cases (currently handled via a workaround treating the source as a point region, which loses information about the angular selection applied).
- Testing showed the original example from Axel's PR was broken and needs fixes; not clearly generalizable yet.
- Quentin noted a possible additional use case: energy-dependent safe masks for 3D analyses.
- Open question: whether array-valued regions can be properly serialized (currently unclear/untested) as part of a RegionGeom.
- Next step: Quentin will test serialization; if it doesn't work cleanly, the effort may not be worth continuing.

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6825](https://github.com/gammapy/gammapy/pull/6825) Unification of Dark Matter Spectral classes - None
* [#6824](https://github.com/gammapy/gammapy/pull/6824) Tutorial adaptation after merging #6819 - None

### PRs merged last week (less than 8 days ago): 
* [#6822](https://github.com/gammapy/gammapy/pull/6822) Backport PR #6821 on branch v2.0.x (Fix fragment file links and descriptions) - Lumberbot (aka Jack)
* [#6821](https://github.com/gammapy/gammapy/pull/6821) Fix fragment file links and descriptions - Kirsty Feijen
* [#6819](https://github.com/gammapy/gammapy/pull/6819) Fix JFactory line-of-sight branch geometry - Júlia Mamprim
* [#6799](https://github.com/gammapy/gammapy/pull/6799) Addition of LogNormal Prior - Fix bug on JFactor nuisance - None
* [#6782](https://github.com/gammapy/gammapy/pull/6782) Dark Matter module: Part 1: Update Dark Matter BASICS Tutorial - None
* [#6779](https://github.com/gammapy/gammapy/pull/6779) Inclusion of regression test for a Dark Matter Module - None
* [#6744](https://github.com/gammapy/gammapy/pull/6744) Dark Matter module - Refactor and test enhance of the spectra class - None

### issues opened last week (less than 8 days ago): 
* [#6820](https://github.com/gammapy/gammapy/issues/6820) Create Gammapy-Benchmkark science case verification - None

 report created at 21/08/2026, 07:48:14
