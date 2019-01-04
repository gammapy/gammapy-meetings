# Gammapy Dev Telcon

* Friday, December 14, 2018 at 10 am
* CTA eZuce, no password.  The connection details are [here](../2018-10-12/ezuce.txt)

# Agenda

* [Gammapy pulse from last week](https://github.com/gammapy/gammapy/pulse)
* [Open pull requests]():
* Report from the SUSS meeting in Bologna - [PDF](2018-12-07_CTA_SUSS_REQ_Gammapy_Summary.pdf) (Christoph)
* Report from the ctapipe developer meeting in Dortmund (Axel)
* Astropy 3.1 is out (see [here](http://docs.astropy.org/en/stable/whatsnew/3.1.html)).
  * Currently we support Astropy 2.0 or later in Gammapy.
    But that's not set in stone, can be useful to look at newer things in Astropy either to use directly in the future, or as examples how to do something.
  * [Commmon API for WCS](http://docs.astropy.org/en/stable/whatsnew/3.1.html#common-api-for-world-coordinate-systems) - how does it compare to Gammapy map geom? Might be useful example concerning quantity and time handling for extra axes.
  * `Time` improved and specifically `Time` as table column - not sure if this is useful for us, we currently don't store Time objects in tables, only `float` columns.
  * SkyCoord offset coordinates could be used for field of view coordinates.
