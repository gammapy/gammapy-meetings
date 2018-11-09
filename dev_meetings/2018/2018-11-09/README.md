# Gammapy Dev Telcon

* Friday, November 9, 2018 at 10 am
* CTA eZuce, no password. The connection details are [here](../2018-10-12/ezuce.txt)

# Agenda

* [Gammapy pulse from last week](https://github.com/gammapy/gammapy/pulse)
* [Open pull requests for Gammapy 0.9](https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A0.9)
* [Open issues for Gammapy 0.9](https://github.com/gammapy/gammapy/issues?q=is%3Aopen+is%3Aissue+milestone%3A0.9)
* Add Scipy fitting backend [#1907](https://github.com/gammapy/gammapy/issues/1907) (Christoph)
* How to implement fitting the background normalization [#1804](https://github.com/gammapy/gammapy/issues/1804)(Axel)

  Add a `HadronicBackground` model class and treat it as a regular model component, but not
  applying IRFs to it. This could be handled in three ways:

    - Implement the `HadronicBackground` as special case in `ModelEvaluator` and do not apply IRFs
    - Define flags on models whether to apply IRFs or not
    - Make IRFs part of the model specification (like "edisp(psf(exposure * sources)) + background". The
      latter is what sherpa does, but it is significantly more work. 
  
  Any other suggestions?

* Observation time from GTI table [#1908](https://github.com/gammapy/gammapy/pull/1908) (David)


