# Gammapy Developer Meeting 
 * Friday, October 09, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

Attendees: 

# Agenda
## General information
### Meeting notes

- automatic notes & transcription has been disabled by University
- need new tool for that

### Domain name

- gammapy.org is still owned by Christoph
- check how to transfer domain name

### New v2.2 release date
- Decision:
 - release on Nov 13th
 - feature freeze Oct 30th
- Note DM functionalities require #6880 #6876 to be merged
- Review of v2.2 roadmap and sorting of priorites
 - 7 issues remain TODO with P0 priority
 - Non finished issues with lower priority will be postponed at feature freeze
   

## Ongoing projects

### Validation: PIG 33

- [#6886](https://github.com/gammapy/gammapy/pull/6886) - Marie
- new subpackage: gammapy.io.fits
- 3 levels:
 - format registry & `DefinitionValidator`
	- `ValidationReport`  resolves HDU class and perform check and return a report
	- applied on `DataStore`
- example usage from existing prototype
 - example validation report table for a datastore
	- question on how to add a new format: few lines if few differences
	- question on SDC format validation: done already for test data in combination with Karl's tool.
- what about DL4/DL5 definition?
 - need to organize discussions
- have the format definition as json files to serve as documentation?
- try to have comments quickly to implement fast
  
### Drift scan support:

- immediate tasks for 2.2 is clear: [#6882](https://github.com/gammapy/gammapy/pull/6882)
- later need further research to understand how to organize maker
- Note: irf projection utilities are exposed in the tutorial.
		- decision: rely instead on existing IRF Map objects.

### DM
  
- use dwarves CTAO paper as reference in benchmarks/validation
- question about [#6880](https://github.com/gammapy/gammapy/pull/6880)
 - decision: keep private. remove from __init__
	- remove fragment

## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6887](https://github.com/gammapy/gammapy/pull/6887) Fix PSF table containment fraction for large rad values (#6853) - Esther
* [#6886](https://github.com/gammapy/gammapy/pull/6886) PIG 33: proposal for data format validation - Marie-Sophie Carrasco
* [#6885](https://github.com/gammapy/gammapy/pull/6885) Change the default spectra source from PPPC4DMID to CosmiXs - Alexander Cerviño Cortínez
* [#6884](https://github.com/gammapy/gammapy/pull/6884) Fix LogParabola2SpectralModel.epeak value - Quentin Remy
* [#6882](https://github.com/gammapy/gammapy/pull/6882) Deprecate `make_map_exposure_true_energy` as part of cleaning up the pointing object - Tomas Bylund
* [#6880](https://github.com/gammapy/gammapy/pull/6880) Creation of LogSpaceGaussiaPrior and use it as an astrophysical factor prior (Dark Matter) - Alexander Cerviño Cortínez

### PRs merged last week (less than 8 days ago): 
* [#6879](https://github.com/gammapy/gammapy/pull/6879) Backport PR #6867 on branch v2.0.x (Fix memory blowup when computing covariance of many-parameter models) - Lumberbot (aka Jack)
* [#6878](https://github.com/gammapy/gammapy/pull/6878) Bump astral-sh/setup-uv from 10.0.1 to 10.2.0 - None
* [#6867](https://github.com/gammapy/gammapy/pull/6867) Fix memory blowup when computing covariance of many-parameter models - Ahmed Mahmoud
* [#6850](https://github.com/gammapy/gammapy/pull/6850) ASDF: serialization for Models - Basmala Hekal
* [#6849](https://github.com/gammapy/gammapy/pull/6849) ASDF: serialization for MapDataset and MapDatasetOnOff - Basmala Hekal
* [#6838](https://github.com/gammapy/gammapy/pull/6838) [catalogs] Add Fourth Fermi-LAT Catalog of High-Energy Sources (4FHL) - Michele Peresano
* [#6828](https://github.com/gammapy/gammapy/pull/6828) Handle JFactory central pixel - Júlia Mamprim
* [#6805](https://github.com/gammapy/gammapy/pull/6805) Ensure `TimeMapAxis` start and stop values are exported to table in isot format - Tomas Bylund
* [#6783](https://github.com/gammapy/gammapy/pull/6783) Dark Matter module: Part 2: Update Dark Matter OBSERVATION SIMULATION Tutorial - Alexander Cerviño Cortínez
* [#6777](https://github.com/gammapy/gammapy/pull/6777) Dark Matter module documentation upgrade - Alexander Cerviño Cortínez
* [#6774](https://github.com/gammapy/gammapy/pull/6774) Dark Matter module: Part 3: Updated Dark Matter tutorial v2.1 of Gammapy - Full analysis Tutorial - Alexander Cerviño Cortínez

### issues opened last week (less than 8 days ago): 
* [#6883](https://github.com/gammapy/gammapy/issues/6883) Document how to use Docker image - Daniel Morcuende
* [#6881](https://github.com/gammapy/gammapy/issues/6881) Double check ConfidenceLevel => deltaTS for errors or Upper-Limits - Fabio Acero

 report created at 09/10/2026, 08:29:59
