# Gammapy Co-Working Week, July 2020

Instead of the summer coding sprint we have another "Gammapy co-working week" from July 6th to 10th 2020.
Ideally all participants can dedicate most of their time to work on Gammapy during the week and make sure
they are available for spontaneous discussions on Slack and remote meetings via Vibe. 

In between communication via Slack: https://gammapy.slack.com (#dev channel)

## Agenda

### Monday 14h00:
Kick off meeting with presentations on Vibe 14h00

Presentations:
- Axel: Introduction and overview ([slides](slides/co-working-week-intro.pdf))
- Chaitanya Priyadarshi / Manuel Artero: Looking at LST data with Gammapy ([slides])
- Luca: A full 3D analysis workflow example: HESS J1702 / implications for Gammapy ([slides])
- Quentin: CTA GPS analysis / implications for Gammapy ([slides])
- Régis / Atreyee: Summary of feedback on CTA IRFs / implications for Gammapy ([link](slides/cta-irf.md)
- Axel: Coding Projects

### Tuesday 10h00:
- User contributed notebooks / tutorials (Bruno leads discussion)

### Wednesday 10h00:
- Quick report by everyone

### Thursday 10h00:
- Quick report by everyone
 
### Friday 10h00:
- Quick report by everyone

### General coding projects (no particular order...):
#### General
- Finish open PRs: https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A0.18

#### API
- Change `SpectrumDataset.edisp` to a `EDispMap` (Régis?)
- Remove `IRFStacker` (Régis / Axel)
- Introduce shorter YAML tags (Quentin)
- Refactor spectral absorption model
- Remove `MapDataset.background_model` (Axel)
- Further unifiy `Estimator` API: `n_sigma` arguments and `steps` handling (Régis / Axel)
- Introduce global model API...probably wait for PIG-20

#### Features
- Finish  `ExcessProfileEstimator` (Bruno)
- Add missing models (Quentin)
  - BrokenPowerLaw
  - PiecwiseBrokenPowerLaw
  - SersicSpatialModel
- Implement support for energy dependent spatial models + docs examples (Atreyee?)
- Simple model management functionality (Quentin) 


#### Bugs and Fixes
- Clean up MapDataset.to_image() (Atreyee)
- Fix MapDatasetOnOff.from_MapDataset() psf dropping - need to check effect on Ring Background Analysis (Atreyee)
- Improve speed of `Map.get_spectrum()`, by using cutout
- Replace use of lru_cache(), that works with multiprocessing (Quentin)


#### Documenation
- Write RST pages for new sub-packages (Axel, Regis)
- Add documentation on `RegionGeom` and `RegionNDMap` (Axel)
- Resolve content duplication between tutorials / RST 
- Fix ring-background tutorial (Atreyee)
- Add example how to make a theta^2 plot (Lea, Manuel, Chaitanya?)

#### Validation and testing
- Update and finish validation of DR1-DL3, CTA 1DC, 3FHL etc.
- Check `EDispKernelMap` validation
- Add ring analysi to validation

### Discussion topics:
- User contributed notebooks
- Global model API
- Plotter API / residual maps computation API
- Logging output (...provenance)

## Participants

1. Axel Donath, MPIK Heidelberg, Germany ([adonath](https://github.com/adonath))
2. Régis Terrier, APC Paris, France ([registerrier](https://github.com/registerrier))
3. Atreyee Sinha, LUPM Montpellier, France ([AtreyeeS](https://github.com/AtreyeeS)) 
4. Quentin Remy, MPIK Heidelberg, Germany ([QRemy](https://github.com/QRemy)) 
5. Bruno Khelifi, APC Paris, France ([bkhelifi](https://github.com/bkhelifi)) 
