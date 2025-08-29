# Gammapy Developer Meeting 
 * Friday, August 29, 2025, at 2 pm (CET)  approx. 14:05-15:17
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

Attendees: Leander Schlegel (LS), Tomas Bylund (TB), Aritra Gupta (AG), Régis Terrier (RT), Daniel Morcuende (DM), Kirsty Feijen (KF), Atreyee Sinha (AS), Mattias Fuessling (MF)
 
# Agenda
## General information

### v2.0 release status
RT reports: 
Release made last Tuesday (August 26), AS made most of the work. 

Overall went fine. Validation and benchmarks scripts used for the released version were also tagged. 

The instructions for making the final full release did not contain the step where `dev/prepare-release.py` is run, and consequently some metadata for the release is incomplete.

The automatic adding of the new version to Zenodo failed, so will have to be done manually.
Bruno has done this before and back then contacted Zenodo team for this.

RT: Has someone already installed and checked that everything is okay with release?

DM confirms for mamba.

RT: All steps are now checked and we should announce the new version. 

AS: Should make sure mails are sent to VERITAS, MAGIC, HAWC, SWGO, need to find people who can send to their mailing lists. 

RT: Have to prepare text for announcement mails. After mails are sent, there should be celebrations.

### Reflections on the new release
RT: It was a long time to make this release, probably the roadmap was too ambitious.

AS: Gabriel Emery was missed for the contributor list somehow, but he is in the author list. Unclear how this happened. Is it worth to update the docs to ensure he is included?
RT: Probably not before next bugfix as manually rebuilding the docs is complicated, as it will be fixed soon probably in any case.

### Introduction of AG: 

AG introduces themselves: Research on phenomenology of dark matter (theory), accretion od DM in compact objects (neutron stars, white dwarfs). Aim to understand and help on DM frontier with gammapy. 

Theoretical predictions fluxes below observed fluxes (???), 

-Theory background: 
In models, DM could be thermalized or non-thermalized. Dark sector with 1 particle, major portion of DM today is non-rel/cold. DM models provide: Velocity averaged annihilation cross-section for annihilation of DM and DM mass. The DM annihilates into standard particles, that go into pions and finally gamma rays. Different models exist (e.g. with dark sector). Possible that no annihilation at threshold is expected, missing in most codes today.

-Possible observations: Diffuse flux or smoking gun signatures in form of lines. Line signatures require good calculation of background, but models that provide line predictions are interesting. 
In non-thermal DM we can not rely on direct detection. Line sig. and diffuse photon flux give opportunity for DM frontier (???) 

We did work which predicts neutrino line, it would be very interesting to see how to work on it from observation side. (???)

Would like to help with these points for DM.

RT: Very interesting view. We include some tables that have part of the channels. Question if we should provide models directly in Gammapy or simply create an interface into which theorists could insert their models. 
View as developer: We have had contributions for DM at points, but difficult to get team in the long run set on DM (???)
Dark matter analysis could also be interesting topic for a User call, could try to have one before the end of the year. 

AS: I'm sure there will be enough people interested.

