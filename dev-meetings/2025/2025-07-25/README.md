# Gammapy Developer Meeting 
 * Friday, July 25, 2025, at 2 pm (CET), (14:00-16:00 approximately)
 * Gammapy Developer Meeting on Zoom (direct link on Slack)

Attendees: Atreyee Sinha (AS), Kirsty Feijen (KF), Daniel Morcuende (DM), Axel Donath (AD), Bruno Khélifi (BK), Quentin Remy (QR),        
           Leander Schlegel (LS)

# Agenda

- A.S.: 56 open issues currently, probably not solvable before release, thereby start looking at PRs

  -> See Discussion of open PRs (longer standing and recently opended) see below, later discussion of open issues (see below as well).

- AD: Comment about Changelog for 2.0:
  
In 2.0 we bring two communities together (a lot work with VERITAS). MAGIC now also publishes public data.
In "Data analysis" - section add at least short MAGIC analysis tutorial. AS: agrees, MAGIC-tut for now was hidden in 1d-analysis.
AD: Maybe 60 percent of work for 2.0 done yet, a bit behind.
BK: SWGO not founded yet, maybe not on webpage, but for changelog okay. AD: Yes, people in SWGO should be informed, that gammapy can be used.
AD: Dedicated call for changelog?
AS: When Régis comes back. Next week I'm not there.
AS: Am I missing important features we want to mention in the highlights?

- Email address to be used to send requests to, to sign up to gammapy? BK agrees, should be received by lead-devs. Can be done fast.

- QR agrees to lead meeting next time, as RT not back and AS can only stay for half an hour approximately.

### Open issues for v2.0

https://github.com/gammapy/gammapy/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A2.0

- #5931: extern/xmltodict.py deprecated. BK,QR,AS agree to remove it completely, as code would be saved in old code-versions.
KF assigned.

- #5891: QR: We can postpone it, no usecase for which its really broken.

- #5854: AS: Would have been nice if we would have had time. BK, AS agree it would be nice, put it to 2.1 for now.

- #5783: AS: Not sure if this is a bug? Internally it works correct, annoying unit written. Agree: Not a bug, clean-up.

- #5775: BK: Needed for data challenge analysis, we have a bit of time. QR: Missing to link output of parser to select observation, one last thing was missing. I can finish it. QR assigned.

- #5745: KF explains, can update docstring. AS: You could look at tutorial if it satisfies the PR. KF agrees, and can add links to the tutorial in the docstring.

- #5737 "Adapt SensitivityEstimator to Cowan approach" : AS, QR discuss it. QR: We can do that, a flux point that does it AS: Question of documentation.  AS: We need more discussion. BK: Add to userguide section for sensitivity computation. AS: Pointsource tutorial (CTA 1d)? Agree that flux point is not well exposed. BK: It is not 1D, can be 3D, we need upgrade in the documentation. Show what are statistical differences, what is the physical meaning. AS: Not a tutorial but userguide. BK: It is in the middle, I think we need a dedicated documentation here.
AS: Put it to 2.0 if someone has time to put documentation in, no one assigned.
QK: We could make new class Joint Sensitivity Estimator? That would combine the steps to do this. Currently it is tied with points estimators.
AS: Question of documentation.

- #5728: AS: More or less necessary. QR: PR moved to 2.1, need time for proper reviews.

- #5713 "Adapt reoptimize option for FluxPointEstimator":  AS,QR discuss. Expose in doc that user can config. parameters to fit before running estimator. AS comments in Issue.

- #5705 assigned to LS, put to 2.1.

- #5693 "Request to Add Finke et al. (2022) EBL Model.": 
AS suggests: Solution how to write your own model, that can be read by gammapy.
QR agrees, would be better if we do not need to add models for other people.

- #5691: AS presents.

- #5626: AS; BK agree, Not needed, can be moved to 2.1

- #5598: BK: 2.1, still a lot of work to do.

- #5587: "Enhance CI": KF: Can be moved to 2.1. You can check preview docs in PR and use labels to skip jobs. Main things remain if we want to rebuild CI completely, which would involved something like CircleCI. DM assigned, for 2.1.

