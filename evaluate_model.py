from typing import Any

import numpy as np
from fastai.vision.all import (
    ImageDataLoaders,
    Interpretation,
    Path,
    load_learner,
    pd,
    set_seed,
)

SEED = 42
set_seed(42)

PROJECT_DIR = Path("kitchenware_classifier")
DATA_DIR = PROJECT_DIR / "data"
IMG_DIR = DATA_DIR / "images"

TRAIN_DF = pd.read_csv(DATA_DIR / "train.csv")
TEST_DF = pd.read_csv(DATA_DIR / "test.csv")
TRAIN_DF["image"] = TRAIN_DF["Id"].map(lambda x: f"{x:0>4}.jpg")
TEST_DF["image"] = TEST_DF["Id"].map(lambda x: f"{IMG_DIR}/{x:0>4}.jpg")

MODEL_FILE = Path("fastai_model.pkl")
EXPORT_FILE = Path("submission.csv")


def evaluate_model(learner: Any):
    learner.show_results()
    interp = Interpretation.from_learner(learner)
    interp.plot_top_losses(9, figsize=(15, 10))


def make_predictions(test_set: pd.Series, learner: Any, dls: ImageDataLoaders) -> Any:
    tst_dl = dls.test_dl(test_set)
    return learner.tta(dl=tst_dl)


def create_submission(tta: Any, dls: ImageDataLoaders):
    tta_preds, _ = tta
    idxs = tta_preds.argmax(dim=1)
    vocab = np.array(dls.vocab)
    sub = pd.read_csv(DATA_DIR / "test.csv")
    sub["label"] = vocab[idxs]
    sub.to_csv(EXPORT_FILE, index=False)
    print(f"Predictions saved to {EXPORT_FILE}.")


def print_summary(learner: Any):
    print(learner.summary())


def main():
    print("Loading learner...")
    learner = load_learner(MODEL_FILE, cpu=False)
    dls = learner.dls
    # print("Evaluating model...")
    # evaluate_model(learner)
    print("Performing Test Time Augmentation...")
    tta = make_predictions(TEST_DF.image, learner, dls)
    print("Generating prediction submission...")
    create_submission(tta, dls)
    print("Model Summary:")
    print_summary(learner)


if __name__ == "__main__":
    main()
