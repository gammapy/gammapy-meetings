# Gammapy Maps

- Christoph Deil
- Nov 18, 2019
- Gammapy coding sprint in Granda

## Overview

- tbd
- [gammapy.maps project board](https://github.com/gammapy/gammapy/projects/2)

## High priority work (2019)

- Improve energy axis and grid handling (remove `scale` helper functions in utils, [GH 2271](https://github.com/gammapy/gammapy/issues/2271))
- Improve MapCoord unit, frame, skycoord, time handling (unclear how exactly and what can be achieved)
- Avoid interpolate float precision warning ([GH 2431](https://github.com/gammapy/gammapy/issues/2431))
- Remove int N/A map code, just use float also for counts maps (try it)
- Remove unused sparse maps code for now [GH 1332](https://github.com/gammapy/gammapy/issues/1332) (Christoph)
- Remove or improve reproject code? [GH 2549](https://github.com/gammapy/gammapy/issues/2549) (Axel, maybe)

Relevant issues:

- Maps API uses unintuive and unnecessary abbreviations ([GH 2286](https://github.com/gammapy/gammapy/issues/2286))
- Unify coordsys and frame handling between maps and models [GH 2437](https://github.com/gammapy/gammapy/issues/2437)
- How to handle invalid integer indices in gammapy.maps? ([GH 1440](https://github.com/gammapy/gammapy/issues/1440))
- Float and int data types in gammapy.maps ([GH 1350](https://github.com/gammapy/gammapy/issues/1350))
- Add min / max edges attributes to MapAxis? [GH 2134](https://github.com/gammapy/gammapy/issues/2134)

## Low priority work (2020)

- Re-add sparse maps to use pydata/sparse [GH 1332](https://github.com/gammapy/gammapy/issues/1332)

## Discussion

- Issues, solutions, tasks, priorities, contributors?
