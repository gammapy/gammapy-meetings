# Gammapy Developer Meeting

* Friday, Apr 24, 2020 at 10 am
* "Gammapy Developer Meeting" on CTA eZuce, no password, [connection details](ezuce.txt)

# Agenda

* [Gammapy pulse from last week](https://github.com/gammapy/gammapy/pulse)
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
* Short report by everyone, what they have worked on during the past week 
* [Issues with `MapDataset.to_image()`](https://github.com/gammapy/gammapy/issues/2865). Decision not to modify the IRFs in true energy and squeeze the `edisp` to have only one bin in `e_reco`. Atreyee will prepare a PR for that.
* [Possible issues with PSF](https://github.com/gammapy/gammapy/issues/2862). In practice, the effects observed with HESS data semme to be due to an incorrect event position stored in the the event files. The issue with CTA 1DC data still remains and is partly due to our conversion to `PSF3D` to compute the average `PSFMap`. We would have a different result if we were to compute the mean PSF at the exact position from the `MultiGaussPSF`. No easy solution there. A least we should ask the IRF team from the ASWG to avoid using functional desciption of the PSF based on parameter interpolation.



