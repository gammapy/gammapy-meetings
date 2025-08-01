# Gammapy Developer Meeting 
 * Friday, August 01, 2025, at 2 pm (CET) 14:05 - 15:17
 * Gammapy Developer Meeting on Zoom (direct link on Slack)

Attendees: Régis Terrier (RT), Hanna (H), Quentin Remy (QR), Daniel Morcuende (DM), Kirsty Feijen (KF), Atreyee Sinha (AS), Katharina Egg (KE), Axel Donath (AD), Leander Schlegel (LS)
# Agenda

- RT: Yesterday we had extra meeting. Look at list of open PRs for v.2.0.

 #5954: "Separate internal EventList data model from gadf format" 
 -------
 - RT: I Can quickly give the status. Now there is internal model for table. Conversion to and from GADF done in IO class    (EventListReader/Writer). One issue from validation error that made test fail, now added something for this: On read the reader opens table and it is checked that minimal columns are present, not a full validation but that minimal four columns are there. If not, error is raised. Otherwise, proceed building the objects and build table, add additional optional columns.
 - QR: Can we still read the SWGO data?
 - RT: I think it works, because the test was running on my machine. There is a test for this specific functionality. If you try to acces events, it would raise a ValueError (in case it fails ???).
 - I will look at the test again, then it should be done, please review afterwards.

 #5859 "Remove deprecated code in FixedPointingInfo"
 ------
 - RT: Removes deprecated code in FixedPointingInfo. Deprecation warning has been there for a long while, now resolved. Changes remove quite a bit of code. Location has now explicitly to be passed to the projection function (???). Change that QR added.
 - QR: I have a fail that is not visible on CI. Maybe someone can try if they see the same. RT: I will check. Modulo this issue, should be ready soon.

  #5898 "Add stacking functionality to LightCurveEstimator"
  ---------
  - RT: Kirsty can you comment?
  - KF: Yes, currently we have a test failing, when name of dataset is changed. Not sure yet what causes this, AS had a look, but was not sure either.
  - AS: I started looking into this but I still did not saw why.
  - AD: WCS reference coordinate is None.
  - AS and AD discuss. AS: Strange that it fails afters stacking was introduced. I can take a look.
  - QR: Might be a precision error?
  - AS: Yes, might we need to add tolerance? I could do a PR with which we see which line is failing.
  - RT: Maybe dataset name is not the same and could lead to a problem?
  - AS: Yes that is the only point I found. Why it works for non-stacking case is confusing me.
  - AD: Depends on which axis you stack. For data axis it gives new names, along the energy axis it fails. First thing I would do is improve error message here to see where it is thrown. Info currently not enough. If axis are not aligned, the code should tell us why this is.
  - AS: I have already a solution for this and will do a PR.
  - RT: Maybe say in docu that it is not advised to do with regular MapDatset? Discussion with AS.
  - RT: We have this issue to be solved, take a decision next week, AS gives update on Monday, RT agrees.

 #6029 "Standardized implementation prior_stat_sum"
 --------
 - QT: Old uniform prior penalized. Will modify the notebook, but should already not contain term "prior" in that case (???).
 We do not show weight system.
 - RT: We will have to work on solution in general for penalties instead of priors. Not being bound to API like it is.
 - AD: Agree, introducing new penalty API requires a bit more work. Is it possible to have custom priors? Then we could fully move the whole definition in the documentation/notebook (Example how to do it custom) then not part of gammapy-API. I think it would be the safest thing to do. QR agrees.
 - AD: If it works technically, preferable solution, because then we do not introduce new API.
 - RT: Idea would be to start with custom prior, then use it for penalized? ???
 - AD: You could even call it "non normalized prior".
   Tutorial on implementing a custom prior discussed by RT, AS, AD, QR.
- RT: Do we deprecate attribute of prior?
- AS: Entire unfiorm prior deprecated?
- QR: Additional usecase ???
- AD: If we do 3D fit we have alot of pixels, and sum the liklihood of those pixesl. Question is, if we maybe have to take mean. This reweighting per pixel, how many measurements, etc... generic way is global way to scale likelihood back to the prior. I think we need it. For the Poisson-Likelihood I ended up using the mean, gave a more stable parametrization with respect to the prior. Requires generic/adhoc handling if unexperienced with the data. What is the value to expect from a Cash-Likelihood for a given dataset, for example. For millions of pixel, prior on single parameter does not do much. In practice handle needed. Also, results can differ for different weights. 
Prior taken to certain power should (under certain properties) still be normalized, still in the Map regime.
- RT: OK, We keep the weight for now and will see how the framework evolves for the penalties. QR you introduced the random variable, if we want to have sampling we need something similar ??? QR agrees, I can add a line.

