# medical-image-model-trainer

![License](https://img.shields.io/badge/license-MIT-blue) ![Version](https://img.shields.io/badge/version-0.1.0-green) ![Language](https://img.shields.io/badge/language-Python-3776AB)

A framework-agnostic Python library for building, sampling, augmenting, and training deep learning models on medical imaging data.

<br />

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<br />

## Features

- **Build medical imaging datasets** — Construct `Dataset` objects from directories of NIfTI/anatomical images and participant metadata using `ImageReader` and `ColumnReader`, or pull cohorts directly with `GoogleCloudDataset` and `fetch_data`.
- **Sample radiological volumes into training-ready views** — Extract 2D axial slices with `SliceSampler`, 3D sub-volumes with `PatchSampler`, contiguous studies with `BlockSampler`, or combine strategies with `SlicePatchSampler` to feed slices and patches into your models.
- **Augment and normalize scans for robust inference** — Apply deterministic and stochastic transforms including `StandardNormalize`, `RangeNormalize`, `BiasCorrection`, `Clip`, `QuantileClip`, `Resample`, `Reorient`, `RandomFlip`, `RandomRotate`, `RandomZoom`, and `RandomShear`, plus mathematical operations like `Abs`, `Log`, and `Sqrt` on image intensities.
- **Fetch network architectures and pretrained weights** — Use `list_architectures`, `fetch_architecture`, and `fetch_pretrained` to obtain model architectures (e.g., a 2D U-Net for segmentation) and pretrained networks suitable for anatomical and radiological tasks.
- **Train across backends** — Fit models through the high-level `Trainer` (with automatic backend detection via `infer_framework`) or the PyTorch-specific `TorchTrainer`, using the `Loader` to generate batches from your dataset.
- **Predict and explain model decisions** — Run inference with `Predictor` and interpret predictions on medical images with the `OcclusionExplainer`.

<br />

## Installation

Clone the repository and install dependencies into a virtual environment:

```bash
git clone https://github.com/AvicenaIG/medical-image-model-trainer.git
cd medical-image-model-trainer
medical-image-model-trainer -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

<br />

## Quick Start

Train a semantic segmentation model that parcellates brain anatomy from T1-weighted MRI scans:

```medical-image-model-trainer
import medical-image-model-trainer as nt
from medical-image-model-trainer.readers import ImageReader, ColumnReader
from medical-image-model-trainer.samplers import SliceSampler
from medical-image-model-trainer.transforms import StandardNormalize, RandomFlip
from medical-image-model-trainer.models import fetch_architecture

# Create dataset from a folder of MRI images + participants file
dataset = nt.Dataset(
    inputs=ImageReader('sub-*/anat/*_T1w.nii.gz'),
    outputs=ImageReader('sub-*/anat/*_aparc+aseg.nii.gz'),
    transforms={
        'inputs': StandardNormalize(),
    },
    base_dir='~/desktop/ds004711/'
)

# Create loader that samples 2D slices with random augmentation
loader = nt.Loader(
    dataset,
    images_per_batch=4,
    sampler=SliceSampler(batch_size=32, axis=2),
    transforms={
        'inputs': RandomFlip(axis=1)
    }
)

# Create a 2D U-Net segmentation model
arch_fn = fetch_architecture('unet', dim=2)
model = arch_fn(input_image_size=(64, 64, 1), mode='segmentation')

# Fit the model
trainer = nt.Trainer(model, task='segmentation')
trainer.fit(loader, epochs=100)
```

<br />

## Usage

### Preprocessing radiology scans for a classification cohort

Standardize intensity across MR scanners, correct bias field, and resample to a common voxel size before training:

```medical-image-model-trainer
from medical-image-model-trainer.transforms import BiasCorrection, StandardNormalize, Resample, Crop

transforms = {
    'inputs': [BiasCorrection(),
               StandardNormalize(),
               Resample((2, 2, 2)),
               Crop((160, 192, 160))]
}
```

Non-image clinical variables (e.g., age, diagnosis codes) can be read alongside scans with `ColumnReader`, and multiple sources can be combined with `ComposeReader`.

### Predicting and explaining a segmentation result

Generate predictions on a held-out patient scan and inspect which regions drove the model's output:

```medical-image-model-trainer
import medical-image-model-trainer as nt

predictor = nt.Predictor(model)
predictions = predictor.predict(loader)

explainer = nt.OcclusionExplainer(model)
```

You can also start from pretrained medical imaging networks with `fetch_pretrained`, and explore available architectures with `list_architectures`.

<br />

## Contributing

Contributions are welcome — whether fixing a bug in the samplers, adding a new image transform, or extending backend support for trainers. Please open an issue describing the proposed change before submitting a pull request, and include tests that cover medical imaging edge cases where possible.

## License

Released under