- #5552: BK: 2.1.

- #5494: AS: What is state? No failing tests? QR: 2.1, we can simplify tests maybe.

- #5484: BK: Issue that it is super slow, it works. QR: Test data was not good? BK: We have to check to have proper evaluation.
QR and BK discuss. AS: Cant we update our HAWC-tutorial? QR: Not really the same. KF: Not really a place in the tutorial for this. BK: Thereby adding tutorial. AS: No public data for this. QR: I check in the tutorial. Internally histogram is fitted and sometimes fit is terrible.
BK: Do we have benchmark on SWGO? QR: Not in gammapy. BK: Could be interesting in gammapy. BK: 2.1

- #4712: AS: Set to 2.1

- #4641: AS: Claudio planned this. Set to 2.1

AS: Most other Issues are older than 2 years, are there important ones staying in 2.0 or move all to 2.1?
QR: Yes, you can move all of them.
KF: Maybe some repeat? Maybe we should go through and check? I can have a quick look and let you know.

### Open PRs for v2.0

https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A2.0

* #6014 : QR: We should support it, AS: Ok from my side, if someone else reviews we can merge.
 
* #6013 : DM: explains AS: Should be fine, can do review.

* #5838 : AS: Put to 2.1 QR agrees.

* #5859 : AS: Will take a look why test is failing.

### PRs already discussed at least once:

* [5982] "Add class instance caching for WcsGeom":
  
QR: Would be good to have in for 2.0, is deactivated by default, so will not cause problems.
AS: AD, you suggested to do benchmarks, where it helps, can you do review on this?
AD: Yes, sure!
BK asks about details, suggests to make a reminder for it 

* [5965] Non-detected sources

AS: Long open, basically ready, only if licence should go on top.
BK: Will tell you this afternoon by slack if any comments.
AS: Otherwise could go in.
KF: Should I check again, some comments from my first review not implemented. KF agrees to implement them.

* [5954] "Separate internal Eventlist data model from gadf format"
  
QR: Check test? AS checks, was okay. BK: Some more testing needed.
AS: We wait for Régis until he is back.

* [5949] Adapt tutorial order
  
KF: Open to suggestions for minimal solution that we could implement. now.
AS: Idea instead of calling it API, Keysteps.
QR: Observationclustering and DM maybe into other section?
AS: Other aspects (nested sampling) also not key to gammapy analysis.
KF: Suggestion from first entry in Issue #5796, BK agrees. KF: I'm open to suggestions, but removing API is good idea, it could be seen and neglected as not important by people.
AS: "Mask" as advanced options?

KF: Maybe really splitting it, do it as suggested in bottom of first entry of Issue #5796.
QR: EBL, Pulsars, DM, Energy-dep morph. into astrophysics section. Nested sampling should not go in, not astroph. use case (QR), as it is fitting and already exposed in the user guide under fitting (BK).
AS: Second section "Detailed explanations" (How to use estimators, catalogs,...)
BK: agrees.

* [5910] "Change argument name in ul"
  
KF: Docstring did not match implementation. In the end implemented Régis suggestion, AS helped me. But one test still failing. Added more raised errors.
AS explains. Get minima from interpolated profile.
KF: Unclear why test fails, as only in one case.
AS: Different interplation to be more stable, but consistent to use different ones? 
LS: Can type of polynomials have an effect, probably preventing finding minimum properly by artifacts?
QR answers: Yes, but here shape of interpolant similar to expected shape.


