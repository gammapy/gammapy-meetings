
# Binary call

* Thursday, March 8, 2018 at 3 pm
* CTA eZuce, no password required -> anyone interested welcome to join!
* Connection details are [here](ConnectionDetails.txt)

## Participants

* Christoph, Regis, Emma, Marion, Arache, David, Jean-Philippe & Lab

# Agenda

* Issues on Binary analysis 
* Recent devlopment on Binary Analysis with Gammapy
* Discussion on further devlopment
* Presenation by Lab [here](Gammapy_binary_call.pdf)
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
  
# Minutes
 
 * Since we don’t have unbinned analysis, Christoph proposes to have a time-interval based analysis in gammapy. Time-based analysis strategies are somewhat similar for some sources, e.g. gamma-ray binaries, pulsars. So, the plan is to develop some tools within gammapy to support timing analyses.
* At present, we have PhaseCurve class (http://docs.gammapy.org/dev/api/gammapy.time.models.PhaseCurve.html) to assign phases to events/observations, which is required to do phase folded analysis. The proposal is to do some more development based on the requirements for these sources.
* Regis proposes that we should have notebooks with prototypes for each of the use cases, i,e. for binaries, pulsars and AGNs, using the available tools of gammapy.

* Based on requirements on different use cases, we can have something simpler in gammapy. To understand the requirements well,  we decided to have notebooks for all these use cases. Lab will prepare a script to show the analysis of the binary based on available tools in gammapy (e.g. LightCurveEstimator class of Gammapy. AGN light curve will is expected to be produced using Gammapy. Marion will prepare a notebook for Pulsar analysis using available classes of Gammapy. After evaluating those scripts and after the dedicated call for pulsar analysis with PINT on 16th March at 2 pm, we will decide our future course of action. 

* Lab is likely to present binary analysis in the  biweekly CTA 1DC-call

