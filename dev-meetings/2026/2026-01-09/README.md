# Gammapy Developer Meeting 
 * Friday, January 09, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Atreyee Sinha (AS), Claudio Galelli (CG), Bruno Khelifi (BK), Quentin Remy (QR), Régis Terrier (RT) 

# Agenda
## General information
- Next user call: AS will find a slot at end of January, early February. Possible agenda items:
	 - BaccMod and other bkg modeling frameworks
 	- Talk from a DM WG person to discuss requirements and missing items
	 - from the gammapy team side: updates on 2.0.1 and possibly a discussion on bkg corrections strategies
- Next coding sprint:
	- BK proposes the week following the CTAO meeting in Paris (i.e. Apr 20th)
	- AS might be around the week after MM conf in Greece (i.e. March 9th)
 - CG likely busy during these periods. QR timescale unclear for first half of 2026.

## [Open issues](https://github.com/gammapy/gammapy/issues)
- Discussion on [New method for the FoVBackgroundMaker: PieceWise+PL](https://github.com/gammapy/gammapy/issues/6297)
  - QR suggests that the proposed behavior is feasible with simple piecewise. Need to check with existing piecewise+pl implementations.
  - Do we need a model in the library? Do we need specific documentation for this approach?
  - In general piecewise approach to FoVBackgroundMAker require adjustements of the `mask_fit` depending on available counts. Can this be done internally as a helper method for users?

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

## Validation & benchmark

- Repeated issues with Zenodo download of LST-1 data. Can we find viable solution?

## Ongoing projects

### Extraction of flux points for multiple sources 
- QR presents new developments for `FluxPointsCollection` with and without fit statistic penalty
  - strong performance increase with caching (masking instead of slicing, converting to TemplateNPred models)
  - Regularized flux points with multiple sources are computationnally heavy and require source per source tuning of the hyper parameter `lambda` that weights the contribution of the penalty. 

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6308](https://github.com/gammapy/gammapy/pull/6308) Correct CITATION location in distribution - Régis Terrier
* [#6305](https://github.com/gammapy/gammapy/pull/6305) Add support for numpy 2.4 - Régis Terrier

### PRs merged last week (less than 8 days ago): 
* [#6310](https://github.com/gammapy/gammapy/pull/6310) Backport PR #6303 on branch v2.0.x (Pin numpy<2.4) - Lumberbot (aka Jack)
* [#6309](https://github.com/gammapy/gammapy/pull/6309) Backport PR #6300 on branch v2.0.x (Bump actions/upload-artifact from 5 to 6) - Lumberbot (aka Jack)
* [#6307](https://github.com/gammapy/gammapy/pull/6307) Backport PR #6301 on branch v2.0.x (Bump stefanzweifel/git-auto-commit-action from 7.0.0 to 7.1.0) - Lumberbot (aka Jack)
* [#6306](https://github.com/gammapy/gammapy/pull/6306) Backport PR #6302 on branch v2.0.x (Bump SonarSource/sonarqube-scan-action from 6 to 7) - Lumberbot (aka Jack)
* [#6303](https://github.com/gammapy/gammapy/pull/6303) Pin numpy<2.4 - Régis Terrier
* [#6302](https://github.com/gammapy/gammapy/pull/6302) Bump SonarSource/sonarqube-scan-action from 6 to 7 - None
* [#6301](https://github.com/gammapy/gammapy/pull/6301) Bump stefanzweifel/git-auto-commit-action from 7.0.0 to 7.1.0 - None
* [#6300](https://github.com/gammapy/gammapy/pull/6300) Bump actions/upload-artifact from 5 to 6 - None

### issues opened last week (less than 8 days ago): 
* [#6304](https://github.com/gammapy/gammapy/issues/6304) [2.0.1] CITATION and CITATION.cff are installed outside of gammapy - Ole Streicher

 report created at 09/01/2026, 07:31:24
