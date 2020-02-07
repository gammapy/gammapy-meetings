# Gammapy Developer Meeting

* Friday, Dec 20, 2019 at 10 am
* "Gammapy Developer Meeting" on CTA eZuce, no password, [connection details](../ezuce.txt)

# Agenda

* [Gammapy pulse from last week](https://github.com/gammapy/gammapy/pulse)
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
* Short report by everyone, what they have worked on during the past week 

* Gammapy v0.16 is released! We scheduled another v0.17 release in March. Let's try to make v0.17 the v1.0 "release candidate". I.e. it should include all major API changes and be "feature complete".
* Brief update on event sampling validation (Fabio)
* Background model handling [GH 2768](https://github.com/gammapy/gammapy/pull/2768) (Axel)
    - Open question: how to handle the data of the background model?
    - Keep on the `MapDataset` as `MapDataset.acceptance` and introduce `AcceptanceBackgroundModel`, which contains the spectral parameters only?
    - Always serialise separately?
    - How to handle models in general during stacking?
  
* Naima SSC [GH 2767](https://github.com/gammapy/gammapy/pull/2767)(Quentin / Régis)
* Fitting tutorial [GH 2764](https://github.com/gammapy/gammapy/pull/2764)(Quentin)
