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
- User contributed notebooks / tutorials (Bruno leads discussion) - Conclusions report:
    - Decision to create a web interface to have 'user contribution example', being either a notebook or a python script
    - Goals:
        - Sharing of the users experience
        - Offer some visibility to contributors with a visible author list (and index on the web page) and a possible associated DOI via Zenodo
    - These contributions are from users and are not the official gammapy tutorials:
        - They can be science related (e.g. transcient simulations), technical (e.g. MCMC fit with Naima) or multi-instrument (e.g. HAWC, Fermi-LAT, XMM, etc)
        - Any topics will be accepted.
        - An acceptance by the lead developers (via a PR) will permit to make a basic control (e.g. duplication).
        - Quality standards would be much lower than for our “official” tutorials.
        - The maintenance scheme might evolve with time. Today, the proposal is that we maintain them with only the latest stable version.
    - We will provide:
        - the infrastructure to present contributions on a dedicated web page, like the [astropy page](http://learn.astropy.org/tutorials.html)
        - the infrastructure to test the notebooks, if there are testable (e.g. existence of the data).
        - the guidelines for users how to do a contribution (e.g. [astropy guidelines](http://learn.astropy.org/contributing.html)).
    - Objectives:
        - Creation of the web page, its integration in our web pages (https://gammapy.org and https://docs.gammapy.org) for september.
        - Creation of the associated guidelines, the metadata used to make web search, for the Continuous Integration, the templates.
        - Some foreseen notebook contributions: Light curves simulations of transient sources (Jean-Philippe L. et al.), statistics (Atreyee), Background model creation (Régis?), MCMC Naima fit (Fabio?), GPS (Quenty?).
         
### Wednesday 10h00:
- Refactor `SpectrumDataset` to use `EDispKernelMap` (Régis)
- Open an issue in iminuit and ask about a better behaviour for https://github.com/gammapy/gammapy/issues/2917. Keep the simple check in https://github.com/gammapy/gammapy/pull/2937 on the Gammapy side, not handling any tolerance. (Luca)
- Improve the modeling / fitting tutorial to show likelihood profiles for all parameters (https://docs.gammapy.org/0.17/notebooks/modeling.html#Inspecting-fit-statistic-profiles) and emphasize the importance of checking likelihood profiles (Luca)
- Modify the "analysis 2" notebook to compute a Li & Ma or TS residual signifiance map as well (Luca)
- Take into account `mask_safe` in `.to_image()` and `.to_spectrum_dataset()` etc. (Atreyee)
- Modify the `ExcessMapEstimator` and `TSMapEstimator` to take into account the `mask_fit`, so that we get equivalent behaviour for all `Estimator` and `Fit` classes (needs a bit more discussion...)
- Finish Models PIG and provide usage examples for the two possibilities of the global Model API for discussion this afternoon (Axel)
- Implement shorter YAML tags and missing models (Quentin)


### Wednesday 17h00:
- Global model API discussion

### Thursday 10h00:
- Quick report by everyone
 
### Friday 10h00:
- Quick report by everyone

### General coding projects (no particular order...):
#### General
- Finish open PRs: https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A0.18

#### API
- Change `SpectrumDataset.edisp` to a `EDispMap` (Régis)
- Remove `IRFStacker` (Régis / Axel)
- Introduce shorter YAML tags (Quentin)
- Refactor spectral absorption model
- Remove `MapDataset.background_model` (Axel)
- Further unifiy `Estimator` API: `n_sigma` arguments and `steps` handling (Régis / Axel) - [Bruno's report](slides/EstimatorsNote.pdf)
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
- Write RST pages for new sub-packages (Axel, Régis)
- Add documentation on `RegionGeom` and `RegionNDMap` (Axel)
- Resolve content duplication between tutorials / RST 
- Fix ring-background tutorial (Atreyee)
- Add example how to make a theta^2 plot (Lea, Manuel, Chaitanya?)

#### Validation and testing
- Update and finish validation of DR1-DL3, CTA 1DC, 3FHL etc.
- Check `EDispKernelMap` validation
- Add ring analysi to validation (Atreyee)

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
