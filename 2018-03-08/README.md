
# Binary call

* Thursday, March 8, 2018 at 3 pm
* CTA eZuce, no password required -> anyone interested welcome to join!
* Connection details are [here](ConnectionDetails.txt)

# Agenda

* Issues on Binary analysis 
* Recent devlopment on Binary Analysis with Gammapy
* Discussion on further devlopment

# Some thoughts/proposal

* Methodology
  * Assign phase to each of the events following ephemeris
  * Group the events in 10 phase bins
  * Run standard analysis on the events for each of the phase bins
  * calculate intergral flux for each bin. This is basically Phase-folded light curve
  * Model the phase-folded light curve
* Proposal   
  * a method/function to calculate phase and add to the eventlist
  * a method/function to group data into user-defined phase bins
  * a method/function to calculate differential flux for those given bins
  * a method/function to calculate integral-flux for those phase bins
  * methods/functions to model both differential flux and phase-folded light curve 
  * a method/function to test the periodicity
  
