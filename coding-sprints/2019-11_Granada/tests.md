# Tests

Notes by Christoph

- Gammapy testing is in pretty good shape:
  - Automated tests: `make test`, `make test-cov`, `make test-nb`
  - Static analysis: `make flake8`, `make pylint`
  - PyCharm is really nice
  - Run as part of CI on travis-ci and Azure Pipelines
  - Coverage and code quality status: see [here](https://github.com/gammapy/gammapy#status-shields)
  - High-level validation and benchmark effort has started: https://github.com/gammapy/gammapy-benchmarks/
- We should improve further, short-term:
  - High-level validation and benchmark effort ongoing (Atreyee, Luca, Fabio, you?)
  - **Help needed!** Improve test coverage (see [examples](https://github.com/gammapy/gammapy/issues/94#issuecomment-553449147))
  - See Gammapy TESTING project board: https://github.com/gammapy/gammapy/projects/13
  - Improve CI configuration ([GH 2270](https://github.com/gammapy/gammapy/issues/2270)), test Python 3.8 ([GH 2466](https://github.com/gammapy/gammapy/issues/2466)) and Windows better ([GH 2430](https://github.com/gammapy/gammapy/issues/2430))
  - Many other things we can improve, but probably not in 2019.
    E.g. try out [coverage 5.0 and contexts](https://coverage.readthedocs.io/en/latest/whatsnew5x.html), or [Cython coverage](https://cython.readthedocs.io/en/latest/src/tutorial/profiling_tutorial.html#enabling-coverage-analysis)?
- Conclusions:
  - Treat tests like code, we have to maintain it. Goal: both should be dead simple.
  - Python is a dynamic language, test-driven development works best
  - Learn to use `pytest` and `coverage` and `PyCharm` to do it.
  - If testing interests you, pick some non-tested function via https://codecov.io/gh/gammapy/gammapy and let's add a test and make a pull request this week!
