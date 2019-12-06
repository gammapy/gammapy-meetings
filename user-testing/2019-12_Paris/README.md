## Date, location

- Observatoire de Paris salle Danjon (one of the door in the stables facing the canteen [see Map here](Danjon_Obs_Paris.jpg))
- December 4th 2019: 09h30 - 17h30

**The summary of this meeting is detailed [here](summary.md).**

# gammapy user test session

The goal of this user-test is to have people of different expertise perform some common use cases and see what kind of difficulties they could encounter along the way. This is not going to be a tutorial and the idea is to be that little mouse sneaking in the office of a gammapy user and see what could be improved in terms of user experience.

We have prepared different use cases of different complexities and each participant can select a topic and work through it during the day. Guiding you too much with directed advice would defeat the purpose of the test.

For some simple use cases (installation, simulation) we plan to record what's on the screen for a few users to see how they navigate through the doc and examples. 
Recording software : Kazam (Linux: sudo apt-get install kazam ), [Chrome browser](https://www.screencastify.com) (all systems), or QuickTime on Mac.

**Important note**: this is not an exam and we’re are not testing your Python or gammapy skills, we’re testing the tool.
There are no wrong answers and don’t be polite about the software  ;-) 

Say something if you notice:
- a missing/unclear/missleading documentation
- lack of coherence in API
- a function not behaving as expected
- a possible bug
- anything that bothers you

**Issue report**
Write your comments and issues on this shared Doc [URL](https://docs.google.com/document/d/1tA0Xz64RviKKfJZZp0GLovb3TrFLgoCFR3U7KGgBsaI/edit?usp=sharing) with :
- your name, type of issue (bug, documentation, API)
- if it concerns a possible bug, please write a minimal reproducible example

The test will be carried out with gammapy v0.15 which will be released on Dec 3rd.


The use cases below require the [HESS DL3 DR1 data](https://www.mpi-hd.mpg.de/hfm/HESS/pages/dl3-dr1/), the CTA IRF, and DC1 data.
DC1 data are heavy and will be circulated with a USB key if you don't have them.


## Use cases to be tested

### installation from scratch (1, 2 people max)
    - check multiple environment handling 
    - find relevant doc 

### Simulation with CTA DC1 IRFs:
Using 1dc IRF South_z20_50h

#### Simulate a 3D observation with a point source (then extended):
        - Source param: PowerLaw, Norm= 1e-13 cm^2s^-1-TeV ^-1 at 1 TeV, Index=2.5, Obs_Time=10h
        - Produce significance map
        - Fit position and spectra (and extension?) 
            - Estimate errors on parameters

#### Simulate several 1D observations of different durations
        - Source param: same as above
        - Estimate source significance at each time and determine how much time needed to reach >5 sigma?
        - Perform fit in each time and determine how much time is needed to constrain spectral index better than 0.1
        - Redo in 3D?
        
#### Simulate 1D observations from a given light curve:
        - Assume:
          -F propto (t/1h)^-1
          - At t0 :
            - Norm = 1e-11 cm^2s^-1-TeV ^-1 at 1 TeV 
            - index = 3
        - Simulate and reconstruct flux light curve

### Data reduction:

#### Analysis of MSH 15-52 (HESS DL3 DR1) (possibly split in 2 different use cases):
        - excess and significance map with RingBackground
            - ON and OFF significance distribution
        - 1D spectrum (reflected region background):
            - Plot flux points with butterfly
            - Plot confidence contours with index vs norm
        - 3D analysis
     
#### Analyze PKS 2155 flare (HESS DL3 DR1) with HLI:
        - Find relevant runs from flare date
        - Make image and spectra of the full night data 
        - Extract flare light curve in N minutes time bins (see paper)
    
#### GC CTA DC1 analysis (with less than 30 runs):
        - Produce Excess, Significance maps with 3D bkg subtraction 
        - Define Skymodel (J1745-303 & G0.9+0.1) with yaml file
        - Perform a multiple 3D source fit 
        - Confidence contours of the 2 sources 
        - Add diffuse emission:
            - confidence of diffuse norm vs J1745 norm.

#### Experimental: Re-do joint crab analysis:
        - spectra extraction for the various instruments and export to disk
        - Reload and joint fit
        - Confidence contours joint and per instrument 

## Participants
 1. Fabio Acero, [facero](https://github.com/facero)
 2. Régis Terrier, [registerrier](https://github.com/registerrier)
 3. Bruno Khelifi, [BKhelifi](https://github.com/bkhelifi)
 4. Atreyee Sinha, [AtreyeeS](https://github.com/AtreyeeS)
 5. Luca Giunti, [luca-giunti](https://github.com/luca-giunti)
 6. Catherine Boisson 
 7. Santiago Pita, [santiagopita](https://github.com/santiagopita)
 8. Anne Lemière, [AnneLemiere](https://github.com/AnneLemiere)
 9. Karl Kosack, [kosack](https://github.com/kosack)
 10. Thierry Stolarczyk, [tstolarczyk](https://github.com/tstolarczyk)
 11. Francois Brun
 12. Jean-Philippe Lenain, [jlenain](https://github.com/jlenain)
 13. Antonio Tutone
 14. Pooja Sharma
 15. Gabriel Emery
 16. Mathieu Servillat, [mservillat](https://github.com/mservillat)
 
 
