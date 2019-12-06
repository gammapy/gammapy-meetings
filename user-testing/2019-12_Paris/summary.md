# Summary of user feedback 

## Installation

- All users have used conda. 
- Smooth installation process for everybody. (Note some old conda versions)
- Some issues with getting gammapy-datasets: 
  * follow-up from installation to getting started
  * overwrite of older installations
  
## Documentation

### General
- Not enough information for basic users:
  * What are the methods applied? Statistics
    * E.g. significance, ring bkg etc
  * A glossary?
- Improve uniformity of docs
- Overview section is not what is expected for a science tool (not only a python package)
- Need workflow graphic

### Tutorials
- Used by everybody
- Lack of description/information
- They are not as self explanatory as we think
- More structure to improve readibility
  * e.g. core/advanced tutorials sections
  * Note: Once expanded tutorials hide the the rest of menu bar
- Not all links work (for classes and methods)
  *Having to browse from the tutorial is annoying 

### How-tos
- Only one person used them. Most did not see them. -> move them up
- Need more structure

### API doc 
- Used by ~50% of users
- Explicit code examples there not a necessity
- Absence of examples in docstring is regretted by several people

## HLI
- Positive feedback on v0.14->v0.15 improvements
- Lack of documentation on how to write yaml config file. 
 * Comments in yaml files?
 * YAML files for all models? E.g. SkyDiffuseCube
- Try to have more explicit interface:
 * names for parameters (e.g. skydir)
 * Error messages for non-validation sometimes un-readable.
- Can we have a validation for inconsistencies in the config file?
- Working with SkyModels sometimes complex:
 * e.g. appending SkyModel on SkyModels. 
 * Can we make a spatial model as the sum of two spatial models?
- Analysis could handle passing covariance to fluxpointdataset. Note that difference between analysis.fluxpoints and actual fluxpoints has surprised some.
- Issues with defaults: SafeMask & Etrue range.
  
## API

- No strong issues
- For API of similar level, similar type of objects should have similar methods eg to_table for tabular objects, peek, plot when relevant etc

  
## Bugs
  
  
