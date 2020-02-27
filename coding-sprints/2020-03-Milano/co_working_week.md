# Gammapy Co-Working Week, March 2020

Instead of the planned coding sprint in Milano, we have a "Gammapy co-working week" from 2nd to 6th March 2020.  Ideally all participants can dedicate most of your time to work on Gammapy during the week and make sure they are available for spontaneous discussions on Slack and remote meetings via Vibe. 

In between communication via Slack: https://gammapy.slack.com (#dev channel)

## Agenda

Monday afternoon 14h00: kick off meeting with presentations on Vibe

### Presentations:
- Axel: Introduction and overview
- Axel: Model handling
- Fabio: Event sampling status (validation and missing features)
- Atreyee: Temporal model evaluation
- Régis: FluxEstimator idea and plans
- Régis: User testing feedback status and missing work

### Rest of the week every day:
- 10h00 regular status meeting on Vibe 


### General coding projects (no particular order...):
- Introduce `EDispKernelMap`
- Refactor `SpectrumDataset` and `SpectrumDatasetOnOff` to use RegionNDMap
- Introduce `gammapy.estimators` and `gammapy.visualization`
- Move estimator classes to `gammapy.estimators`
- Finish open PRs
- Event sampling:
  - Finish validation
  - Handle temporal models (+ minimal validation)
  - Tutorial and docs
- Temporal models:
  - Add temporal model evaluation to `SkyModel`
  - Add `TemporalModel.plot()` method(s)
  - Add temporal models to model gallery
- Adapt benchmarks / validation to latest master and re-run


### Discussion topics:
- What to do about `gammapy.cube`,  `gammapy.spectrum` and `gammapy.detect`?
- Solve MapDataset meta data problem (requires discussion + proposal)
- Global model and background model handling (requires discussion + proposal)



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
 
