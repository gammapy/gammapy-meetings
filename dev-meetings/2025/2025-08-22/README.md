# Gammapy Developer Meeting 
 * Friday, August 22, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack)

Attendees: Régis Terrier (RT), Bruno Khélifi (KF), Atreyee Sinha (AS), Tomas Byland (TB), Kirsty Feijen (KF), Axel Donath (AD)

# Agenda

Discussion on testing of gammapy 2.0rc1. AS has had the opportunity to browse the docs and run some analysis.
- No immediate issues seen.
- BK says that binder for some tutorial is not working. Made a test on the dev doc.


RT ran the benchmarks/validations and most of them look relatively consistent. 
- one extra data point in the crab/plots_flux-points-1d.png (BK: extra point is outside the energy range of the model, could it be a mask fit?)
- appears that this relates to having the upper limit vs not. Value previously was nan and now it is 8e-17. It could be to do with the change by Quentin.
- RT: doing better with the upper limits but it still needs work
- now we have a result for the lightcurve (which previously we had a plotting issue)
- RT: looks like we are okay with the validations we we will merge this


We should add some further information to the release notes (RT).

#6095 can be added in for v2.0 - KF just some simple adjustments to the docs. By adding plt.show it avoid having the axes being returned in the tutorials as well.

#6106 was merged to avoid the warning in the analysis-3d tutorial. RT is should be fine because we only use this in one instance, so a simple fix is prefered. We don't gain enough to create our own method (AS)


#6108 should be postponed to v2.1

#6105 is the last thing for v2.0. We merged this as it is a small note about sherpa (RT,AS).

