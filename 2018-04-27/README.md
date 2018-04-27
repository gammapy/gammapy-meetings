# Gammapy Telcon

* Friday, April 27, 2018 at 11 am
* CTA eZuce, password "gammapyregular".  The connection details are [here](ConnectionDetails.txt)

# Agenda

* Gammapy updates (Christoph)
  * A lot of work on 3D analysis in the past weeks by Johannes, Régis and me.
  * Still very much work in progress, but to see where we are in gammapy master:
    * http://docs.gammapy.org/dev/notebooks/analysis_3d.html
    * http://docs.gammapy.org/dev/notebooks/simulate_3d.html
    * Model XML I/O coming later today: https://github.com/gammapy/gammapy/pull/1397
  * We will is to release Gammapy v0.8 on Monday, May 7
  * If you present Gammapy results at the Orsay CTA meeting May 14-18,
    please re-run with Gammapy v0.8
  * Next week we will continue development on 3D as well as fixes for 1D analysis
    and do as much as possible. If you have time to help, please get in touch with me.
  * We are aware of the following two high-priority issues, those will be fixed next week.
    If there are other important things for v0.8, please let us know!
    * LC estimator issue - from Catherine DC-1 AGN check - see [GH 1385](https://github.com/gammapy/gammapy/pull/1385)
    * Reflected regions issue - from Cyril CTA PeVatron analyses - see [GH 1336](https://github.com/gammapy/gammapy/issues/1336)
* How to document gammapy analysis for the DC1 (Roberta)

For each analysis we should deliver only one file, i.e. a tarball mandatorily including:

1. code used to produce the results, either a python script or a notebook. At the very beginning the notebook should show the version of the python packages used.

2. Analysis outputs (skymaps, spectral points and lightcurves) in machine-readable format. In particular, skymaps in FITS, spectral and lightcurve points preferibly in ecsv format. You can also store the spectral points as an astropy.table in a FITS file. At the moment there is no official definition of DL4.

3. A yaml file containing the best fit parameters with the correponding covariance matrix. This is needed to plot the butterfly.

4. A readme file including the configuration setup used for the analysis

5. A general script/makefile that runs all the analysis in batch mode and at the very end it creates the tarball to be uploaded to the redmine page. That's useful to maintain working examples with the last version of the code. As log of the analysis we can save the html of the notebook after having rerun it.

You can use the notebooks for the HESS J1702 as example on how to save/store the information. In the same directory you can find the make.py I created for this analysis. It is just an example, we are not asking you to use click if you do not like it. click is a Python package for creating command line interfaces.

https://github.com/gammasky/cta-analyses/blob/master/dc-1-checks/hess_j1702/


## Reminder

* Gammapy docs: http://docs.gammapy.org
* Gammapy webpage: http://gammapy.org/
* Gammapy development: github.com/gammapy/gammapy

Next Gammapy meetings: http://gammapy.org/news.html

See http://gammapy.org/contact.html for contact info, e.g. mailing list
for announcements or questions, Slack for help or to join development, ...
