# Gammapy Co-Working Week, July 2020

Instead of the summer coding sprint we have another "Gammapy co-working week" from July 6th to 10th 2020.
Ideally all participants can dedicate most of their time to work on Gammapy during the week and make sure
they are available for spontaneous discussions on Slack and remote meetings via Vibe. 

In between communication via Slack: https://gammapy.slack.com (#dev channel)

## Agenda

### Monday 14h00:
Kick off meeting with presentations on Vibe 14h00

Presentations:
- Axel: Introduction and overview
- Léa: Looking at LST data with Gammapy
- Luca: A full 3D analysis workflow example: HESS J1702 / implications for Gammapy
- Quentin: CTA GPS analysis / implications for Gammapy
- Régis / Atreyee: Summary of feedback on CTA IRFs / implications for Gammapy
- Axel: Models PIG and work distribution

### Tuesday 10h00:
- Quick report by everyone

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
- Change `SpectrumDataset.edisp` to a `EDispMap`
- Remove `IRFStacker`
- Introduce shorter YAML tags
- Refactor spectral absorption model
- Remove `MapDataset.background_model`
- Introduce global model API

#### Features
- Finish  `ExcessProfileEstimator`
- Add missing models
- Implement support for energy dependent spatial models + docs examples

#### Documenation
- Write RST pages for new sub-packages

#### Validation and testing
- Update and finish validation of DR1-DL3, CTA 1DC, 3FHL etc.
- Check `EDispKernelMap` validation

### Discussion topics:
- Solve MapDataset meta data problem (requires discussion + proposal)


## Participants

1. Axel Donath, MPIK Heidelberg, Germany ([adonath](https://github.com/adonath))
2. Régis Terrier, APC Paris, France ([registerrier](https://github.com/registerrier))
3. Atreyee Sinha, LUPM Montpellier, France ([AtreyeeS](https://github.com/AtreyeeS)) 
4. Quentin Remy, MPIK Heidelberg, Germany ([QRemy](https://github.com/QRemy)) 
5. Bruno Khelifi, APC Paris, France ([bkhelifi](https://github.com/bkhelifi)) 