Discussion about the requirement file for the pip installation (BK, #6091).
- Need to decide if we do this or not (RT). We had recent questions about astropy7.1 being installed and things being broken, also similarly with matplotlib, so it could be useful to have this file (RT).
- Need to decide where we could put this info in the docs if we decide to add it (RT). It can be mentioned in the getting-started with the pip install (AS). We should kept it simplictic there but rather add something to the "Using pip" section (RT). It makes sense to have it in this section (KF).
- It doesn't show that you should create an env and then install, so we could show the uses how to do that (RT).
- Should we really include this, it seems to make more effort for us to maintain this (AD). By now the convention is log files to have a reproducable env (AD). We don't want a reproducable env, we would like the user to install without incompatibilities (RT).
- It is unclear whether is worth doing this because really a "pip install gammapy[all]" should work for all, and we should have the setup.cfg better setup to work for that (AD). The same could also be said for the use of conda. Don't see how future versions wont break if we use this method with setup.cfg (RT).
- In the end, if we keep the requirements.txt as the same as the conda env file then we could go ahead as this is a small effort (AD). Recommend to stay as is for now, but gradually move towards using pixie and uv (AD).
- We should create a discussion on this

We don't need a second release candidate. We can go ahead now that everything is okay. 

Binder is not working (BK). It could be because they do not work on the dev or pre-releases (RT, AD). We should be able to get it working for each version, by default defining an env that uses the dev version, then adjust as needed, on release change it to the version and add the tags (AD).


We should announce a user call in line with v2.0 around mid September (AS, RT). Could include the new MCMC and bayesian, and also the new Fermi analysis, we can ask Fabio and Quentin for that (AS). After September 22nd.



### PRs opened last week (less than 8 days ago): 
* [#6102](https://github.com/gammapy/gammapy/pull/6102) jfactory integral calculation description - Kirsty Feijen
* [#6097](https://github.com/gammapy/gammapy/pull/6097) Update release.rst after 2.0 release - Atreyee Sinha
* [#6095](https://github.com/gammapy/gammapy/pull/6095) jupytext requires plt.show - Kirsty Feijen
* [#6094](https://github.com/gammapy/gammapy/pull/6094) Fix release notes for v2.0 - Kirsty Feijen
* [#6093](https://github.com/gammapy/gammapy/pull/6093) Suppress pydantic warnings - Kirsty Feijen

### PRs merged last week (less than 8 days ago): 
* [#6104](https://github.com/gammapy/gammapy/pull/6104) Backport PR #6101 on branch v2.0.x (Add instrument names in tutorials  data section) - Lumberbot (aka Jack)
* [#6103](https://github.com/gammapy/gammapy/pull/6103) Backport PR #6100 on branch v2.0.x (Update installation for windows instruction) - Lumberbot (aka Jack)
* [#6101](https://github.com/gammapy/gammapy/pull/6101) Add instrument names in tutorials  data section - Atreyee Sinha
* [#6100](https://github.com/gammapy/gammapy/pull/6100) Update installation for windows instruction - Atreyee Sinha
* [#6099](https://github.com/gammapy/gammapy/pull/6099) Backport PR #6098 on branch v2.0.x (Clearer appearance for the click scipts in the documentation) - Lumberbot (aka Jack)
* [#6098](https://github.com/gammapy/gammapy/pull/6098) Clearer appearance for the click scipts in the documentation - Kirsty Feijen
* [#6092](https://github.com/gammapy/gammapy/pull/6092) Backport PR #6089 on branch v2.0.x (Add names to HowTo, to allow linking) - Lumberbot (aka Jack)
* [#6090](https://github.com/gammapy/gammapy/pull/6090) Backport PR #5939 on branch v2.0.x (Update citation.cff for v2.0) - Lumberbot (aka Jack)
* [#6089](https://github.com/gammapy/gammapy/pull/6089) Add names to HowTo, to allow linking - Kirsty Feijen
* [#6088](https://github.com/gammapy/gammapy/pull/6088) Backport PR #6010 on branch v2.0.x (Changelog for 2.0) - Lumberbot (aka Jack)
* [#6087](https://github.com/gammapy/gammapy/pull/6087) Backport PR #6048 on branch v2.0.x (Update minimal dependencies for v2.0) - Lumberbot (aka Jack)
* [#6086](https://github.com/gammapy/gammapy/pull/6086) Backport PR #6069 on branch v2.0.x (Remove TODO) - Lumberbot (aka Jack)
* [#6085](https://github.com/gammapy/gammapy/pull/6085) Backport PR #6061 on branch v2.0.x (Workflow to check the building of wheels nightly) - Lumberbot (aka Jack)
* [#6084](https://github.com/gammapy/gammapy/pull/6084) Backport PR #6072 on branch v2.0.x (Adapt ObservationsEventsSampler.run docstring to observations) - Lumberbot (aka Jack)
* [#6083](https://github.com/gammapy/gammapy/pull/6083) Backport PR #6077 on branch v2.0.x (Fix evaluate_error for PiecewiseNormSpectralModel) - Lumberbot (aka Jack)
* [#6082](https://github.com/gammapy/gammapy/pull/6082) Backport PR #6074 on branch v2.0.x (Fix warnings on deprecated license in classifiers and universal bdist wheel options) - Lumberbot (aka Jack)
* [#6081](https://github.com/gammapy/gammapy/pull/6081) Backport PR #6078 on branch v2.0.x (Update Nested Sampling tuto with error band from samples) - Lumberbot (aka Jack)
* [#6079](https://github.com/gammapy/gammapy/pull/6079) Backport PR #6055 on branch v2.0.x (Change location and details of rad max tutorial) - Lumberbot (aka Jack)
* [#6078](https://github.com/gammapy/gammapy/pull/6078) Update Nested Sampling tuto with error band from samples - Fabio Acero
* [#6077](https://github.com/gammapy/gammapy/pull/6077) Fix evaluate_error for PiecewiseNormSpectralModel - Quentin Remy
* [#6074](https://github.com/gammapy/gammapy/pull/6074) Fix warnings on deprecated license in classifiers and universal bdist wheel options - Daniel Morcuende
* [#6072](https://github.com/gammapy/gammapy/pull/6072) Adapt ObservationsEventsSampler.run docstring to observations - Kirsty Feijen
* [#6069](https://github.com/gammapy/gammapy/pull/6069) Remove TODO - Kirsty Feijen
* [#6061](https://github.com/gammapy/gammapy/pull/6061) Workflow to check the building of wheels nightly - Daniel Morcuende
* [#6048](https://github.com/gammapy/gammapy/pull/6048) Update minimal dependencies for v2.0 - Régis Terrier
* [#6047](https://github.com/gammapy/gammapy/pull/6047) Bump actions/first-interaction from 1 to 2 - None
* [#6010](https://github.com/gammapy/gammapy/pull/6010) Changelog for 2.0 - Atreyee Sinha

### issues opened last week (less than 8 days ago): 
* [#6091](https://github.com/gammapy/gammapy/issues/6091) Post 2.0rc1 update and remaining PRs - Bruno Khélifi

 report created at 22/08/2025, 07:22:54