RT: We have number of feature requests related to DM (e.g. #5734, #5359, #4776). Main question is how to organize, what should be there, how to connect with external things like new models. Maybe we could create parent-discussion to gather all this.

AS: We create a new project for DM? 

RT: Yes is good idea, just not clear how to organize in the moment/what to put in. Some things connected to modelling, some to analysis, estimators.

AG: Brainstorming: We could ask users, if thermal or non thermal models, heavy, light DM. Theoretical parameters would then be input to our code, that predicts fluxes. In every case different input needed. With this we take out the theory parts for the observational/experimental side of the code.

RT: Not sure if/how to implement in gammapy option dependent on some parameters. But should define how to interface codes, could be simpler way to work. Maintaining on long term for DM models we probably can not do.
Then model production would be left to dedicated codes, but we agree how to interface with Gammapy.
Let's organize user-call on this and contact people, who contributed on this in the past.

AS: Next user-call probably in November.

RT: Should be okay, more important, that most people related to it are around.

AG: I can take a look at open issues and try to fix them.

### Organising the development cycle
RT: Try to establish main projects that drive the timing of the release cycle.
We could discuss among all devs.
Need to think more carefully about how to set milestones for PRs and issues, there has been tendency to simply bump things to next available milestone but this means no prioritization is being done. Should start to put things into wishlist by default and only milestone things after performing a prioritization. Should go through features in next dev call to discuss. Will put most into wishlist.

MF: Congratulations to Gammapy 2.0! We will give you room to present this release in depth at October CTAO-meeting and hope some of you that worked hard on it, can be there.
Should make sure this leads to a proper release of the Science Analysis Tools, which would be a major milestone for the Science tools work package. 
Reminds us that the SAT is supposed to serve for the science data challenge, in particular Gammapy 2.1 will be used to generate the simulation for the SDC, and so it is important to check ahead of time that all features needed for the SDC are present in Gammapy. We will discuss with David Green next week about the list of science cases in order to give input for the planning of release 2.1 during the first weeks of the new development cycle.

### Next user call
AS: Can I announce 22.9 for the next User-Call? I asked QR and FP. 

RT: Yes, perfect.

RT: Thats all for today, thank you and have a nice week.

## Open issues

## Bugs

## Documentation

## DevOps

## Validation & benchmark

## Ongoing projects:
### sensi

### HLI

### MWL

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6116](https://github.com/gammapy/gammapy/pull/6116) Add missing contributor in release notes for v2.0 - Gabriel Emery
* [#6115](https://github.com/gammapy/gammapy/pull/6115) Kwargs updates - Kirsty Feijen
* [#6108](https://github.com/gammapy/gammapy/pull/6108) fix Flux unit of FluxPoints object inconsistent - Tomas Bylund
* [#6102](https://github.com/gammapy/gammapy/pull/6102) jfactory integral calculation description - Kirsty Feijen

### PRs merged last week (less than 8 days ago): 
* [#6113](https://github.com/gammapy/gammapy/pull/6113) Update release instructions - Régis Terrier
* [#6112](https://github.com/gammapy/gammapy/pull/6112) Backport PR #6094 on branch v2.0.x (Fix release notes for v2.0) - Lumberbot (aka Jack)
* [#6110](https://github.com/gammapy/gammapy/pull/6110) Backport PR #6105 on branch v2.0.x (Update quickstart.rst for windows installation) - Lumberbot (aka Jack)
* [#6109](https://github.com/gammapy/gammapy/pull/6109) Backport PR #6095 on branch v2.0.x (jupytext requires plt.show) - Lumberbot (aka Jack)
* [#6107](https://github.com/gammapy/gammapy/pull/6107) Backport PR #6106 on branch v2.0.x (Remove deprecated pydantic copy in tutorial) - Lumberbot (aka Jack)
* [#6106](https://github.com/gammapy/gammapy/pull/6106) Remove deprecated pydantic copy in tutorial - Régis Terrier
* [#6105](https://github.com/gammapy/gammapy/pull/6105) Update quickstart.rst for windows installation - Atreyee Sinha
* [#6104](https://github.com/gammapy/gammapy/pull/6104) Backport PR #6101 on branch v2.0.x (Add instrument names in tutorials  data section) - Lumberbot (aka Jack)
* [#6103](https://github.com/gammapy/gammapy/pull/6103) Backport PR #6100 on branch v2.0.x (Update installation for windows instruction) - Lumberbot (aka Jack)
* [#6101](https://github.com/gammapy/gammapy/pull/6101) Add instrument names in tutorials  data section - Atreyee Sinha
* [#6100](https://github.com/gammapy/gammapy/pull/6100) Update installation for windows instruction - Atreyee Sinha
* [#6099](https://github.com/gammapy/gammapy/pull/6099) Backport PR #6098 on branch v2.0.x (Clearer appearance for the click scipts in the documentation) - Lumberbot (aka Jack)
* [#6098](https://github.com/gammapy/gammapy/pull/6098) Clearer appearance for the click scipts in the documentation - Kirsty Feijen
* [#6095](https://github.com/gammapy/gammapy/pull/6095) jupytext requires plt.show - Kirsty Feijen
* [#6094](https://github.com/gammapy/gammapy/pull/6094) Fix release notes for v2.0 - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6118](https://github.com/gammapy/gammapy/issues/6118) Inconsisten edge unit/type for MapTimeAxis - Tomas Bylund
* [#6117](https://github.com/gammapy/gammapy/issues/6117) Mask safe plotted twice in residual panel of count distribution plot - Daniel Morcuende
* [#6114](https://github.com/gammapy/gammapy/issues/6114) When to keep kwargs - Kirsty Feijen
* [#6111](https://github.com/gammapy/gammapy/issues/6111) Upgrade installation instructions - Régis Terrier

 report created at 29/08/2025, 07:23:33
