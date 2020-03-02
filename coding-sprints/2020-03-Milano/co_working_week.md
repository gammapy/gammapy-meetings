# Gammapy Co-Working Week, March 2020

Instead of the planned coding sprint in Milano, we have a "Gammapy co-working week" from 2nd to 6th March 2020.  Ideally all participants can dedicate most of their time to work on Gammapy during the week and make sure they are available for spontaneous discussions on Slack and remote meetings via Vibe. 

In between communication via Slack: https://gammapy.slack.com (#dev channel)

## Agenda

Monday afternoon 14h00: kick off meeting with presentations on Vibe.
- Meeting ID: 7754787364
- https://vibe.ezuce.com/launcher/?meetingID=7754787364


### Presentations:
- Axel: Introduction and overview ([slides](slides/intro-co-working-week.pdf))
- Fabio: Event sampling status (validation and missing features) ([slides](slides/))
- Atreyee: Temporal model evaluation ([slides](slides/))
- Régis: FluxEstimator idea and plans ([slides](slides/))
- Régis: User testing feedback status and missing work ([slides](slides/))

### Rest of the week every day:
- 10h00 regular status meeting on Vibe 

#### Tuesday 10h00:
 - Axel: Model handling ([slides](slides/))


### General coding projects (no particular order...):
#### General
- Finish open PRs: https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A0.17

#### API
- Refactor `SpectrumDataset` and `SpectrumDatasetOnOff` to use RegionNDMap
- Introduce `gammapy.estimators` and `gammapy.visualization`
- Move estimator classes to `gammapy.estimators`

#### Features
- Introduce `EDispKernelMap`
- Add temporal model evaluation to `SkyModel`
- Add `TemporalModel.plot()` method(s)
- Handle temporal models (+ minimal validation)

#### Documenation
- Write RST pages for new sub-packages
- Finish uniform presentation of notebooks
- Document event sampling

#### Validation and testing
- Finish event sampling validation
- Update and finish validation of DR1-DL3, CTA 1DC, 3FHL etc.

### Discussion topics:
- What to do about `gammapy.cube`,  `gammapy.spectrum` and `gammapy.detect`? (quick discussion, decisiion and implementation in the same week)
- Solve MapDataset meta data problem (requires discussion + proposal)
- Global model, background model handling and energy dependent spatial models (requires discussion + proposal)
- Makers class


## Participants

1. Axel Donath, MPIK Heidelberg, Germany ([adonath](https://github.com/adonath))
2. Fabio Pintore,  ([fabiopintore](https://github.com/fabiopintore))
3. Régis Terrier, APC Paris, France ([registerrier](https://github.com/registerrier))
4. Luca Giunti, APC-CEA Paris, France ([luca-giunti](https://github.com/luca-giunti))
5. Christopher van Eldik, ECAP, Germany
6. Jose Enrique Ruiz, IAA-CSIC, Granada, Spain ([Bultako](https://github.com/Bultako))
7. Bruno Khelifi, APC, Paris, France ([bkhelifi](https://github.com/bkhelifi))
8. Giovanni De Cesare, Bologna, Italy ([giovixo](https://github.com/giovixo))
9. Atreyee Sinha, LUPM Montpellier, France ([AtreyeeS](https://github.com/AtreyeeS))
 
