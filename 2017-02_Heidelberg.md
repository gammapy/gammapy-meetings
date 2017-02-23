# Python for gamma-ray astronomy bootcamp (Feb 2017, MPIK, Heidelberg)

## Summary

* Location: [MPIK Heidelberg](https://www.mpi-hd.mpg.de/mpi/en/start/).
* Start: **Monday, Feb 27, 2017 at 9 am**
* End: **Wednesday, March 1, 2017 at 4 pm**
* Tutorial sessions end on Wednesday. On Thursday and Friday, rooms and offices
  as well as Gammapy and ctapipe experts are available though (see below).
* Room:
  * Monday to Wednesday: Central seminar room in the library building #12 (see [MPIK site map](https://www.mpi-hd.mpg.de/mpi/en/contact/access-and-site-map/), ground floor, to the right)
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

## Prepare

To prepare for day 1, please do the following two steps:

1. Install software
2. Download materials

### 1. Install software

Please come with your laptop and software already installed. We recommend you
install Anaconda from https://www.continuum.io/downloads . Feel free to ask for
help with installation in person or via email before the workshop. Or come early
on day one and we'll help you get set up.

*(Using a Python installation on a server (e.g. lfs1 at MPIK) is possible, but
probably won't work well, because we will use Jupyter notebooks a lot, and
experience shows that using them via a remote server is difficult to set up and
often slow and unpleasant to use, i.e. not a good solution to get started.)*

To check that your installation and setup is OK, try to exectue the following Python code:
* `print('hello world!')`
* `import numpy`
* `import scipy`
* `import matplotlib`
* `import astropy`

If you get an `ImportError` you don't have all the software we will use.

Try to execute `print('hello world')` from three places:
1. Python terminal (type `python` to start)
2. IPython terminal (type `ipython` to start)
3. IPython notebook (= Jupyter notebook) (type `jupyter-notebook` to start)

You can find instructions how to do the installation and how to start Python and IPython and execute your first Python code here:

* Section 1 ("Introduction", install section at the bottom) and 2 ("How to run Python code") from ["A Whirlwind Tour of Python"](http://nbviewer.jupyter.org/github/jakevdp/WhirlwindTourOfPython/blob/master/Index.ipynb)
* More information for IPython (how to start and execute notebooks) is available in Chapter 1 of the ["Python Data Science Handbook"](http://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb)

### 2. Download materials

* Make a directory on your computer where you'll put everything, e.g.:
    * `mkdir python-tutorials`
    * `cd python-tutorials`
* Get the tutorial materials, i.e. the Jupyter notebooks from Jake's courses:
   * https://github.com/jakevdp/WhirlwindTourOfPython
   * https://github.com/jakevdp/PythonDataScienceHandbook
* As for any Github repo, you can get it via `git clone`:
  * `git clone https://github.com/jakevdp/WhirlwindTourOfPython.git`
  * `git clone https://github.com/jakevdp/PythonDataScienceHandbook.git`

This is all you will need for day 1.

For day 2 and 3 there will be other Python packages for you to install (Astropy,
Gammapy, ctapipe, ...) and tutorial materials and example datasets to download.

For Gammapy, you will have to get the development version of Gammapy (clone from
Github, as well as the `gammapy-extra` repository, which contains the example
datasets and Jupyter notebooks. Instructions how to do this are given in the
`setup` section here:
http://nbviewer.jupyter.org/github/gammapy/gammapy-extra/blob/master/index.ipynb


## Agenda

We will develop a detailed agenda and post tutorial materials before the workshop. For now, this is a rough outline of what is planned.

The workshop will be very hands-on, basically a series of short explanations /
demos followed by a small exercise.

### Monday

* We will start the Python class at **9:30 am**.
* Conference room in the library building #12 (see [MPIK site map](https://www.mpi-hd.mpg.de/mpi/en/contact/access-and-site-map/), up the stairs, to the right)
* If you need with setup, please come already at **9:00 am**.
* See the instructions for software installation and how to download materials above in the "Prepare" section.

Morning session on "Python" (Christoph Deil):

* Basically the plan is that we go through part of the material from ["A Whirlwind Tour of Python"](http://nbviewer.jupyter.org/github/jakevdp/WhirlwindTourOfPython/blob/master/Index.ipynb) and do a combination of presentation, demos and exercises. Questions are welcome at any time! Let me know if I should go faster, slower or move on to something else.
* Make sure everyone is set up (see section "Prepare" above)
* Executing Python scripts and interactive terminal use
* Numbers, strings, tuples, lists, dictionaries
* Python functions (in some detail)
* Python classes (basics)
* Python modules, packages, import
* Understanding Python errors / exceptions / tracebacks
* Maybe: Reading and writing data to files (text, CSV, JSON, YAML)

Usually Python code is very intuitive and easy to understand. But we haven't
really explained how Python works today. If you come from a C / C++ background,
or if you take a step back and think about how Python code execution really
works, some things (especially how "variables" work) might blow your mind.

If you'd like to develop a mental model of how Python works, or learn a bit how
it's wired together in the background to make it work the way it does, I
recommend you study the following resources:

* http://foobarnbaz.com/2012/07/08/understanding-python-variables/
* Code execution visualisations at http://pythontutor.com/
* [Python epiphanies notebook](http://nbviewer.jupyter.org/github/oreillymedia/python_epiphanies/blob/master/Python-Epiphanies-All.ipynb)

Afternoon session on "Scientific Python" (Daniel Parsons):

* IPython terminal and notebook
* Numpy and array-oriented cmputing
* A few examples using scipy, matplotlib and pandas
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

* Alba Fernandez-Barral
* [Axel Donath](https://github.com/adonath)
* [Christoph Deil](https://github.com/cdeil)
* Daniel Galindo (Universitat de Barcelona)
* German Hermann (day 1 only)
* Harm Schoorlemmer
* [Jason Watson](https://github.com/watsonjj)
* [Johannes King](https://github.com/joleroi)
* Justus Zorn
* Kester Smith (MPIA, Heidelberg)
* Pooja Surajbali
* [Roberta Zanin](https://github.com/robertazanin)
* [Ruben Lopez-Coto](https://github.com/rlopezcoto)
* Sabrina Casanova
* Stefan Eschbach (University of Erlangen)
* Vincent Marandon
