# Gammapy Dev Telcon

* Friday, October 19, 2018 at 10 am
* CTA eZuce, no password.  The connection details are [here](../2018-10-12/ezuce.txt)

# Agenda

* [Gammapy pulse from last week](https://github.com/gammapy/gammapy/pulse)
* [Open pull requests](https://github.com/gammapy/gammapy/pulls)
* [PIG 6](https://github.com/gammapy/gammapy/pull/1877)
    * scenarios discussed in PIG to introduce new use cases without modifications for the user
    * Observations class will be introduced in the coming week
    * how to deal with ObservationFilter in general?
    * first introduce time interval selection
* [Infinites, NaNs and model parameter bounds](https://github.com/gammapy/gammapy/pull/1881)
    * option to use `numpy.nan_to_num` might not be relevant.
    * user defined min and max values for now to protect for `nan`in fits see PR[#1882](https://github.com/gammapy/gammapy/issues/1842). Beware of scaling effects though.
    * better handling of `Parameter` min and max to be cleanly handled in [Modeling](https://github.com/gammapy/gammapy/projects/7).   
    * stall PR and wait for @adonath.
* Dealing with parameter covariance. See [Parameters class](https://docs.gammapy.org/0.8/api/gammapy.utils.fitting.Parameters.html) and [multinormal distributions](https://multinorm.readthedocs.io/)
    * see also issue [#1883](https://github.com/gammapy/gammapy/issues/1883)
    * where to store covariance (`Fit` or `Parameters`?). 
    * what about likelihood profiles for non symmetric errors? Valid parameter range and CL definition has to be foreseen too.
* Closing issue [#1842](https://github.com/gammapy/gammapy/issues/1842). 
    * background norm is found to be consistently within 2% after addition of `ScaledRegularGridInterpolator`
