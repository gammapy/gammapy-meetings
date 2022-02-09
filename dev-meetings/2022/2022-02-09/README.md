# Meeting on the Gammapy internal DL3 data model

* Wednesday, February 9st, 2022 at 6 pm (CET)
* "Gammapy Developer Meeting" on Zoom (direct link on Slack)

# Context and objectives

* Gammapy internal data model is still too closely connected to the gadf v0.2 data format
  - the `EventList` is currently a table formatted according to gadf and relying on its header keywords
  - `GTI` is directly a table formatted according to gadf (time columns as quantity) and following its header definition (reference time definition)  
  - the `DataStore` relies on the two tables `obs_index` and `hdu_index` defined by gadf as data members.
  - `IRF` now have a cleaner implementation. I/O? 
* CTAO data model is being prepared and new format definitions will be proposed in the coming months
* Gammapy v1.0 is to be released in the coming months (before next CTA meeting) and as it will serve as long term stable release, it should be able to support the new CTA format.

## Related issues

* [Separate internal data model from specific serialization formats](https://github.com/gammapy/gammapy/issues/3767)
* [Read information from EVENTS header when not present in OBS_INDEX](https://github.com/gammapy/gammapy/issues/3724)
  - associated PR: [Merge obs_info from obs index with EVENTS Header](https://github.com/gammapy/gammapy/pull/3742)



 


