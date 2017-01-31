# Python for gamma-ray astronomy bootcamp (Feb 2017, MPIK, Heidelberg)

## Summary

* Location: [MPIK Heidelberg](https://www.mpi-hd.mpg.de/mpi/en/start/).
* Start: **Monday, Feb 27, 2017 at 9 am**
* End: **Wednesday, March 1, 2017 at 4 pm**
* Tutorial sessions end on Wednesday. On Thursday and Friday, rooms and offices
  as well as Gammapy and ctapipe experts are available though (see below).
* Room:
  * Monday to Wednesday: Conference room in the library building #12 (see [MPIK site map](https://www.mpi-hd.mpg.de/mpi/en/contact/access-and-site-map/), up the stairs, to the right)
  * Thursday / Friday: "Glaskasten" on the second floor of the Bothe lab and offices.
* Contact: If you have a questions, or would like to join, please email [Christoph Deil](https://github.com/cdeil) and [Jason Watson](https://github.com/watsonjj).

## About

**We are organising a 3 day "bootcamp" to get people started or become better with Python, Numpy, Astropy, Gammapy, ctapipe, ... as a user or contributor.**

**This will be mostly an MPIK-internal workshop, but everyone is welcome to join!**
If you come visit, let us know if you need a recommendation for a hotel or want to stay in the MPIK guest house.

There's a wide range of existing skill levels ("never used Python" to "Gammapy
or ctapipe developer"). We'll have to compromise a bit. We'll start with
absolute basics on day 1, and go all the way to use Gammapy and ctapipe for some
data analysis and make a first pull request with a small contribution on day 3.
It'll be hands-on, with exercises. We'll roughly cover the things listed on
Slide 5 here:
https://github.com/gammapy/gammapy-extra/raw/master/presentations/2017-01-13_Gammapy.pdf
but level and content will be adjusted to make it useful for most people based
an your replies below.

There will be larger Gammapy meeting (at APC Paris the week before, see [2017-02_Paris.md](2017-02_Paris.md)) and ctapipe
meetings (at MPIK) in the coming months. We also plan to have this be a kick-off
bootcamp, and then start regular bi-weekly "code café" or "analysis café" where
we meet for a few hours. More about that later.

## Agenda

We will develop a detailed agenda and post tutorial materials before the workshop. For now, this is a rough outline of what is planned.

The workshop will be very hands-on, basically a series of short explanations /
demos followed by a small exercise.

### Monday

* We will start the Python class at 9:30 am.
* If you need to install Python, please come already at 9:00 am.
* Conference room in the library building #12 (see [MPIK site map](https://www.mpi-hd.mpg.de/mpi/en/contact/access-and-site-map/), up the stairs, to the right)

Morning (Christoph Deil):

* Make sure everyone is set up
    * Install Anaconda: https://www.continuum.io/downloads
    * This should work: `python -c 'import astropy'`
    * Download the tutorial materials (mostly IPython notebooks) for day 1.
* Python
    * Develop a mental model how Python variables and code execution works (not like C at all) using http://pythontutor.com/ 
    * Executing Python scripts and interactive terminal use
    * Numbers, strings, tuples, lists, dictionaries
    * Python functions in detail
    * Basics of Python classes
    * Python modules, packages, import
    * Understanding Python errors / exceptions / tracebacks
    * Reading and writing data to files (text, CSV, JSON, YAML)
    * See https://github.com/jakevdp/WhirlwindTourOfPython

Afternoon (Daniel Parsons):

* Scientific Python (Daniel Parsons)
    * IPython terminal and notebook
    * Numpy and array-oriented cmputing
    * A few small examples using scipy, matplotlib and pandas
    * See https://github.com/jakevdp/PythonDataScienceHandbook

### Tuesday

Morning (Axel Donath):

* Astropy
    * FITS and other I/O
    * Working with images and WCS
    * Working with tables
    * Sky coordinates and times
    * Let us know what you're interested in
    * See http://www.astropy.org/astropy-tutorials/

Afternoon:

* Short introduction to Gammapy (Axel Donath and Johannes King)
    * See [notebooks](http://nbviewer.jupyter.org/github/gammapy/gammapy-extra/blob/master/index.ipynb) and [docs](http://docs.gammapy.org/en/latest/)
* Short introduction to ctapipe (Jason Watson)
    * See [notebooks](https://github.com/cta-observatory/ctapipe/tree/master/examples/notebooks) and [docs](https://cta-observatory.github.io/ctapipe/)

### Wednesday

Morning:

* Questions, extras, exercises on topics from last two days,
  depending on feedback from participants
* Series of short demos of more advanced packages / topics, e.g.
    * pytest (a [tutorial](https://github.com/jiffyclub/pytest-features))
    * Sphinx (a [tutorial](https://github.com/cdeil/sphinx-tutorial))
    * Plotting with bokeh (Jason Watson)
    * Timing and profiling code

Afternoon:

* From Gammapy / ctapipe user to developer:
    * Coding with PyCharm, running tests
    * Conda and pip in more detail (how does install and import work?)
    * Git and Github - https://guides.github.com/
    * Everyone makes their first pull request

### Thursday and Friday

If there is interest, we can use Thursday and Friday to split up and into groups
of 2-3 people and do some detailed discussions or pair coding. E.g. to help you
to script your H.E.S.S. or CTA science analysis, or to work on a pull request
for ctapipe or Gammapy to add some feature you want.

Thursday afternoon is a celebration for Heinz Völk.

## Participants

All MPIK except where noted.

* [Christoph Deil](https://github.com/cdeil)
* [Jason Watson](https://github.com/watsonjj)
* [Johannes King](https://github.com/joleroi)
* [Axel Donath](https://github.com/adonath)
* [Roberta Zanin](https://github.com/robertazanin)
* Sabrina Casanova
* German Hermann (day 1 only)
* Justus Zorn
* Daniel Galindo (Universitat de Barcelona)
