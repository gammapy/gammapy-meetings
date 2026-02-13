# Gammapy Developer Meeting 
 * Friday, February 13, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Tomas Bylund (TB), Regis Terrier (RT), Bruno Khelifi (BK), Atreyee Sinha (AS), Basmala Hekal (BH), Daniel Morcuende (DM), Katharina Egg (KE), Matthias Fuessling (MF), Quentin Remy (QR), Fabio Pintore (FP)

# Agenda
## General information
### GSOC project
BH is expressing interest in taking part of the GSOC, RT briefly presented the project and linked to the relevant [issue](https://github.com/gammapy/gammapy/issues/5709).

### Date of coding sprint
RT suggest two options March 30-April 3, and April 30 to ???. Aim is to have 2.1 released shortly before the coding sprint. 

A doodle will be sent.

### Use of AI tools
We are starting to see contributions that have clearly been partially made using LLM-type tools, how are we to keep track and properly disclose their use in papers and similar products?


## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

A new PR [#6381](https://github.com/gammapy/gammapy/pull/6381) that adds GPU acceleration raises the issue of how to test GPU dependent code? On github running GPU workers require paying. BK reports that Nathan Pigoux will try setting up a test runner with GPU access on the Lyon cluster (IN2P?). 


This is ones of several PRs is written by a new contributor that is supposed to join CTAO, but unknown when or where.  The PRs seems to have been at least partially written by an LLM.


## Validation & benchmark

## Ongoing projects

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6389](https://github.com/gammapy/gammapy/pull/6389) Add plot_flux_violin - Quentin Remy
* [#6386](https://github.com/gammapy/gammapy/pull/6386) fix(maps): align TimeMapAxis pixel convention with MapAxis; add round… - None
* [#6385](https://github.com/gammapy/gammapy/pull/6385) Fix: Raise IndexError for negative indices in Map.get_image_by_idx - None
* [#6381](https://github.com/gammapy/gammapy/pull/6381) Evaluator: add GPU acceleration to apply_psf with benchmark - None

### PRs merged last week (less than 8 days ago): 
* [#6392](https://github.com/gammapy/gammapy/pull/6392) Backport PR #6383 on branch v2.0.x (Correct off-by-one error in `WcsGeom.pix_to_idx` clipping) - Lumberbot (aka Jack)
* [#6391](https://github.com/gammapy/gammapy/pull/6391) Backport PR #6388 on branch v2.0.x (Fix HPX pix_to_idx handling of non-spatial pix and add regression test) - Lumberbot (aka Jack)
* [#6390](https://github.com/gammapy/gammapy/pull/6390) Backport PR #6360 on branch v2.0.x (Do not perform equality checks with floating point values) - Lumberbot (aka Jack)
* [#6388](https://github.com/gammapy/gammapy/pull/6388) Fix HPX pix_to_idx handling of non-spatial pix and add regression test - None
* [#6387](https://github.com/gammapy/gammapy/pull/6387) Make LogScale clipping threshold adaptive to input dtype - None
* [#6384](https://github.com/gammapy/gammapy/pull/6384) Cleanup`TimeMapAxis.pix_to_coord` validity mask - None
* [#6383](https://github.com/gammapy/gammapy/pull/6383) Correct off-by-one error in `WcsGeom.pix_to_idx` clipping - None
* [#6382](https://github.com/gammapy/gammapy/pull/6382) Backport PR #6371 on branch v2.0.x (MAJOR fixes for Sonar Qube) - Lumberbot (aka Jack)
* [#6378](https://github.com/gammapy/gammapy/pull/6378) add GTI to FermipyDataset - Tora T. H. Arnesen
* [#6371](https://github.com/gammapy/gammapy/pull/6371) MAJOR fixes for Sonar Qube - Kirsty Feijen
* [#6360](https://github.com/gammapy/gammapy/pull/6360) Do not perform equality checks with floating point values - Bruno Khélifi

### issues opened last week (less than 8 days ago): 
* [#6380](https://github.com/gammapy/gammapy/issues/6380) Run SonarQube on tagged versions - Daniel Morcuende

 report created at 13/02/2026, 07:54:03
