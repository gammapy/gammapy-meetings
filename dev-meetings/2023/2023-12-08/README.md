# Gammapy Developer Meeting 
 * Friday, December 08, 2023, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
# Agenda

### PRs opened last week (less than 8 days ago): 
* [#4964](https://github.com/gammapy/gammapy/pull/4964) Adapt accordion id in HowTo - Astro-Kirsty
* [#4963](https://github.com/gammapy/gammapy/pull/4963) Expose remaining `utils` functions in API - Astro-Kirsty
* [#4961](https://github.com/gammapy/gammapy/pull/4961) Example in docstring of `select_nested_models` - Astro-Kirsty
* [#4951](https://github.com/gammapy/gammapy/pull/4951) BLD: cleanup unused build-time dependencies - Clément Robert
* [#4942](https://github.com/gammapy/gammapy/pull/4942) Parallel support for FluxProfileEstimation - Quentin Remy

### PRs merged last week (less than 8 days ago): 
* [#4965](https://github.com/gammapy/gammapy/pull/4965) Expose more features useful for UL computation - Quentin Remy
* [#4960](https://github.com/gammapy/gammapy/pull/4960) Backport pull request #4956 : release notes for v1.0.2 - Régis Terrier
* [#4959](https://github.com/gammapy/gammapy/pull/4959) Backport PR #4956 on v1.0.x: changelog for v1.0.2 - Régis Terrier
* [#4958](https://github.com/gammapy/gammapy/pull/4958) Backport PR #4956 on branch v1.1.x (Prepare release notes for v1.0.2) - Lumberbot (aka Jack)
* [#4957](https://github.com/gammapy/gammapy/pull/4957) Update CITATION.cff for v1.0.2 release - Régis Terrier
* [#4956](https://github.com/gammapy/gammapy/pull/4956) Prepare release notes for v1.0.2 - Régis Terrier
* [#4955](https://github.com/gammapy/gammapy/pull/4955) Backport PR #4940 on branch v1.1.x (Fix MapEvaluator for the apply_edisp=False case) - Lumberbot (aka Jack)
* [#4954](https://github.com/gammapy/gammapy/pull/4954) Backport PR #4936 on branch v1.1.x (PiecewiseNormSpectralModel serialising interp) - Lumberbot (aka Jack)
* [#4953](https://github.com/gammapy/gammapy/pull/4953) Backport PR #4936 on branch v1.0.x (PiecewiseNormSpectralModel serialising interp) - Lumberbot (aka Jack)
* [#4949](https://github.com/gammapy/gammapy/pull/4949) BLD: pin extension-helpers to 1.* following upstream recommendation - Clément Robert
* [#4946](https://github.com/gammapy/gammapy/pull/4946) Expose `gammapy.estimators.resample_energy_edges` in the tutorials and `HowTo` - Astro-Kirsty
* [#4945](https://github.com/gammapy/gammapy/pull/4945) Return the coordinate for the doubling time as an astropy.Time object - Claudio Galelli
* [#4944](https://github.com/gammapy/gammapy/pull/4944) Expose more features - Quentin Remy
* [#4943](https://github.com/gammapy/gammapy/pull/4943) Expose cluster features in API - Astro-Kirsty
* [#4940](https://github.com/gammapy/gammapy/pull/4940) Fix MapEvaluator for the apply_edisp=False case - Quentin Remy
* [#4939](https://github.com/gammapy/gammapy/pull/4939) Backport PR #4937 on branch v1.1.x (Fix import of angular_separation for astropy 6) - Lumberbot (aka Jack)
* [#4938](https://github.com/gammapy/gammapy/pull/4938) Backport PR #4937 on branch v1.0.x (Fix import of angular_separation for astropy 6) - Lumberbot (aka Jack)
* [#4937](https://github.com/gammapy/gammapy/pull/4937) Fix import of angular_separation for astropy 6 - Maximilian Linhoff
* [#4936](https://github.com/gammapy/gammapy/pull/4936) PiecewiseNormSpectralModel serialising interp - Katrin Streil
* [#4931](https://github.com/gammapy/gammapy/pull/4931) Remove deprecations in `gammapy.modeling` - Claudio Galelli
* [#4930](https://github.com/gammapy/gammapy/pull/4930)  Remove deprecations in `gammapy.maps` - Astro-Kirsty
* [#4929](https://github.com/gammapy/gammapy/pull/4929)  Remove deprecations in `gammapy.astro` - Astro-Kirsty
* [#4928](https://github.com/gammapy/gammapy/pull/4928) Remove deprecation from `gammapy.datasets` - Claudio Galelli
* [#4925](https://github.com/gammapy/gammapy/pull/4925) TODO refactor `ModelBase.from_dict` method into child methods - REGEARD Maxime
* [#4916](https://github.com/gammapy/gammapy/pull/4916) Add `energy_true` to `MapDataset.create()` in tutorial - Astro-Kirsty
* [#4903](https://github.com/gammapy/gammapy/pull/4903) Remove useless norm parameters from spectral model - Quentin Remy
* [#4902](https://github.com/gammapy/gammapy/pull/4902) Add norm attribute to estimators and deprecate previous norm related attributes - Quentin Remy
* [#4885](https://github.com/gammapy/gammapy/pull/4885) Cleanup docstrings for `gammapy.estimators` - Claudio Galelli
* [#4836](https://github.com/gammapy/gammapy/pull/4836) Fix a division per zero in `TemplateSpatialModel` normalisation - Bruno Khélifi
* [#4828](https://github.com/gammapy/gammapy/pull/4828) Adapt SkyModel to evaluate on TimeMapAxis - Atreyee Sinha

### issues opened last week (less than 8 days ago): 
* [#4962](https://github.com/gammapy/gammapy/issues/4962) Documentation list and discussion - Astro-Kirsty
* [#4952](https://github.com/gammapy/gammapy/issues/4952) radially asymmetric IRFs - Shotaro
* [#4950](https://github.com/gammapy/gammapy/issues/4950) Offset axis calculated from fov lon/lat axis can contain a negative bin - Lukas Nickel
* [#4948](https://github.com/gammapy/gammapy/issues/4948) Adjust docs for `gammapy.utils.regions` - Astro-Kirsty
* [#4947](https://github.com/gammapy/gammapy/issues/4947) Tutorial for more complex background models - Astro-Kirsty

 report created at 08/12/2023, 07:09:11