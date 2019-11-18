# Gammapy Testing

- Christoph Deil
- Nov 18, 2019
- Gammapy coding sprint in Granda

## Overview

- Automated tests: `make test` or e.g. `pytest -v gammapy/cube -k map_fit`
- 847 test functions in 112 test files in `gammapy/xyz/tests` folders
- 1492 tests run since we use `@pytest.mark.parametrize` in 136 test functions
- No defined testing levels, tests range from [unit tests](https://github.com/gammapy/gammapy/blob/master/gammapy/irf/tests/test_background.py) to [science analysis tests](https://github.com/gammapy/gammapy/blob/master/gammapy/analysis/tests/test_analysis.py).
- Quality of tests ranges from excellent to terrible
- Tutorial notebooks `make test-nb` and scripts `make test-scripts` (only check that no error is raise, no asserts on outputs)
- Test coverage: `make test-cov`, or e.g. `pytest gammapy --cov=gammapy --cov-report=html`
- Coverage status at https://codecov.io/gh/gammapy/gammapy and we now get [Codecov report on pull requests](https://github.com/gammapy/gammapy/pull/2552#issuecomment-554656572)
- Continuous integration on travis-ci (11 builds) and Azure Pipelines (5 builds)
- Static analysis: `make flake8`, `make pylint` and PyCharm locally
- Static analysis online on LGTM and Codacy (not well configured ATM)
- Transparent status:  https://github.com/gammapy/gammapy#status-shields
- TESTING project board: https://github.com/gammapy/gammapy/projects/13

## High priority work (2019)

- High-level validation and performance benchmarks: https://github.com/gammapy/gammapy-benchmarks/
  (work ongoing by Atreyee, Quentin, Luca, Fabio)
- **Help welcome!** Improve test quality and coverage (see [examples](https://github.com/gammapy/gammapy/issues/94#issuecomment-553449147))

- Christoph: Improve CI configuration ([GH 2270](https://github.com/gammapy/gammapy/issues/2270)), test Python 3.8 ([GH 2466](https://github.com/gammapy/gammapy/issues/2466)) and Windows better ([GH 2430](https://github.com/gammapy/gammapy/issues/2430))
- Christoph: Make tests that connect ot internet like test_cli_download_tutorials not run by default

## Low priority work (2020)

- Activate and run doctests [GH 101](https://github.com/gammapy/gammapy/pull/101)?
- Change to pytest to run notebooks and add asserts
- Migrate travis-ci builds to Azure pipelines or Github actions, to be on one platform
- Write a PIG "Gammapy test structure" to have a clear layered approach to testing (similar to [PIG 16 - Gammapy package structure](https://docs.gammapy.org/0.14/development/pigs/pig-016.html))
- Review and improve all Gammapy tests
- Add [Cython coverage](https://cython.readthedocs.io/en/latest/src/tutorial/profiling_tutorial.html#enabling-coverage-analysis) (or remove Cython code)

## Suggestion

- Treat tests like code, we have to maintain it. Goal: both should be dead simple.
- Python is a dynamic language, test-driven development works best
- Learn to use `pytest` and `coverage` and `PyCharm` to do it.
- If you want to try it out, I'm happy to pair-code this week.

## Discussion

- Issues, solutions, tasks, priorities, contributors?
