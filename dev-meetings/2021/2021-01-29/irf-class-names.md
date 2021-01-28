# IRF class naming scheme

With the changes introduced in https://github.com/gammapy/gammapy/pull/3185, the IRF classes are agnostic of any dimensionality.

A suffix like 1D, 2D or 3D I think is non-ideal, as it not necessarily unique, except if combined with information on the FoV coordinate system, such as offset / phi vs. lon-fov, lat fov.

One could try to reflect this in the name using, e.g. `RadialBackground2D` or `FoVBackground3D` ,  but this might lead to a proliferation of classes, so maybe completely give up the distinction by dimensionality as we do for maps.

## Option 1

- IRF (base class)
- PointSpreadFunctionIRF (base class)
- ParametricPointSpreadFunctionIRF (base class)
- MultiGaussPointSpreadFunctionIRF
- KingPointSpreadFunctionIRF
- EnergyDispersionIRF
- BackgroundIRF
- EffectiveAreaIRF


What to do about existing classes?
- PSFMap -> PointSpreadFunctionMap?
- PSFKernel -> PointSpreadFunctionKernel?
- EDispMap -> EnergyDispersionMap?
- EDispKernel -> EnergyDispersionKernel?

Or just keep?


## Option 2

Existing classes:
- PSFMap
- PSFKernel
- EDispMap
- EDispKernelMap
- EDispKernel

Introduce: 
- PSFIrf?
- EDispIrf
- EAreaIrf
- BkgIrf?

I think this becomes very cryptic, especially if all upper-case like PSFIRF or BKGIRF...

