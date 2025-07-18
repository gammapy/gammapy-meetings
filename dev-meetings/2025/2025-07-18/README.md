# Gammapy Developer Meeting 
 * Friday, July 18, 2025, at 2 pm (CET) approx. 14:03-15:53 
 * Gammapy Developer Meeting on Zoom (direct link on Slack)

Attendees: Kirsty Feijen (KF), Atreyee Sinha (AS), Axel Donath (AD), Matthias Fuessling (MF), Tomas Bylund (TB), Leander Schlegel (LS), Régis Terrier (RT), Daniel Morcuende (DM)

# Agenda

- Short report from the Scipy 2025 conference (AD)
  ---
  - Less attendence than in the last years due to cuts in funds

  - ROSES (???) fund for open source projects probably will end soon, gammapy not directly affected.
    Astropy not really in danger, payings through secure James Webb funding, other private fundings.
  - Many API Updates, xarray set out to support astro data.
  - Chat with (???) (zfit) on technical topics.
    How to handle parameters? (esp. in gammapy distribution computing).
    Approach for zfit: Single param list with unique names for parameters
  - AI (time based pulsar array studies), not relevant for gammapy in the moment
  - Chat with ??? nowfocus (???), could be useful for gammapy.
 
RT: xarray possible replacement for maps at some point?
    Regarding zfit, overview important for possible restructuring at some point (?)
    AD: zfit using not an option, but can exchange design ideas / learn from each other.
  
### Documentation
* general updates made to tutorials to be formatted correctly
* added documentation on skipping github actions to the dev how to
* reordering of the tutorials

