# gammapy user test session

Context and some bla bla

## Date, location

- Observatoire de Paris salle XX
- December 4th 2019: 09h30 - 17h00

## Use cases to be tested

### installation from scratch (1 ou 2 people max)
    - check multiple environment handling 
    - find relevant doc 

### Simulation with CTA DC1 IRFs:
   
#### Simulate a 3D observation 3D with a point source (then extended):
        - Extract significance map
        - Fit position and spectra (and extension?) 
            - Estimate errors on parameters

#### Simulate several 1D observations of different durations
        - Estimate significance at each time and determine how much time needed to reach >5 sigma?
        - Perform fit in each time and determine how much time is needed to constrain spectral index better than 0.1
        - Redo in 3D?
#### Simulate 1D observations 1D from a given light curve:
        - Assume:
          -F propto (t/1h)^-1
          - At t0 :
            - N_O = 1e-11 cm^2s^-1-TeV ^-1 at 1 TeV 
            - index = -3
        - Simulate and reconstruct light curve

### Data reduction:

#### Analysis of MSH 15-52 (HESS DL3 DR1) (possibly split in 2 different use cases):
        - excess and significance map with RingBackground
            - ON and OFF significance distribution
        - 1D spectrum (reflected region background:
            - Plot flux points with butterfly
            - Plot confidence contours with index vs norm
        - analyse 3D
     
#### Analyze PKS 2155 flare (HESS DL3 DR1) with HLI:
        - Find relevant runs from flare date
        - Make image and spectra of the full night data 
        - Extract flare light curve in N minutes time bins (see paper)

#### Re-do joint crab analysis:
        - spectra extraction for the various instruments and export to disk
        - Reload and joint fit
        - Confidence contours joint and per instrument 
    
#### GC DC1  analysis (with less than 30 runs):
        - Try to perform a multiple 3D source fit (J1745-303 & G0.9+0.1)
        - Define tested model with yaml file
        - Confidence contours of the 2 sources 
        - Add diffuse emission:
            - confidence of diffuse norm vs J1745 norm.


## Participants
 1. Fabio Acero (facero)[https://github.com/facero]
 2. Régis Terrier (registerrier)[https://github.com/registerrier]
 3. Bruno Khelifi (BKhelifi)[https://github.com/bkhelifi]
 4. Luca Giunti (luca-giunti)[https://github.com/luca-giunti]
 5. Catherine Boisson 
 6. Santiago Pita (santiagopita)[https://github.com/santiagopita]
 7. Anne Lemière (AnneLemiere)[https://github.com/AnneLemiere]
 8. Karl Kosack (kosack)[https://github.com/kosack]
 9. Atreyee Sinha (AtreyeeS)[https://github.com/AtreyeeS]
 10.
 11.
 
