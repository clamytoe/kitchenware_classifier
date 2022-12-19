from pathlib import Path

import numpy as np
from fastai.vision.all import load_learner, pd

PROJECT_DIR = Path("kitchenware_classifier")
DATA_DIR = PROJECT_DIR / "data"
TEST_FILE = DATA_DIR / "test.csv"
TEST_DF = pd.read_csv(TEST_FILE)
IMG_DIR = DATA_DIR / "images"
TEST_DF["image"] = TEST_DF["Id"].map(lambda x: f"{IMG_DIR}/{x:0>4}.jpg")
MODEL_FILE = "fastai_model.pkl"
OUTPUT_FILE = "submission.csv"


def process_images(df, model):
    learn = load_learner(model)
    dls = learn.dls
    tst_dl = dls.test_dl(df.image)
    return learn.tta(dl=tst_dl), dls


def generate_submission(tta, dls):
    tta_preds, _ = tta
    idxs = tta_preds.argmax(dim=1)
    vocab = np.array(dls.vocab)
    sub = pd.read_csv(TEST_FILE)
    sub["label"] = vocab[idxs]
    sub.to_csv(OUTPUT_FILE, index=False)
    return sub


def main():
    tta, dls = process_images(TEST_DF, MODEL_FILE)
    sub = generate_submission(tta, dls)
    print(sub.head())


if __name__ == "__main__":
    main()