KF reports on the status. Especially:
- VERITAS tutorial [#5918](https://github.com/gammapy/gammapy/pull/5918)
KF: VERTIAS tutorial basically ready.
RT: VERITAS turotial should be good to go, AS agrees, one more approval needed only, RT agrees to approve PR, let AS merge.
Maybe safer to use regular safe-regions?

* to add descriptions to the various `peek` functions -- delegation of tasks [#5961](https://github.com/gammapy/gammapy/pull/5961)
  - PR started for improving peek-functions, delegation of tasks needed.


### Outstanding:

AS: Can we talk about #5979, #5982 ?

* [#5979](https://github.com/gammapy/gammapy/pull/5979) Fix memory leak related to lru_cache - Quentin Remy

AD comments:
There was a memory leak, long standing issue. lru cach is dict with keys are arguments passed to a func, value is the computed, returned value by this function. Problem with implementation is: caches is global one, keeps reference to the class object itself. If geometries out of scope, caching still keeps reference to geometry object, not garbage collected -> mem leak. Solution: Weak reference for geometry objects. 
Problem is solved by this solution, so far it is the one from cpython implementation. 
Also possible: One could go to fully instance-based caching (give up on decorator-approach), also a bit complex solution, but able to ignore self. 
No perfect solution to the problem. Probably, code works like it is and we never have to touch this again.
AS: What is the advantage of the cash method (?)?
AD: Advantage is, it is general solution, also for other parts in gammapy usable.
AS asks a question, AD: Caching is normally used, if it is only expensive to compute, here it is not only exp. to compute but mem-heavy, too. Could be at one point be part of python standard library.
RT adds: Limited set of poss. params, maybe we could also cach specific results to avoid recomputing in some cases?
AS: Tested that the code works, solves the mem-issue.
RT: Benchmarks? AS: Yes, we have to do something over the benchmarks. RT: Added "trigger benchmarks"-label.

* [#5982](https://github.com/gammapy/gammapy/pull/5982) Add class instance caching for WcsGeom and HpxGeom - Quentin Remy

AD comments on behalf of Quentin Remy (QR): QR had the idea that sometimes we create geometries repetitively through mutiple instances Solution -> check existing instances and return only one, if it already exists.
Not completely clear to me (AD), how relevant this is, ..., probably worth introducing it.
Approach does not use hashing (normally needed for caching). Comparison of geometry objects, numerical tolerance for comparison needed, unclear if can be done with hashing, therefore QR solution goes through all instances and compares them.
How many instances of geom object in normal analysis (order of 10 maybe, 100s with datasets?)
Suggestion: Benchmark to show that it does improve performance.
AS: Benchmarks which will have many datasets?
AD: Yes that would be typical case, multiple datasets (at least 10) sharing same geometry.
AS, AD: For stacking helpful.
RT: More clever way to manipulate geometries?
AD: Not meant to be mutable, but are modifiable, WCS object modifiable.
RT: If introduce equality condition -> tolerance condition. Is this in general completely safe? X-Ray data for example, we need to check.
AD: Commented on this in PR, good way to define meaningful hash of geom-object.
AS: What do you mean by that?
AD: Clarifies. "__" returns unique identifier by object, that is defined by property on the object.
What are the properties of a geom-object, that make it equal (???) to other one? Not trivial.
In current state, PR maybe to risky. Two things needed: Hashing of geom object and if definable in meaningful way, second: real world impact?

* tutorial on upper limits [#5933](https://github.com/gammapy/gammapy/pull/5933)
* tutorial for non-detection [#5969](https://github.com/gammapy/gammapy/pull/5969)

RT: What is the status?
  AS: Was maybe discussed last week?
  AS recapitulates the status.
On #5969:
AS recapitulates RTs comments: Two different things: Making PSMap or Fluxmap, or searching for source at specific point.
RT: Use case is, looking for a source. If it is there, have UL on total flux. But so far, specific pos given.
Focus on question of known/expected source at known position. Is the object emitting in my data, or not.
Discussion between AS and RT.

*need to make a decision on the tutorial ordering adaptions [#5949](https://github.com/gammapy/gammapy/pull/5949)

RT: Make API parts more visible, too many things in the API-part. Discussing of "key-steps" part, clarification needed, not everything as key-step.
AS: astro_dark_matter also in recipes. Put it only once? Uncomfortable with name "key-steps", suggests you have to do it first.
KF answers: You can argue, that one should understand the points beforehand. If looking for having extra section for example, things like clustering, theta_square_plot.py would be moved there. Question: What do we want to change for 2.0, if anything.
RT: Maybe keep API part for DM, priors, etc and something specific for smaller use-cases.
Decision regarding astro_dark_matter.py not taken yet. 
KF: Leaving it in the turotials makes more sence yet, not clear how many people go to the recipes.
RT: We can not rely on gammapy-recipes, as long as it is not stable.
KF, RT agrees that specific opinions could be put on the PR.
RT: Decision taking needed soon.


* can we merge? [#5886](https://github.com/gammapy/gammapy/pull/5886/)
* command line option for tutorial setup -- should we remove from all other tutorials now too? [#5941](https://github.com/gammapy/gammapy/pull/5941/)

### PRs and Timeline:
RT: Many open PR yet with 2.0-milestone. Timeline? End of July not realistic.
We need to branch, create 2.0, test it. Who is around?
->AS,KF,BK, available probably in the coming time.
Open point, changelog needs to be prepared, AS agrees to do it.
Citations takes time as well (especially. people from last coding sprint).

* Discussion of PR #5881 "A class for vectorized evaluation of flux uncertainties based on samples". 

RT reports: Inconsistency how evaluation is done e.g. on naima models and ??? models, not uniform yet.
Evaluate function must be vectorizable, otherwise errorband can not be plotted. Do we need fall-back-mechanism?
For-loop eval of all the parameters?
Discussion with AS.
RT: Main thing that needs to be done: Introduce fall back mechanism.
Regarding whole PR, feature really needed, PR should go in for 2.0.

* Brief discussion of PR #5838 "Addition of FitStatistic penalties"

RT: Can come later.

* Brief discussion of PR #5815

 RT: Have to talk with BK.


RT: Regarding code, do we agree to postpone to mid august / Aug 20? 
AS agrees, end of August should be hard deadline.
RT: Branching maybe in two weeks.

* Brief discussion of PR #5910 with KF.

  KF: First changed only name of params, but tests fails. What is final verdict?
  RT: Have to check how it is used in the code.

* Brief discussion of PR #5960. 

AS: Discussed last week. Issue that edges are in true_energy, but cut in recon energies (???).
KF agrees. How to do it?
RT: Not go in direction of weights, rather tresholds. It would otherwise change the logic. You can try to see, if it is possible, but would be different mechanism.
AS: Other option, make very fine bins, the downsample.
RT gives example with problem of throwing first bin.

* Brief discussion of PR #5933:
  
RT, AS: BK made a lot of review comments.
RT: Why need "likelihood_to_pdf"? AS answers. RT: Not sure if this is correct, likelihood is not normalized, not a real pdf.
AS: Is converted to pdf. RT: I think it is not really correct, you can do this in bayesian analysis, obtaining posterior, but in this case it is not what we have, renormalizing it like it is done, not sure if this is correct.
AS: Will remove it. RT: Suggest to change it, otherwise it is fine.


RT: Try to have most docs-PRs merged in one-two weeks time, features as well. Then we can finish in August.

DM: Data-exploration section in dev-doc is under Model Gallery. 
KF answers: Will open a separate PR, fixed this already in other PR.

* Brief discussion Issue #5988,5989,5990.

RT: Agree with the issues that there is a problem, better to have before 2.0



RT ends meeting, AS agrees to lead meeting next week.

### PRs opened last week (less than 8 days ago), not already discussed above: 
* [#5984](https://github.com/gammapy/gammapy/pull/5984) Coherent checksum behavior in the IO function of `Datasets` - Bruno Khélifi

### PRs merged last week (less than 8 days ago), not already discussed above:
* [#5978](https://github.com/gammapy/gammapy/pull/5978) Update dev howto.rst for issue #5972 - Leander Schlegel
* [#5974](https://github.com/gammapy/gammapy/pull/5974) Fix links label for CompoundSpectralModel - Quentin Remy
* [#5968](https://github.com/gammapy/gammapy/pull/5968) Part 3 - Tutorial cleanup - Kirsty Feijen
* [#5958](https://github.com/gammapy/gammapy/pull/5958) Fix TSmapEstimator pad_width - Quentin Remy
* [#5945](https://github.com/gammapy/gammapy/pull/5945) Create exclusion mask for bright stars in FoV - Samantha Wong
* [#5923](https://github.com/gammapy/gammapy/pull/5923) simple fix to problem with EventList printing - Tomas Bylund
* [#5911](https://github.com/gammapy/gammapy/pull/5911) Introducing generic reproject_irf_on_geom functions using FoVFrame classes - Régis Terrier

### other issues opened last week (less than 8 days ago), not already discussed above: 
* [#5986](https://github.com/gammapy/gammapy/issues/5986) Spatial model not frozen in tutorial - None
* [#5985](https://github.com/gammapy/gammapy/issues/5985) `RADECSYS` is deprecated - Bruno Khélifi
* [#5983](https://github.com/gammapy/gammapy/issues/5983) Add format name and format version in  metadata of the serialized files - Bruno Khélifi
* [#5981](https://github.com/gammapy/gammapy/issues/5981) 'EDispKernelMap' object has no attribute 'sample_coord' - Ricardo_zzp
* [#5980](https://github.com/gammapy/gammapy/issues/5980) Improve the Fermi-Lat notebook - Atreyee Sinha

 report (originally) created at 18/07/2025, 07:27:59
