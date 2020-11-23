# Gammapy Co-Working Week, November 2020

Instead of the autumn coding sprint we have another "Gammapy co-working week" from Nov 23rd to 27th 2020.
Ideally all participants can dedicate most of their time to work on Gammapy during the week and make sure
they are available for spontaneous discussions on Slack and remote meetings via Zoom. 

A Zoom room is open for the full week. ID: 837 3792 5932

The password will be given on Slack (#dev channel).

In between communication via Slack: https://gammapy.slack.com (#dev channel)

For this co-working week we will put a string focus on documentation!

## Agenda

### Monday 14h00:
Kick off meeting with presentations on Zoom 14h00

Presentations:
- **Axel**: Introduction and overview (5 min.) ([slides](slides/co-working-week-intro.pdf))
- **Laura**: HAWC analysis with Gammapy & proposed features (10 + 5 min.) ([slides](slides/))
- **Valentina**: Real time analysis requirements (10 + 5 min.) ([slides](slides/))
- **Quentin**: Model management, fit strategies & various ideas inspired from the CTA GPS analysis (10 + 5 min.) ([slides](slides/))
- **Régis**: PIG 22, unified estimator result object (10 + 5 min.) ([slides](slides/))
- **José Enrique**: Ideas docs and release workflow improvements (10 + 5 min.) ([slides](slides/))
- **Axel**: Remaing work for v1.0 / coding projects for the week (10 + 5 min.) ([slides](slides/))

### Tuesday 10h00 / 17h00:
- Quick report by everyone
         
### Wednesday 10h00 / 17h00:
- **Atreyee**: First results from the user feedback form (5 + 5 min.) ([slides](slides/))
- Quick report by everyone

### Thursday 10h00 / 17h00:
- Quick report by everyone
- "Group photo" (screenshot)
 
### Friday 10h00:
- Quick report by everyone

### Friday 15h00:
- Close out meeting

### General coding projects (no particular order...):


#### General
- Finish open PRs: https://github.com/gammapy/gammapy/pulls 
- Prototype for a real time analysis?
- Decide on final API changes
- Move from Travis-CI to github actions

#### Documenation
- Move API tutorials to the corresponding sub-packages and build "in place"
- Simplify data download: remove index files and use a single tar file instead?
- Simplify notebook download: remove index files and use a single tar file at the top of the tutorials page instead?
- Resolve content duplication between tutorials / RST 
- Write RST pages for new sub-packages (Axel, Régis)
- Add documentation on `RegionGeom` and `RegionNDMap` (Axel)
- Further improve IRF documentation
- User contributed notebooks?

#### Validation and testing
- Update and finish validation of DR1-DL3, CTA 1DC, 3FHL etc.
- Move CI setup to github workflows?

#### API
- Merge `SpectrumDataset` and `MapDataset`?
- Make `Fit` class configurable, so that users can choose backends for flux points estimation.
- Remove support for `EDispKernel` in `MapDataset`
- Remove `BackgroundModel` and support the use case via `TemplateSpatialModel`?

#### Features
- Model management functionality, such as `Models.select()` and `Parameters.freeze(type="spatial")`, lets 
- Unified flux points handling (see PIG 22)
- Implement `EDispEnergyScaleModel`?

#### Bugs and Fixes
- TBD

### Discussion topics:
- Model book-keeping in `MapDataset.to_image()`, `MapDataset.to_spectrum_dataset()` etc. methods. Should we rely on `.npred_background()`? 


## Participants
1. Axel Donath, MPIK Heidelberg, Germany ([adonath](https://github.com/adonath))
2. Régis Terrier, APC Paris, France ([registerrier](https://github.com/registerrier))
3. Atreyee Sinha, LUPM Montpellier, France ([AtreyeeS](https://github.com/AtreyeeS)) 
4. Quentin Remy, MPIK Heidelberg, Germany ([QRemy](https://github.com/QRemy)) 
5. Bruno Khelifi, APC Paris, France ([bkhelifi](https://github.com/bkhelifi)) 
6. Jose Enrique Ruiz, IAA-CSIC Granada, Spain ([bultako](https://github.com/bultako)) 
7. Laura Olivera Nieto, MPIK Heidelberg, Germany ([LauraOlivera](https://github.com/LauraOlivera)) 
8. Fabio Pintore, INAF/IASF Palermo, Italy ([fabiopintore](https://github.com/fabiopintore))
9. Valentina Fioretti NAF OAS Bologna, Italy ([vfioretti](https://github.com/vfioretti))
10. Fabio ACERO, CEA/Saclay, France ([facero](https://github.com/facero))
11. Giovanni De Cesare INAF/OAS Bologna Italy ([giovixo](https://github.com/giovixo))
12. Giulia Stratta INAF/OAS Bologna Italy ([gistratta](https://github.com/gistratta))
13. Ambra Di Piano INAF/OAS Bologna Italy ([ambra-dipiano](https://github.com/ambra-dipiano))

