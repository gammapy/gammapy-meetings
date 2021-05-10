# Gammapy Co-Working Week, May 2021

Instead of the spring coding sprint we have another "Gammapy co-working week" from May 3rd to May 7th 2022.
Ideally all participants can dedicate most of their time to work on Gammapy during the week and make sure
they are available for spontaneous discussions on Slack and remote meetings via Zoom.

A Zoom room is open for the full week. ID: 837 3792 5932

The password will be given on Slack (#dev channel).

In between communication via Slack: https://gammapy.slack.com (#dev channel)

For this co-working week we will put a strong focus on coding wrapping up the Gammapy release candidate for v1.0.
Only few discussions and coding, coding and coding instead...

## Group Photo
![group-photo-co-working-may-2021](https://user-images.githubusercontent.com/3715928/117621247-b1f55c00-b171-11eb-936a-77c078587ed2.jpg)


## Issues to work on

In general just check the v0.19 milestone: https://github.com/gammapy/gammapy/issues?q=is%3Aopen+is%3Aissue+milestone%3Av0.19

Here is a list of some selected issues to work on:
- https://github.com/gammapy/gammapy/issues/3271
- https://github.com/gammapy/gammapy/issues/3240 (Fabio)
- https://github.com/gammapy/gammapy/issues/3118
- https://github.com/gammapy/gammapy/issues/2913 (Atreyee)
- https://github.com/gammapy/gammapy/issues/2704 (Fabio)
- https://github.com/gammapy/gammapy/issues/2442 (Axel)
- https://github.com/gammapy/gammapy/issues/2434 (Axel)
- https://github.com/gammapy/gammapy/issues/3004
- https://github.com/gammapy/gammapy/issues/3324 (Fabio)
- Glossary entry for FoV/ ROI (Luca)
- Validate Crab HEALPix analysis (Vikas + Laura)
- Debug FP convergence issue with Jean

## Short discussions
- https://github.com/gammapy/gammapy/issues/2353
-

## Agenda

### Monday 14h00:
Kick off meeting with presentations on Zoom 14h00

Presentations:
- **Axel**: Introduction and overview (5 min.)
- **Jose Enrique**: not only gammapy code (10 min.) ([slides](slides/devops.pdf))


Work topics:

- finish open PRs! (everyone)
- gammapy.irf docs (Atreyee)
- event selection docs (Laura)
- flux points class (Axel)
- docs tests (José Enrique)
- edisp convolution caching (Quentin)
- datasets API notebook (Quentin)

### Tuesday:

**9h30**
- FP convergence issue (Régis, Axel)
- Review open PRs (Axel)
- https://github.com/gammapy/gammapy/issues/2704 (Fabio P.)
- Code meta JSON / CITATION files / Docker setup (José Enrique)
- Finish find_roots PR / Update estimators in benchmarks (Quentin) 

**16h30**


### Wednesday:
**9h30**
- Docker PR https://github.com/gammapy/gammapy/pull/3339 (José Enrique)
- FP convergence issue (Régis)
- HEALPix co-working session (Laura, Axel, ...)
- Review open PRs (Axel, Régis)
- Check DL3 optional meta data access (Atreyee, ...)
- https://github.com/gammapy/gammapy/issues/2704 (Fabio P.)


**16h30**

### Thursday:
**9h30**
- Docker / meta data discussion (José Enrique, Axel, Bruno, Regis, Quentin)

**16h30**
- Edisp caching (Quentin)
- HPX dataset fit validation (Laura) 


### Friday 9h30:
- Work planning
- Edisp caching profiling (Axel / Quentin)
- Flux points/ estimate discussion session (Régis / Axel / Quentin)
- Cached counts fix: either remove or implement update mechanism or unify map dtype or cython (?)
- Kernel radius TS map estimator https://github.com/gammapy/gammapy/issues/3004 (Régis / Axel / Quentin, requires checking...)
- HPX npred computation PR & testing (Laura / Vikas)
- Fix broken doc links, doc tests, see https://github.com/gammapy/gammapy/issues/3143 (José Enrique)
- CITATION.cff and `cffconvert` (wait for feedback, com back to it next week) (José Enrique / Bruno?)
- Implement `Map.plot_mask()` (Fabio P.)


### Friday 15h00:
- Close out meeting
- "Group photo" (screenshot)


## Participants
1. Axel Donath, MPIK Heidelberg, Germany ([adonath](https://github.com/adonath))
2. Régis Terrier, APC Paris, France ([registerrier](https://github.com/registerrier))
3. Atreyee Sinha, LUPM Montpellier, France ([AtreyeeS](https://github.com/AtreyeeS))
4. Quentin Remy, MPIK Heidelberg, Germany ([QRemy](https://github.com/QRemy))
5. Bruno Khelifi, APC Paris, France ([bkhelifi](https://github.com/bkhelifi))
6. Jose Enrique Ruiz, IAA-CSIC Granada, Spain ([bultako](https://github.com/bultako))
7. Laura Olivera Nieto, MPIK Heidelberg, Germany ([LauraOlivera](https://github.com/LauraOlivera))
8. Fabio Pintore, INAF/IASF Palermo, Italy ([fabiopintore](https://github.com/fabiopintore))
9. Fabio Acero, CEA Saclay, France ([facero](https://github.com/facero))
10. Luca Giunti, APC Paris / CEA Saclay, France ([luca-giunti](https://github.com/luca-giunti))
11. Vikas Joshi, ECAP Erlangen, Germany ([vikasj78](https://github.com/vikasj87))
12. Catherine Boisson, Obs Paris
