#!/usr/bin/env python
# coding: utf-8
# Kitchenware Classifier

from fastai.vision.all import (
    EarlyStoppingCallback,
    ImageDataLoaders,
    Path,
    Resize,
    SaveModelCallback,
    accuracy,
    aug_transforms,
    error_rate,
    minimum,
    pd,
    set_seed,
    slide,
    steep,
    valley,
    vision_learner,
)
from torch import device

# Model to use
MODEL = "convnext_nano"
MODEL_FILE = "fastai_model.pkl"

# Load data and set variables
SEED = 42
set_seed(42)

PROJECT_DIR = Path("kitchenware_classifier")
DATA_DIR = PROJECT_DIR / "data"
IMG_DIR = DATA_DIR / "images"

TRAIN_DF = pd.read_csv(DATA_DIR / "train.csv")
TEST_DF = pd.read_csv(DATA_DIR / "test.csv")
EXTRA_DF = pd.read_csv(DATA_DIR / "extra.csv")
TRAIN_DF = pd.concat([TRAIN_DF, EXTRA_DF], ignore_index=True)
TRAIN_DF["image"] = TRAIN_DF["Id"].map(lambda x: f"{x:0>4}.jpg")
TEST_DF["image"] = TEST_DF["Id"].map(lambda x: f"{IMG_DIR}/{x:0>4}.jpg")

# Data Augmentations
tfms = aug_transforms(
    min_zoom=1.0,
    max_zoom=1.1,
    max_lighting=0.2,
    max_warp=0.2,
    p_affine=0.75,
    p_lighting=0.75,
    size=224,
)

# Build data loaders
dls = ImageDataLoaders.from_df(
    TRAIN_DF,
    path=str(IMG_DIR),
    valid_pct=0.2,
    seed=42,
    bs=8,
    val_bs=8,
    fn_col="image",  # type: ignore
    shuffle=True,
    label_col="label",  # type: ignore
    item_tfms=Resize(460),
    batch_ftms=list(tfms),
    device=device("cuda"),
)
# dls.show_batch()

# Build learner
learn = vision_learner(
    dls,
    MODEL,
    metrics=[error_rate, accuracy],
    path=".",
)
keep_path = learn.path
learn.path = DATA_DIR  # type: ignore

print("Finding best learning rate...")
lrs = learn.lr_find(suggest_funcs=(minimum, steep, valley, slide))
print(f"{lrs=}")

save_best = SaveModelCallback(
    monitor="valid_loss",
    min_delta=0.000001,
    fname="best_model",
)
early_stop = EarlyStoppingCallback(
    monitor="valid_loss",
    min_delta=0.000001,
    patience=3,
)

print("Training the Model...")
learn.fit(10, lrs.valley, cbs=[save_best, early_stop])
learn.path = keep_path  # type: ignore

print("Model validation:", learn.validate())

# Save the model
print(f"Saving model as: {MODEL_FILE}...")
learn.export(MODEL_FILE)

print("Training completed!")
print(learn.summary())
