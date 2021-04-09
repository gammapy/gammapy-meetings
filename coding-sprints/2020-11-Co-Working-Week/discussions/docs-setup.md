# Discussion notes docs setup
Wednesday Nov 25th., 10h00

## Overview
See [slides](../slides/documentation.pdf) by José Enrique.

## Notes
- Find a place where to store static images..?
- Versioned releases: keep (binder links, html docs) and remove ((datasets, tutorials)
- Remove gammapy download notebooks and gammapy download scripts
- Keep links to nobtebooks and scripts for each notebook at the top of the html pages
- Display the collection of tutorials as a gallery and re-structure groups?
- Improve [speed execution](nbs_exectime.txt) of some notebooks 
- Execute python code found in RST pages?
- Problems found diffing nbs with widgets?
- Other options for the setup (jupytext)
- Improve /automatize release process?
- Maintenance: broken links and sphinx builds

## Action items
- Simplify notebook, tutorials and scripts download: remove index files and use a single tar file
- Move API tutorials to the corresponding sub-packages and build "in place" (resolve content duplication between tutorials / RST )
- Introduce Gallery for tutorials
