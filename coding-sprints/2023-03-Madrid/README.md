# Gammapy Coding Sprint / Co-working week, March 2023

* Start: Monday, March 20th, 2023 at 2 pm
* End: Friday, March 24th, 2023 at noon
* Location: UCM Madrid / Online
* Contacts: [AtreyeeS](https://github.com/AtreyeeS), [registerrier](https://https://github.com/github.com/registerrier)

This meeting is a "coding sprint" for people that **want to work on the development** of Gammapy
(http://gammapy.org/). You're very welcome if you're new to coding or haven't contributed to
Gammapy yet. But note that this is **not** a workshop on how to use Gammapy.

Ideally all participants can dedicate most of their time to work on Gammapy during the week and make sure they are available for spontaneous discussions on Slack and remote meetings via Zoom.

A Zoom room will be open the full week.

## Local Logistics

- Will be held in the 3rd floor, EMFTE Seminar room, Faculty of Physics, Univeridad Complutense de Madrid (https://goo.gl/maps/qYJrtAwrBrG3db5j7)
- The closest metro station is Ciudad Universataria, on line 6.

![mapa_ucm](https://user-images.githubusercontent.com/32677370/225902054-c6f466e7-e5d8-455d-ad90-25b71617553f.jpg)

A more zoomed out map can be found here: https://www.ucm.es/plano-ucm


- To access the room, enter the Fisica Building, take the stairs, first room on the left on the 3rd floor.
- Lunch at the canteen on the basement



## Agenda


### Monday 
##### Afternoon session (2 pm): Kick-off
* Introduction to the coding sprint - [slides](coding_sprint_intro.pdf)
  * Preparation of the Roadmap for v2 -  [#4388](https://github.com/gammapy/gammapy/pull/4388) 
  * Preparation of the CTAO SDC - Fabio - [slides](SDC_summary_models_fabio.pdf)
  * Possible high level analysis utilities - Quentin
  * Pulsar analysis - Alvaro & Maxime
  * Gammapy data model definition - Régis

* Paper working session
  * Status - Axel

### Tuesday

##### Morning session 

* 10 am: Discussion on event types, Tarek and Juan

### Wednesday

* 4 pm: paper session

### Thursday 

* 11 am: IRF models, Katrin

* 5 pm: paper session

* 6 pm: paper submission to A&A

* 9 pm: Group photo to celebrate the day! And thanks to Axel for the work on the paper.

![20230323_214946.jpg](https://user-images.githubusercontent.com/16781593/227476626-307399f1-3a7d-44b4-a51b-a8d05a38136b.jpg)


### Friday 

#### Close-out session: 2 pm

* 21 PRs opened this week
* 15 with v1.1 milestone, 6 with v1.0.2 milestone

##### Bug
* Obs filter live time [#4394](https://github.com/gammapy/gammapy/pull/4394) - Maxime
* Iminuit output [#4393](https://github.com/gammapy/gammapy/pull/4393) - Bruno
* Fix issue in metadata when using RegionNDMap.write [#4403](https://github.com/gammapy/gammapy/pull/4403) - Fabio
  * Backport? 
* Check of the time system information of the DataStore [#4399](https://github.com/gammapy/gammapy/pull/4399) - Bruno 
  * Should it go in v1.0.x?
* Merged: Fix plot_spectrum_datasets_off_regions with too many regions [#4397](https://github.com/gammapy/gammapy/pull/4397) - Bruno
##### Feature
###### Data
* Allow to load observations with only IRFs defined [#4280](https://github.com/gammapy/gammapy/pull/4280) - Quentin
###### Makers
* Adding rad max cut in PhaseBackgroundMaker [#4352](https://github.com/gammapy/gammapy/pull/4352) - Maxime
###### Datasets
* Add a livetime map on dataset [#4407](https://github.com/gammapy/gammapy/pull/4407) - Atreyee
###### Models 
* LightCurveTemplateModel serialisation [#4412](https://github.com/gammapy/gammapy/pull/4412) - Atreyee
* Update the evaluate_timevar_source function in MapDatasetEventSampler [#4418](https://github.com/gammapy/gammapy/pull/4418) - Fabio
###### Maps
* adding from_stack and append to LabelMapAxis [#4417](https://github.com/gammapy/gammapy/pull/4417) - Maxime
###### Estimators
* Expose more methods in ExcessMapEstimator [#4414](https://github.com/gammapy/gammapy/pull/4414) - Quentin
###### Plotting
* Add a function that plot the npred_signal of models of a dataset [#4409](https://github.com/gammapy/gammapy/pull/4409) - Maxime
* Add the possibility to plot in MJD the light curves [#4395](https://github.com/gammapy/gammapy/pull/4395) - Bruno
* plot function for 1D distribution of map data [#4408](https://github.com/gammapy/gammapy/pull/4408) - Maxime
##### Performance
* Support for parallel evaluation in FluxPointsEstimator [#4402](https://github.com/gammapy/gammapy/pull/4402) - Quentin
* Support for parallel evaluation in LightCurveEstimator [#4404](https://github.com/gammapy/gammapy/pull/4404) - Quentin
* Add configuration and helper function to run multiprocessing or ray  [#4406](https://github.com/gammapy/gammapy/pull/4406) - Quentin
##### Infrastructure
* Add profilers to dev environment [#4398](https://github.com/gammapy/gammapy/pull/4398) - Quentin
* Merged: Impose maximal ipywidget version [#4400](https://github.com/gammapy/gammapy/pull/4400) - Régis
##### Documentation
* Pulsar analysis tutorial [#4369](https://github.com/gammapy/gammapy/pull/4369) - Maxime & Alvaro
* Small notice for beginner in the tutorials page [#4391](https://github.com/gammapy/gammapy/pull/4391) - Bruno
* Adding more documentation on datasets docstring [#4405](https://github.com/gammapy/gammapy/pull/4405) - Maxime
##### PIG
* PIG 26 - Roadmap for v2.0 [#4388](https://github.com/gammapy/gammapy/pull/4388) 

## Participants

### On-site

1. Atreyee Sinha, UCM, Madrid, Spain ([AtreyeeS](https://github.com/AtreyeeS))
2. Régis Terrier, APC Paris, France ([registerrier](https://github.com/registerrier))
3. Bruno Khélifi, APC Paris, France ([bkhelifi](https://github.com/bkhelifi))
4. Daniel Morcuende, UCM, Madrid, Spain ([morcuended](https://github.com/morcuended))
5. Maxime Regeard, APC, Paris, France ([MRegeard](https://github.com/MRegeard))
6. Alvaro Mas, UCM, Madrid, Spain ([alvmas](https://github.com/alvmas))
7. Quentin Remy, MPIK Heidelberg, Germany ([QRemy](https://github.com/QRemy))
8. Juan Bernete, CIEMAT, Spain ([JBernete](https://github.com/JBernete))
9. Tarek Hassan, CIEMAT, Spain ([TarekHC](https://github.com/TarekHC))

X. Please add your name and GitHub name here...

### Online

1. Tim Unbehaun, ECAP, Erlangen, Germany ([tunbehaun273](https://github.com/tunbehaun273))
2. Fabio Pintore, INAF/IASF Palermo, Italy ([fabiopintore](https://github.com/fabiopintore))
3. Abelardo Moralejo, IFAE, Barcelona, Spain
4. Silvia Crestan, INAF-IASF Milano, Italy ([screstan](https://github.com/screstan))
5. Cosimo Nigro, IFAE, Barcelona, Spain ([cosimoNigro](https://github.com/cosimoNigro))
6. Axel Donath, CfA, Cambridge, US ([adonath](https://github.com/adonath)) (sparse participation...)

X. Please add your name and GitHub name here