#6038 "Vectorized error evaluation of flux uncertainties based on samples"
-----
- QR: Now it is fully working. Every thing is vectorized, when the model can not, there is a fallback, then loop over samples is done. I removed change it naima ???. I tried to parallize it, there was no gain, kept it like this, simple loop. Possibility to give sample directly as attribute ??? For now, samples given as list of arrays in specific order of parameters.
- RT: No specific tests, probably test for vectorized spectrum that you could use, so that it is tested independently. Question reg. typical number of samples: Since it is parallelized more than 3000 x N_parameters.
- QR: 3500 x N_Parameter. For powerlaw 10000, for more complex model it will be more. The larger param-space, the more points you need to sample it correctly. RT agrees.
- RT: Adding independent class for this type of calculation may be good. Maybe cleaner refactoring, but not urgent. Maybe you could make some tests for vectorized version, otherwise looks fine, reviews needed. QR agrees to add tests.

RT: Then we are through with higher prioritity. 

#6002 "Update of plot functions for the colour bar"
----
- AS: Colorbar was in middle of plot, we need this before release.
- QR: Can we find generic solution?
- AS: It was fine before #599? ??? DM, KF, do you have an idea?
- DM: Maybe it was tight_layout aplied, that is what BK removes.
- AD: Yes, we should this not call internally in gammapy, only users outside. In tutorial fine, but not in production code.
- DM: I will have a look later.
- KF: For v. 1.3 we added more functionality for colorbar, so why previous PR needed, what happened between 1.3 and now, does anyone know?
- AS: We should add this to high priority list.
- AD, KF, RT, AS agree: we should revert #5992.
- RT, AD discuss: Complex to do certain plots. We should aim at 80 percent for nice plots, 100 percent is much of work. If nicer plot needed for your toturial, code could be added there.
- AS: For VERITAS it happens, not for other tutorials (HESS).
- AD: Revert 5992, then introduce solution for 5991.
- RT: Agree, we revert. General comment: Difficult task for many commit, because the right one has to be found.
  AD, RT: Revert whole PR / revert merge commit? AD: I can try, RT agrees.
- RT, KF, discussion over general concept/strategy for method (oversquash?) to adjust number of commits per PR ??? KF: Then one main branch just final product, DM: History cleaner. KF, RT, AD agree.
- AD: Checked that direct revert not possible, requires fixing conflicts.
- RT: Comment in 6002 that it is better to keep it simple, especially for peek function.
- AD: Have to leave in 2 mins, but can do the revert.

#6031 "Exposing AnalysisConfig better"
-----
- KF (shares screen): Current documentation quite messy and confusing to look at. Thereby, I implemented in PR change of settings, to make it nicer (suppress parts). Question how to proceed: Two options are to either in each of these parameters specify input, or adjust docstring of those classes?
- RT: AnalysisConfig based on pydantic?
- KF: Yes, this is why I had to add this specific setting.
RT, KF, AS discuss.
- AS: Explaining manually kind of equivalent to exposing all.
- KF: If we do not expose, all the configs not needed.
- RT: New analysis high-level interface not ready now, but will be at some point. Question is, shall we do correct exosition now, if we have to deprecate soon?
- AS: Is class much used?
- RT: Probably not as only exposed in two points in tutorials. Is there way to get rid of all pydantic specific functions? Strong objection to exposing the ??? Otherwise proceed.

#6043 "Fix docstrings"
------
KF explains, is a small change.


#???? ""
--------
DM explains. RT: Comes from old issue from Max, KF agrees.


RT: Through with open PRs, Changelog and Citation.cff remain and open Issues. Much less than before.
- AS: Yes, we postponed the ones open for more than 2 years, as they can not be high priority. RT agrees.
- RT: For the remaining ones, we postpone the ones with feature requests. No bugs so far, no documentation, we could postpone everything.
We postpone them and check on remaining PRs next week. Ideally branching next week, I can join for that at some point, but will be mostly away. QR, AS?
- RT, QR, AS agree to do it together.
- RT: Branching, finalizing citation and changelog remain. If branching next week, rest maybe before 15 of August, then final checks. ???
We are close to be done with 2.0, thank you for the hard work! :)

### Open PRs for v2.0

https://github.com/gammapy/gammapy/pulls?q=is%3Aopen+is%3Apr+milestone%3A2.0

### Open issues for v2.0

https://github.com/gammapy/gammapy/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A2.0

