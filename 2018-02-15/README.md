# Telcon on gammapy.maps

* Thursday, Feb 15, 8 pm CEST (that's 10 am US pacific time)
* On CTA eZuce: "gammapy.maps", no password, guests allowed, see [ezuce.txt](ezuce.txt)
* Participants: Matthew Wood, Régis Terrier, Christoph Deil, anyone interested in gammapy.maps

Agenda:

The call will be focused on gammapy.maps, and how to use it from analysis code (see [PIG 2](https://github.com/gammapy/gammapy/pull/1277))

* Map dimensions and coordinates
  * Currently gammapy.maps has a tuple-based interface for coordinates.
    How does the special support for Quantity / Angle / SkyCoord work?
    Is there special broadcasting behaviour for sky coordinates?
    Change to or add name-based coordinates like xarray, that avoid `axis[2]` and `np.newaxis` in a lot of code using maps,
    i.e. more generic analysis code that can really deal with arbitrary new axes?
    What about FOV coordinates and time?
    Re-usable for IRFs that don't have sky coordinate axes?
  * Currently IRF coordinates are separate and badly implemented in Gammapy
    Ideally we would share map and IRF coordinate handling, or if not feasible we should implement them in a similar way.
    See https://github.com/gammapy/gammapy/issues/1308#issuecomment-365885058 for what we have for IRF,
    and links to what others have implemented (xarray, name based, allows arbitrary order of data dimensions) and think (Astropy generic WCS API, tuple index based, not implemented).
  * Example notebook of current and expected usages  : https://github.com/gammapy-meetings/2018-02-15/nddata_interpolation.ipynb 
  * Take a decision on special coordinate and axis names in Gammapy: https://github.com/gammapy/gammapy/pull/1295
* Maps Serialisation (multiple maps in one FITS file?, HDF5?)
  * HDF5 support could be added via `to_h5group` methods.  Initially this could call through to `to_hdulist` and some method to automatically convert FITS to HDF5 but eventually these could be rewritten to take greater advantage of the HDF5 feature set.  The hierarchical stucture of HDF5 would be convenient in many ways e.g. it would provide a more natural mechansism for grouping the map and BANDS HDUs together.  We'd also need to think carefully about how this changes the format specs. 
* Docs (need more on map creation and read / write; change all examples to data files that users have)
* Features (anything missing?)
  * Support for more ROI geometries.  For instance adding circular geometries for WCS or rectangular geometries for HPX.  It would also be nice to add support for a MOC geometry to HPX.  Ultimately it would be good to have some unified mechanism for defining the geometry footprint via a region object that could be passed to factory methods or constructors.
  * `cutout` and `paste`.  These should be fairly straightfoward to implement so it's mainly a matter of settling on the best API for these methods.
  * Full support for HPX->WCS and WCS->HPX reprojection.  Currently not supported for all map types (irregular etc.).  
  * Extrapolation for HPX maps.  Extrapolation isn't supported by `healpy` so that might be one motivation for eventually migrating to `astropy-healpix`.
  * Sparse maps.  Originally planned to implement via a custom sparse array class -- however the `sparse` library (https://github.com/pydata/sparse) is now sufficiently advanced that it's probably a better option as it will fully support the full suite of numpy operations.  Ultimately we need to figure out how best to implement the sparse HPX and WCS classes without completely rewriting all of the existing methods in `WcsNDMap` and `HpxNDMap`.  `HpxGeom` also needs some refactoring to support sparse maps as it presently stores an explicit list of pixel indices (which defeats the objective of a sparse map).
* Please add here anything you'd like to discuss before the call!
