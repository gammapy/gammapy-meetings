# Telcon on gammapy.maps

* Thursday, Feb 15, 8 pm CEST (that's 10 am US pacific time)
* On CTA eZuce: "gammapy.maps", no password, guests allowed, see [ezuce.txt](ezuce.txt)
* Participants: Matthew Wood, Régis Terrier, Christoph Deil, anyone interested in gammapy.maps

Agenda:

The call will be focused on gammapy.maps, and how to use it from analysis code (see [PIG 2](https://github.com/gammapy/gammapy/pull/1277))

* Maps Serialisation (multiple maps in one FITS file?, HDF5?)
* Docs (need more on map creation and read / write; change all examples to data files that users have)
* Features (anything missing?)
  * Support for more ROI geometries.  For instance adding circular geometries for WCS or rectangular geometries for HPX.  It would also be nice to add support for a MOC geometry to HPX.
  * `cutout` and `paste`.  These should be fairly straightfoward to implement so it's mainly a matter of settling on the best API for these methods.
  * Full support for HPX->WCS and WCS->HPX reprojection.  Currently not supported for all map types (irregular etc.).  
  * Extrapolation for HPX maps.  Extrapolation isn't supported by `healpy` so that might be one motivation for eventually migrating to `astropy-healpix`.
  * Sparse maps.  Originally planned to implement via a custom sparse array class -- however the `sparse` library (https://github.com/pydata/sparse) is now sufficiently advanced that it's probably a better option as it will fully support the full suite of numpy operations.  Ultimately we need to figure out how best to implement the sparse HPX and WCS classes without completely rewriting all of the existing methods in `WcsNDMap` and `HpxNDMap`.  
* Please add here anything you'd like to discuss before the call!
