# Gammapy Developer Meeting 
 * Friday, January 23, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Fabio Pintore (FP), Livia Rocha (LR), Tomas Bylund (TB), Quentin Remy (QR), Atreyee Sinha (AS), Katharina Egg (KE), Kirsty Feijen (KF), Bruno Khelifi (BK), Régis Terrier (RT), Claudio Galelli (CG), Fabio Acero (FA), Natthan Pigoux (NP)


# Agenda
## General information
- automatic report workflow failed because of deprecated access token. A new token has been generated but no report is available for this week.


### CTAO Science Analysis Tool acceptance process
BK describes the CTAO product acceptance procedure: there are several review rounds which each require the creation of formal documentation of the software that is to be delivered. This work is formally the responsibility of the IKC labs.

Possible plan: 
    Start of Preliminary Design review summer this year, but in parallel work on documents for the Critical Design Review. This supposing that Gammapy can be reviewed separately from the other parts of SUSS, some of which are quite delayed.

### Gammapy 2.1 release date
Initially scheduled for next week, timed to have an version ready for the CTAO Science Data Challenge, but it seems already 2.0.1 fixes all issues reported from the SDC team. Only open issue is which keyword to  are to be saved, but this is no showstopper.

RT requests proposals on what should go into 2.1 to decide on what is an appropriate new date.
- QR nominates the Bayesian model selection, estimated as needing 1 month.

RT Suggest feature freeze on 27th of February, and next release the 12th of March.

### Summer of code
The Google and European summer of code project applications are due quite soon, is anyone interested in submitting a proposal? RT has one idea about making an ASDF reader, that was an idea from RT and KF from last year. Will likely resubmit it.

### Paris Gammapy school
Planned for 2-6 of November

### Summer conferences
Submission deadlines for summer conferences are approaching, ex COSPAR has deadline 13 of February.

## [Open issues](https://github.com/gammapy/gammapy/issues)
KF has started working on cleaning up gammapy-data, work is being tracked in [#78](https://github.com/gammapy/gammapy-data/issues/78), things like standardization  

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)
BK reports that currently the sphinx build is failing for an unclear reason.

## Validation & benchmark

## Ongoing projects
### Unbinned analysis
Guillaume opened 8 new PRs about the unbinned analysis prototype. A meeting for discussing this work is being scheduled via [doodle](https://www.when2meet.com/?34553083-8XKGT).


