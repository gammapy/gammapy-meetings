# Gammapy Developer Meeting 
 * Friday, November 21, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack)
 * Attendees:  Régis Terrier, Tomas Bylund, Daniel Morcuende, Kirsty Feijen, Fabio Acero, Claudio Galelli, Katharina Egg, Aritra Gupta, Bruno Khelifi, Viviana Gammaldi, Judit Perez-Romero, Jaume Zuriaga-Puig

# Agenda
## General information

### Gammapy v2.0 paper

- Should consider reviving the effort for the v2.0 paper. Regis redid the joint crab with the nested sampling for the CADS school, so we could include that in the paper.
- we have elements from the school which could make it easier to have the outline for the paper
- sidenote: SILK project ideas won't be published until next year, so we should mention the new functionalities but leave more extended discussion for that publication
- Kirsty suggests organizing weekly meetings (rather than fortnightly) for advancing with the paper - we have a poll for that on the channel

### Provenance
- Tomas proposes a prototype for provenance tracking is inspired by ctapipe : a singleton that keeps track of everything in a big log
- Tomas presents an example for tracking the data reduction; being able to set the tracker on makers, observations, and datasets, for example
- do we really want to track provenance in user scripts or at the workflow level?

    - Régis suggests to have it at the workflow level for the work that Quentin has done

    - it is harder to track at the notebook level, so we need to have a clear strategy going forward

- currently prototyping work, so we should keep track of the discussions on this

    - decided to create a sub repo for this 



### Dark matter discussion
with Viviana Gammaldi, Juame Zuriaga-Puig, Judit Pérez-Romero and Aritra Gupta

- Aritra: summary of what we need to do in [#174](https://github.com/gammapy/gammapy-benchmarks/issues/174) but specifically has been working on fixing the j-factors
- PrimaryFlux contains all the tables from the PPPC4 paper

    - Judit already checked that the tables are correct: when there is a strong cutoff there was an error, but there was a correction. One of the nice aspects of gammapy is the spectral model incorporated by Judit (DarkMatterAnnihilationSpectralModel). Computation of j-factors is very different for the type of objects (density profile) etc but all of this is incorporated in a more complex code called [CLUMPY](https://clumpy.gitlab.io/CLUMPY/v3.1.1/)

- The main idea we had is to make sure what we currently have is correct

    - we have simple j-factor calculations but do not want to incorporate too much and repeat what is already out there, so we could think of having an interface to CLUMPY?

- Should we have any j-factor in gammapy?

    - it could be nice for some toy examples, but it is hard to incorporate all the source types needed

    - instead need to have an interface that can handle the outputs of CLUMPY (and possibly for CosmiXs)

- There is a new code for the calculation similar to PPPC4 called [CosmiXs](https://github.com/ajueid/CosmiXs)

    - Can be used to calculate various aspects with the new updated spectra given to the community

- channel created on slack dark-matter
- Will fix a date for another meeting to have a summary

## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

- SonarQube will be merged and then we can go ahead with the pyproject toml

## Validation & benchmark

## Ongoing projects

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6227](https://github.com/gammapy/gammapy/pull/6227) Corrected required model unit if exposure not applied - Katharina Egg
* [#6225](https://github.com/gammapy/gammapy/pull/6225) MAINT: Test python 3.14 in CI and drop 3.10 - Daniel Morcuende
* [#6224](https://github.com/gammapy/gammapy/pull/6224) Fix the way labels are fetched for changelog check - Daniel Morcuende
* [#6223](https://github.com/gammapy/gammapy/pull/6223) Simplify the generation script for contributors for the release procedure - Kirsty Feijen
* [#6222](https://github.com/gammapy/gammapy/pull/6222) Update mailmap with old email addresses - Daniel Morcuende
* [#6221](https://github.com/gammapy/gammapy/pull/6221) Add monthly workflow to run pre-commit over all files with fixes - Daniel Morcuende

### PRs merged last week (less than 8 days ago): 
* [#6218](https://github.com/gammapy/gammapy/pull/6218) Backport PR #6217 on branch v2.0.x (Check changelog: set fetch depth to 0 so diff is done against all fetched refs) - Lumberbot (aka Jack)
* [#6217](https://github.com/gammapy/gammapy/pull/6217) Check changelog: set fetch depth to 0 so diff is done against all fetched refs - Daniel Morcuende
* [#6213](https://github.com/gammapy/gammapy/pull/6213) Add a link towards the `npred` computation into the stats user-guide page - Bruno Khélifi
* [#6128](https://github.com/gammapy/gammapy/pull/6128) Prototype for a new ObservationTable class - Leander Schlegel

### issues opened last week (less than 8 days ago): 
* [#6229](https://github.com/gammapy/gammapy/issues/6229) Negative `lambda_` and non-integer `alpha` in `ExpCutoffPowerLawSpectralModel` returns NaN - REGEARD Maxime
* [#6228](https://github.com/gammapy/gammapy/issues/6228) `plot_error` method of `SpectralModel` can fail by sampling specific parameter values - REGEARD Maxime
* [#6226](https://github.com/gammapy/gammapy/issues/6226) Wrong model unit required if exposure not applied - Katharina Egg
* [#6220](https://github.com/gammapy/gammapy/issues/6220) Add fragment file for #6197 - Kirsty Feijen
* [#6219](https://github.com/gammapy/gammapy/issues/6219) Monthly pre-commit run over all files - Daniel Morcuende

 report created at 21/11/2025, 07:25:41