### PRs opened last week (less than 8 days ago): 
* [#6038](https://github.com/gammapy/gammapy/pull/6038) Vectorized error evaluation of flux uncertainties based on samples - Quentin Remy
* [#6031](https://github.com/gammapy/gammapy/pull/6031) Exposing `AnalysisConfig` better - Kirsty Feijen
* [#6029](https://github.com/gammapy/gammapy/pull/6029) Standardized implementation prior_stat_sum - Quentin Remy
* [#6027](https://github.com/gammapy/gammapy/pull/6027) Correct setup in tutorialjupytexttests.yml - Daniel Morcuende
* [#6025](https://github.com/gammapy/gammapy/pull/6025) Add Bayesian model selection - Quentin Remy
* [#6024](https://github.com/gammapy/gammapy/pull/6024) Add utilities to create arviz.InferenceData from  SamplerResult - Quentin Remy
* [#6010](https://github.com/gammapy/gammapy/pull/6010) Changelog for 2.0 - Atreyee Sinha

### PRs merged last week (less than 8 days ago): 
* [#6039](https://github.com/gammapy/gammapy/pull/6039) Adapt CTAO tutorial with xmltodict - Kirsty Feijen
* [#6035](https://github.com/gammapy/gammapy/pull/6035) Final removals of  tutorial setup - Kirsty Feijen
* [#6034](https://github.com/gammapy/gammapy/pull/6034) Remove TODO from documentation build - Kirsty Feijen
* [#6033](https://github.com/gammapy/gammapy/pull/6033) fix[ci]: ensure linkcheck tox dependencies are installed  - npigoux
* [#6028](https://github.com/gammapy/gammapy/pull/6028) Clearer description of `select_nested_models` - Kirsty Feijen
* [#6026](https://github.com/gammapy/gammapy/pull/6026) Fix the call to tutorials/api - Kirsty Feijen
* [#6023](https://github.com/gammapy/gammapy/pull/6023) Restructure gammapy.modeling.selection - Quentin Remy
* [#6022](https://github.com/gammapy/gammapy/pull/6022) Add random_variable  property on prior - Quentin Remy
* [#6021](https://github.com/gammapy/gammapy/pull/6021) Fix tutorials and link errors - Kirsty Feijen
* [#6018](https://github.com/gammapy/gammapy/pull/6018) Remove extern - Kirsty Feijen
* [#6016](https://github.com/gammapy/gammapy/pull/6016) Fix for reco PSF in create_map_dataset_from_dl4 - Quentin Remy
* [#6015](https://github.com/gammapy/gammapy/pull/6015) Update minimum python version supported mentioned in howto dev documentation - Daniel Morcuende
* [#6014](https://github.com/gammapy/gammapy/pull/6014) Fix discrepancy in exposure maps unit  attached to edsip and psf from FermipyDatasetsReader - Quentin Remy
* [#6013](https://github.com/gammapy/gammapy/pull/6013) Install gammapy and jupytext in check notebooks action - Daniel Morcuende
* [#6012](https://github.com/gammapy/gammapy/pull/6012) Install gammapy and jupytext in check notebooks action - Daniel Morcuende
* [#6009](https://github.com/gammapy/gammapy/pull/6009) Update dev docs to mention utility scripts available for a release - Atreyee Sinha
* [#6008](https://github.com/gammapy/gammapy/pull/6008) Description for data peek functions - Kirsty Feijen
* [#6007](https://github.com/gammapy/gammapy/pull/6007) Fix doc uniformprior - None
* [#6005](https://github.com/gammapy/gammapy/pull/6005) Fixing `FluxPoints` docstring - None
* [#6004](https://github.com/gammapy/gammapy/pull/6004) Fix linkchecks and adapt conf - Kirsty Feijen
* [#6000](https://github.com/gammapy/gammapy/pull/6000) Tutorials run as notebooks - Kirsty Feijen
* [#5998](https://github.com/gammapy/gammapy/pull/5998) Remove tutorial setup - Kirsty Feijen
* [#5995](https://github.com/gammapy/gammapy/pull/5995) Update Fermi-LAT tutorial - Quentin Remy
* [#5984](https://github.com/gammapy/gammapy/pull/5984) Coherent checksum behavior in the IO function of `Datasets` - Bruno Khélifi
* [#5982](https://github.com/gammapy/gammapy/pull/5982) Add class instance caching for WcsGeom - Quentin Remy
* [#5979](https://github.com/gammapy/gammapy/pull/5979) Fix memory leak related to lru_cache - Quentin Remy
* [#5975](https://github.com/gammapy/gammapy/pull/5975) Allow configuration of a size_factor in Models.to_regions - Atreyee Sinha
* [#5973](https://github.com/gammapy/gammapy/pull/5973) Warn users when using negative amplitude models in FluxEstimator - Atreyee Sinha
* [#5969](https://github.com/gammapy/gammapy/pull/5969) Add tutorial for non-detected sources - Atreyee Sinha
* [#5961](https://github.com/gammapy/gammapy/pull/5961) Adding description to irf peek functions - Kirsty Feijen
* [#5949](https://github.com/gammapy/gammapy/pull/5949) Adapt tutorial order - Kirsty Feijen
* [#5941](https://github.com/gammapy/gammapy/pull/5941) Tutorial setup command line option - Kirsty Feijen
* [#5933](https://github.com/gammapy/gammapy/pull/5933) Add tutorial for computing parameter upper limits - Atreyee Sinha
* [#5910](https://github.com/gammapy/gammapy/pull/5910) Change argument name in ul - Kirsty Feijen

### issues opened last week (less than 8 days ago): 
* [#6042](https://github.com/gammapy/gammapy/issues/6042) Implement scheduled build of wheels - Daniel Morcuende
* [#6041](https://github.com/gammapy/gammapy/issues/6041) Evaluate the use of CircleCI - Daniel Morcuende
* [#6020](https://github.com/gammapy/gammapy/issues/6020) Move MAGIC tutorial to Data Exploration - Atreyee Sinha
* [#6019](https://github.com/gammapy/gammapy/issues/6019) Bayesian model selection - Quentin Remy
* [#6017](https://github.com/gammapy/gammapy/issues/6017) User feedback on documentation - Kirsty Feijen

 report created at 01/08/2025, 07:32:23
