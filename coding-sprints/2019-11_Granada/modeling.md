# Gammapy Modeling

- Christoph Deil
- Nov 18, 2019
- Gammapy coding sprint in Granda

## Overview

- We introduced `gammapy.modeling` and `gammapy.modeling.models`. See [docs](https://docs.gammapy.org/dev/modeling/index.html#reference-api) [PIG 16](https://docs.gammapy.org/0.14/development/pigs/pig-016.html)
- [PIG 14 - Uncertainty estimation](https://github.com/gammapy/gammapy/pull/2255)
- gammapy.modeling project board: https://github.com/gammapy/gammapy/projects/7

## High priority work (2019)

Things we should try to do for v0.15. I put an estimate of how long it could take.
(about as reliable as astronomical distance estimates)

- Write documentation (`docs/modeling/index.rst`, `tutorials/models.ipynb`, `tutorials/modeling.ipynb`)
- Implement PIG 14 - clean up spectral model evaluation, error propagation (2 days)
- Polish model registry and factory ([GH 2387](https://github.com/gammapy/gammapy/issues/2387#issuecomment-553777765)) (1 day)
- Clean up model names ([GH 2353](https://github.com/gammapy/gammapy/issues/2353))
  (`lon_0` -> `lon`, `reference` -> `energy_ref`, `lambda_` -> `alpha`, ...)
  Needs proposal and decision. Do next week? (1-2 days)

Would like to have for v1.0, but probably not a blocker?

- Improve model evaluate and `__call__` API ([GH 2443](https://github.com/gammapy/gammapy/issues/2443)) (needs design proposal, ~ 1 week, defer to 2020?)
- Add optional `SkyModel.temporal_model` (2 hours) and make evaluate work properly (1-2 days)
- Make [SkyDiffuseCube](https://docs.gammapy.org/dev/api/gammapy.modeling.models.SkyDiffuseCube.html) a `SpatialModel` subclass?
- API to interact with parameter errors ([GH 1398](https://github.com/gammapy/gammapy/issues/1398)) (1 day)
- Remove parameter scaling? ([GH 2434](https://github.com/gammapy/gammapy/issues/2434)) (1-2 days)
- LogGaussianSpectralModel mean position ([GH 2436](https://github.com/gammapy/gammapy/issues/2436)) (3 hours)

## Low priority work (2020)

- Dedicated effort on Gammapy modeling 2.0? Hire Tom?
- Goal: 10x to 1000x faster, depending on model and machine

## Discussion

- Issues, solutions, tasks, priorities, contributors?

