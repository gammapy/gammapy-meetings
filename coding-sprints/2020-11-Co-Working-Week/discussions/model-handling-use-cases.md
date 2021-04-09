# Model handling


```python
dataset = MapDataset()

sky_model = SkyModel()
bkg_model = FoVBackgroundModel(dataset_name=dataset.name)

models = Models([sky_model, bkg_model])
dataset.models = models
```

## Use case 1: making cutouts


```python
dataset_cutout = dataset.cutout(**cutout_kwargs, name="cutout")

bkg_model_cutout = FoVBackgroundModel(dataset_name=dataset_cutout.name)

# throw away components outside
region = dataset_cutout.counts.geom.footprint
models = sky_models.select_region(region=region)

# or just freeze to account for possible leakage?
models_outside = sky_models.select_region(region=region, inside=False)
models_outside.parameters.freeze_all()

dataset_cutout.models = models + bkg_model_cutout
```

## Use case 2: to spectral dataset

One has a 3D dataset including multiple sources in the FoV and now a spectral analysis should be performed:


```python
dataset_spectrum = dataset.to_spectrum_dataset(region=region)

# if the background was pre-optmized, we re-assign it
dataset_spectrum.background = dataset.npred_background().get_spectrum(region=region)

# scenario 1, accounting for containment an contamination
models_spec = models.select(tag="sky-model")
models_spec.parameters.freeze_all()
models_spec["my-source"].parameters.unfreeze(type="spectral")

# scenario 2, classical 1d analysis
model = models["my-source"]
model.spatial_model = None
dataset_spectrum.models = [model]
```

## Use case 3: to image


```python
dataset_image = dataset.to_image(name="dataset-image")

bkg_model = FoVBackgroundModel(dataset_name=dataset_image.name)
bkg_model.spectral_model.tilt.frozen = True

# freeze spectral parameters
models = models.select(tag="sky-model")
models.parameters.freeze(type="spectral")
models.parameters.unfreeze(name="amplitude")

dataset_new.models = models + bkg_model
```

## Some proposed methods for model management


```python
models = Models()

# re-asigne models to a new dataset?
models.reassign(dataset_name, dataset_name_new)

# select sky region
models.select_region(region=, inside=True)

# select mask
models.select_mask(mask=)

# convert to template model
models.to_template_spatial_model(geom=geom)
model.to_template_spectral(geom, psf=psf, region)

# support array indices
models[["model-1", "model-2"]]
models.select(names=)

# freezing and un-freezing 
models.parameters.freeze(type="spectral", name="amplitude")
models.parameters.unfreeze(type="spectral", name="amplitude")

models.parameters.unfreeze_all()
models.parameters.select(type="spectral", name=, name_substring=,)

# probably we should add
source_catalog.to_models()
models = Models([row.sky_model() for row in source_catalog])

# one could "mirror" the API of the datasets
models.cutout()
models.to_image()
models.to_spectrum()

# however one would probably choose different method names...

```


```python
# in general a good srategy we should recommand to users
# is keeping the sky models and background models separate for joint analyses

sky_models = Models([sky_model_1, sky_model_2])
bkg_models = Models([FoVBackgroundModel(d.name) for d in datasets])

models = sky_model + bkg_models
```
