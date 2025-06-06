# Gammapy Developer Meeting 
 * Friday, June 06, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
# Agenda

### PRs opened last week (less than 8 days ago): 
* [#5905](https://github.com/gammapy/gammapy/pull/5905) Fix documentation of of the installation - Bruno Khélifi
* [#5904](https://github.com/gammapy/gammapy/pull/5904) Add requires_module decorator - Quentin Remy
* [#5903](https://github.com/gammapy/gammapy/pull/5903) Add `LogUniformPrior` to registry - Kirsty Feijen
* [#5902](https://github.com/gammapy/gammapy/pull/5902) Remove unused modify_unit_order_astropy_5_3 - Quentin Remy
* [#5900](https://github.com/gammapy/gammapy/pull/5900) Support for workflow step products  - Quentin Remy
* [#5898](https://github.com/gammapy/gammapy/pull/5898) Add stacking functionality to `LightCurveEstimator` - Kirsty Feijen
* [#5897](https://github.com/gammapy/gammapy/pull/5897) Examples for estimator utils - Kirsty Feijen
* [#5896](https://github.com/gammapy/gammapy/pull/5896) Improve docstring of run function for `EnergyDependentMorphologyEstimator` - Kirsty Feijen
* [#5894](https://github.com/gammapy/gammapy/pull/5894) Adapt plot function default labels - Kirsty Feijen
* [#5892](https://github.com/gammapy/gammapy/pull/5892) Improve docstring of run function for `ParameterEstimator` and `ParameterSensitivityEstimator` - Kirsty Feijen
* [#5889](https://github.com/gammapy/gammapy/pull/5889) Adapt intructions for static figures - Kirsty Feijen
* [#5888](https://github.com/gammapy/gammapy/pull/5888) Fix gammapy.catalog to support astropy v7.1 - Quentin Remy
* [#5886](https://github.com/gammapy/gammapy/pull/5886) Improve HowTo page titles (#5839) - Gnana Sindhu

### PRs merged last week (less than 8 days ago): 
* [#5901](https://github.com/gammapy/gammapy/pull/5901) Documentation improvement for the case of NaN UL - Bruno Khélifi
* [#5899](https://github.com/gammapy/gammapy/pull/5899) Fix errors in docs - Kirsty Feijen
* [#5895](https://github.com/gammapy/gammapy/pull/5895) CI fix : no yield in tests - Quentin Remy
* [#5893](https://github.com/gammapy/gammapy/pull/5893) Improve docstring of run function for `SensitivityEstimator` - Kirsty Feijen
* [#5890](https://github.com/gammapy/gammapy/pull/5890) Fix CTA error - Kirsty Feijen
* [#5885](https://github.com/gammapy/gammapy/pull/5885) Update the installation guide in order to reduce the emphasis on Anaconda - Bruno Khélifi
* [#5884](https://github.com/gammapy/gammapy/pull/5884) Rm setting log levels in modules - Tobi Preis

### issues opened last week (less than 8 days ago): 
* [#5891](https://github.com/gammapy/gammapy/issues/5891) Asimov TS to Sigma conversion wrong - Stefan Fröse
* [#5887](https://github.com/gammapy/gammapy/issues/5887) Make a technical tutorial about metadata handling - Bruno Khélifi

# Minutes

* Regis presented a PR introducing a FoVFrame to simplify internal API and demonstrated how this could potentially support drift-mode observations.
 [#5860](https://github.com/gammapy/gammapy/pull/5860)
* Kirsty opened several PRs that add docstrings to several `.run()` functions as well as improving some docs, reviews welcome.
* Atreyee raised the issue that the HOWTO section is hard to navigate, some suggested solutions emerged
    * Remove some HOWTOS
    * Split up into subsections
    * Create a separate "Example" category
* Quentin fixed a regression for Astropy 7.1, which required regenerating some test datafiles. 
* Kirsty provided a PR for function default labels but was not entirely happy with the solution. It was accepted as good enough for now, but a porper plotting class could be created in the future.
* Samantha will present the Veritas gammapy tutorial next week.

## Upper limit calculations
Samantha Wong and Matthew Lundy has had problems getting upper limits when trying to place differential limits on what is likely empty fields, the issue arrises when the excess happens to be negative. In that case the reference flux calculated is negative which breaks hardcoded assumptions and limits aren't produced.

It is somewhat surprising that this issue has not been highligted previously, it could be because Veritas is trying to use gammapy for all analysis while in other experiments it as been applied mainly to fields where there is some signal.

Discussion on how to handle it produces two suggestions
* Emit a warning whenever the reference model has a negative norm to let the user know they need to make a choice
* Update the code so it produces upper limits also when the norm is negative (even if this is perhaps not the most apropriate Upper Limit)

## Workflow step PR
The analysis class is being refactored into a workflow composed of several steps, hopefully this will allow for more parallelism.

The PR [#5900](https://github.com/gammapy/gammapy/issues/5900) introduces a `Product` class to store intermediate results in the steps instead of storing them inside the worflow class, making for looser coupling easing paralell execution of separate steps.

This work will now be split into several smaller PRs because the current one is a bit hard to follow.
