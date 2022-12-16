from pathlib import Path

from fastai.vision.all import load_learner

model_file = Path("fastai_model.pkl")
learner = load_learner(model_file, cpu=False)
pred = learner.predict("kitchenware_classifier/data/images/0001.jpg")
pred = learner.predict("kitchenware_classifier/data/images/0002.jpg")
print(pred)
