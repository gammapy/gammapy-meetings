# Gammapy Developer Meeting 
 * Friday, June 13, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
## Agenda
- ~~Presentation on Veritas gammapy tutorial - Samantha Wong~~ postponed to next week
- Discussion on organization - All
- Activity report - All 

## Minutes

### Meeting organization
* Regis suggest that the automatic page for the dev meetings be created in more in advance than friday morning so one can add an agenda ahead of time.
* We had a discussion about creating fixed points in the agenda to structure the discussions on the meetings, for example having a point about reviewing the status the bugs so they are tracked and not forgotten untill shortly before release.
* Atreyee suggests all bugs get assigned to a lead dev, who is then responsible of tracking that bug and ensure someone gets around to solving it
* Regis mentions a similar thing could be used for tracking feature requests, there are currently 47 feature requests.
* Bruno suggests the following recurring agenda items

    - bugs

    - documentation

    - devops

    - ongoing projects (sensi, HLI, MWL, etc)

    - open issues

    - validation & benchmarks


* Bruno remarks that it makes sense if IKC partners shoulders some of work coordinating these points
* For next week: review the proposed release schedule for CTAO SUSS Science Analysis Tools, Bruno presents.

### DevOps
* Regis presents on a CI issue on windows, it seems the runners use a new version of windows which changed the default drive name. After restructuring the CI configuration the problem was solved.
* The CI sphinx-build jobs have been very slow, partly due to the linkcheck process. Because the outcome of that test was largely ignored, Hanna Stapel suggest making the linkcheck to a separate CI job that runs regularly PR [#5912](https://github.com/gammapy/gammapy/pull/5912) .

### Recent issues
* Problems with the model sampler, Kirsty discovered it doesn't work on models with linked parameters. A fix required several steps, taken with:
    - PR [#5913](https://github.com/gammapy/gammapy/pull/5913) - Fabio
    - PR [#5914](https://github.com/gammapy/gammapy/pull/5914) - Fabio
    - PR [#5915](https://github.com/gammapy/gammapy/pull/5915) - Quentin
* Fabio demonstrates a bug where models with linked parameters doesn't always show that parameters are linked when printed.
  - Quentin proposes the following fix [#5916](https://github.com/gammapy/gammapy/pull/5916)
* Regis requests a report about the solution for the sampler and any open questions linked to this issue next week. Fabio volunteers to report back.

* [#5909](https://github.com/gammapy/gammapy/issues/5909) A strange issue about warnings when using `.peek` on `EffectiveArea2D`. Tomas investigates

### Internal gammapy.data model : associated refactoring of gammapy.makers 
* Regis presents a re-factoring of makers and observation to handle FoV coordinate transform and would like to have it reviewed. [#5911](https://github.com/gammapy/gammapy/pull/5911). 

### Sensitivity: computing correct ts conversion for the Asymov dataset
* A discussion about issue  [#5891](https://github.com/gammapy/gammapy/issues/5891) that I I couldn't follow. 

### Other PR
* Kirsty requests feedback on PR [#5910](https://github.com/gammapy/gammapy/pull/5910)  where a function argument needs a better name

## Activity report 

### PRs opened last week (less than 8 days ago): 
* [#5910](https://github.com/gammapy/gammapy/pull/5910) Change argument name in ul - Kirsty Feijen
* [#5905](https://github.com/gammapy/gammapy/pull/5905) Fix documentation of of the installation - Bruno Khélifi
* [#5904](https://github.com/gammapy/gammapy/pull/5904) Add requires_module decorator - Quentin Remy

### PRs merged last week (less than 8 days ago): 
* [#5907](https://github.com/gammapy/gammapy/pull/5907) Modify GAMMAPY_DATA definition in CI matrix - Régis Terrier
* [#5903](https://github.com/gammapy/gammapy/pull/5903) Add `LogUniformPrior` to registry - Kirsty Feijen
* [#5902](https://github.com/gammapy/gammapy/pull/5902) Remove unused modify_unit_order_astropy_5_3 - Quentin Remy
* [#5901](https://github.com/gammapy/gammapy/pull/5901) Documentation improvement for the case of NaN UL - Bruno Khélifi
* [#5899](https://github.com/gammapy/gammapy/pull/5899) Fix errors in docs - Kirsty Feijen
* [#5896](https://github.com/gammapy/gammapy/pull/5896) Improve docstring of run function for `EnergyDependentMorphologyEstimator` - Kirsty Feijen
* [#5893](https://github.com/gammapy/gammapy/pull/5893) Improve docstring of run function for `SensitivityEstimator` - Kirsty Feijen
* [#5888](https://github.com/gammapy/gammapy/pull/5888) Fix gammapy.catalog to support astropy v7.1 - Quentin Remy
* [#5885](https://github.com/gammapy/gammapy/pull/5885) Update the installation guide in order to reduce the emphasis on Anaconda - Bruno Khélifi
* [#5875](https://github.com/gammapy/gammapy/pull/5875) Export creation metadata on DL3 and DL4 products - Régis Terrier
* [#5860](https://github.com/gammapy/gammapy/pull/5860) Introduce a FoVFrame in gammapy.utils.coordinates - Régis Terrier

### issues opened last week (less than 8 days ago): 
* [#5909](https://github.com/gammapy/gammapy/issues/5909) Warnings when using EffectiveArea2D.peek - Maximilian Linhoff
* [#5908](https://github.com/gammapy/gammapy/issues/5908) Sampler fails when you have linked parameters - Kirsty Feijen
* [#5906](https://github.com/gammapy/gammapy/issues/5906) FluxPoints doesn't properly handle a negative spectral model amplitude - Samantha Wong

