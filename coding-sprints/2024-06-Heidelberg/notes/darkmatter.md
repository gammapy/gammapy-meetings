# Notes for the DM submodule

@registerrier asked me to contribute some thoughts on where the DM stuff should head, so here we go:

## Overview:

There are two main "functions" of the module:
1. Provide a `DarkMatterAnnihilationSpectralModel` or `DarkMatterDecaySpectralModel`
2. Provide calculation of J-Factors and J-Factor maps using the `JFactory`

## Thoughts

1. The dark matter spectral models are composed of a `PrimaryFlux` instance which calculates the primary flux at the source for a specific annihilation/decay channel, and a J-factor, which itself is a spatial contribution, taking into account the dark matter content of the source. My take here is that, since in a 3d-analysis the J-Factor can be a map, we should introduce a seperate spectral and spatial model for dark matter, alias remove the J-factor from the spectral model and handle this via a skymodel. It's confusing to set the J-Factor to 1 in case of an additional spatial map for it and the quantities don't work out anymore.
2. The `PrimaryFlux` class is based on a `TemplateNDSpectralModel` and reads in the PPPC4DM fluxes from a table located at `"$GAMMAPY_DATA/dark_matter_spectra/AtProduction_gammas.dat"`. There are suitable other DM fluxes that have been used in newer analyses, we should add them to gammapy-data, namingly HDMSpectra `https://github.com/nickrodd/HDMSpectra` and CosmiXs `https://github.com/ajueid/CosmiXs`. I started writing a conversion tool for HDMSpectra, maybe it helps, `https://github.com/StFroese/HDMConverter`.
3. The `JFactory` is really slow, I did some profiling but haven't finished it, feel free to take a look `https://github.com/gammapy/gammapy/pull/4999`.
4. The reason for having a faster `J-Factory` actually comes from the idea of introducing priors to the DM analysis. A typical prior would be the uncertainty of a calculated J-Factor (normally a log10-prior which don't have right now I think), take a look here `https://github.com/gammapy/gammapy/pull/5097`. So why stop there? If we would be able to calculate the J-Factor on demand using the `J-Factory` we could introduce priors on the parameters of the `DMProfile`s.
6. I created a Gammapy DM tutorial for a MAGIC meeting this year, would be worth updating it to use CTA/MAGIC IRFs to produce DL3 data and move it to gammapy docs. (`https://github.com/StFroese/gammapy-dm-tutorial`)
7. This brings me to the next thing, we may want to introduce a new estimator for the calculation of the DM upper limits.