### PRs opened last week (less than 8 days ago): 
* [#6010](https://github.com/gammapy/gammapy/pull/6010) Changelog for 2.0 - Atreyee Sinha
  
- AS: Started to fill in Changelog. Am not aware of the things to be highlighted for Infrastructure: DM and KF agree to take a look.
- AS: Get a timeout, KF agrees to check it, AD: Is a limitation by GitHub Actions. Limit by GitHub for too many requests in a too small amount of time, you could artificially increase time. "time.sleep" in between requests could work.

* [#6009](https://github.com/gammapy/gammapy/pull/6009) Update dev docs to mention utility scripts available for a release - Atreyee Sinha

- AS: Where does metadata reside in workflow? BK, AD answer. AD recommends to run it, see what diff is and if it is reasonable.
- AS: What does file prepare-release.py? AD: Updates release-date and version in citation.cff. Suggests to run it and see diff. AS: Before or after release? AD: Before the release. BK: After or before release-candidate is made? AD: Not sure it matters. As release candidate does not go to zenodo but only PyPI. 
- KF: We should merge your PR, AS.

* [#6008](https://github.com/gammapy/gammapy/pull/6008) Description for data peek functions - Kirsty Feijen

KF: Easier to do for specific IRFs, but a bit diffcult for observations, as it depends on what is stored in there. Wait for opinions on how we should proceed. Idea behind PR, that it is not clear what the peek-functions tell.

* [#6007](https://github.com/gammapy/gammapy/pull/6007) Fix doc uniformprior - None

AS: Fix on the docstring, but def. problem with priors in general? QR: Yes. AS: Should be good for 2.0, QR agrees. KF: As it is so simple, we can just merge it. It is clear we should have it in for 2.0, QR agrees. 

* [#6006](https://github.com/gammapy/gammapy/pull/6006) Add utility function to create a grid of rectangular regions - Atreyee Sinha
* [#6005](https://github.com/gammapy/gammapy/pull/6005) Fixing `FluxPoints` docstring - None

* [#6002](https://github.com/gammapy/gammapy/pull/6002) Update of plot functions for the colour bar - Bruno Khélifi

BK: Close to be ready, one case has to be tested, will let AS know by slack.

* [#5998](https://github.com/gammapy/gammapy/pull/5998) Remove tutorial setup - Kirsty Feijen

KF: Other PR has been merged, can go in.

* [#5995](https://github.com/gammapy/gammapy/pull/5995) Update Fermi-LAT tutorial - Quentin Remy

AS: Okay from my side, are your comments still open, BK, KF?
BK: Problem is, esp. for beginners, that DL4 products can not be produced. QR: There is a code block for it, BK: agrees, all good for me.
AS: We can merge it. KF: I can check a last time that format is fine.

* [#5898]

AS explains. Some tests are failing due to icompatibility in Geom. KF: Really puzzling, the test was not failing before removed background, added if-statement. Can someone else take a look? AS: I can do it.

* [5881] "A class for vectorized evaluation of flux uncertainties based on samples"

QR: Definition is same for uncertainty but much faster than we do it now.
AS: Options to do it slower but same for naima-models. 
QR: We can make compound-model work, should be feasible.
  

### PRs merged last week (less than 8 days ago): 
* [#6004](https://github.com/gammapy/gammapy/pull/6004) Fix linkchecks and adapt conf - Kirsty Feijen
* [#6001](https://github.com/gammapy/gammapy/pull/6001) Sphinx guidelines for links - Kirsty Feijen
* [#6000](https://github.com/gammapy/gammapy/pull/6000) Tutorials run as notebooks - Kirsty Feijen
* [#5999](https://github.com/gammapy/gammapy/pull/5999) Handling non-backward compatible format of the covariance matrix - Bruno Khélifi
* [#5997](https://github.com/gammapy/gammapy/pull/5997) Run doctests - Kirsty Feijen
* [#5996](https://github.com/gammapy/gammapy/pull/5996) Cleanup docs - Kirsty Feijen
* [#5994](https://github.com/gammapy/gammapy/pull/5994) Solve IRF circular import  - Régis Terrier
* [#5993](https://github.com/gammapy/gammapy/pull/5993) Fix tutorial page LHS dropdown - Kirsty Feijen
* [#5992](https://github.com/gammapy/gammapy/pull/5992) Update the peek function - Bruno Khélifi
* [#5984](https://github.com/gammapy/gammapy/pull/5984) Coherent checksum behavior in the IO function of `Datasets` - Bruno Khélifi
* [#5979](https://github.com/gammapy/gammapy/pull/5979) Fix memory leak related to lru_cache - Quentin Remy
* [#5977](https://github.com/gammapy/gammapy/pull/5977) Update docs of counts_statistic.py - Atreyee Sinha
* [#5976](https://github.com/gammapy/gammapy/pull/5976) Add option to convert PointSkyRegion to CircleSkyRegion while creating masks - Atreyee Sinha
* [#5975](https://github.com/gammapy/gammapy/pull/5975) Allow configuration of a size_factor in Models.to_regions - Atreyee Sinha
* [#5973](https://github.com/gammapy/gammapy/pull/5973) Warn users when using negative amplitude models in FluxEstimator - Atreyee Sinha
* [#5968](https://github.com/gammapy/gammapy/pull/5968) Part 3 - Tutorial cleanup - Kirsty Feijen
* [#5961](https://github.com/gammapy/gammapy/pull/5961) Adding description to irf peek functions - Kirsty Feijen
* [#5960](https://github.com/gammapy/gammapy/pull/5960) Energy edges instead of center for `aeff-max` in `SafeMaskMaker` - Kirsty Feijen
* [#5945](https://github.com/gammapy/gammapy/pull/5945) Create exclusion mask for bright stars in FoV - Samantha Wong
* [#5941](https://github.com/gammapy/gammapy/pull/5941) Tutorial setup command line option - Kirsty Feijen
* [#5936](https://github.com/gammapy/gammapy/pull/5936) Update of the user guide documentation of `Modelling and Fitting` - Bruno Khélifi
* [#5934](https://github.com/gammapy/gammapy/pull/5934) Estimator documentation: update the n_sigma description - Bruno Khélifi
* [#5927](https://github.com/gammapy/gammapy/pull/5927) Add mask plot for spectral - Kirsty Feijen
* [#5923](https://github.com/gammapy/gammapy/pull/5923) simple fix to problem with EventList printing - Tomas Bylund
* [#5918](https://github.com/gammapy/gammapy/pull/5918) Adding VERITAS tutorial - Samantha Wong
* [#5886](https://github.com/gammapy/gammapy/pull/5886) Improve HowTo page titles - Gnana Sindhu
* [#5879](https://github.com/gammapy/gammapy/pull/5879) Fix date keywords in DataStore - Fabio PINTORE
* [#5855](https://github.com/gammapy/gammapy/pull/5855) Utility to filter a table parsing string of  logical operations - Quentin Remy

### issues opened last week (less than 8 days ago): 
* [#6003](https://github.com/gammapy/gammapy/issues/6003) FluxPoints documentation showing extra attribute - None
  

* [#5990](https://github.com/gammapy/gammapy/issues/5990) Prior class - weight parameter in the call, not the evaluate - None

AS, QR: is about, how should the weights go in. For 2.0 we can keep it like this, but we need to clarify purpose of weight. Two different cases, QR explains. AD: From stat. perspective, it corresponds to variance (at least for Gaussian case). For Gaussian prior already in, as you define variance of prior. Question if you want to support this in more uniform way. For uniform prior also in, once you define bounds of uniform prior. Some degree of overlap between definitions, matter of documentation? 
QR: For now, only defined as multiplicative factor.
AD: Documentation, have one example where we show how to do this. Should be possible to handle with definition of variance
AS: We can put it to 2.1.
QR: We dont use weights as it is implemented, we can see later what we do about it.

* [#5989](https://github.com/gammapy/gammapy/issues/5989) Non standardized implementation of the Prior classes - None

QR: #5989 should be solvable easily. AS: Has to be resolved for 2.0. Ask @lgreaux if they want to fix it themselves, assigned.

* [#5988](https://github.com/gammapy/gammapy/issues/5988) Non-coherent documentation for UniformPrior class - None
* [#5986](https://github.com/gammapy/gammapy/issues/5986) Spatial model not frozen in tutorial - None

 report (originally) created at 25/07/2025, 07:28:14
