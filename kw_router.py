from fastai.vision.all import load_learner
from fastapi import APIRouter, File, Request, UploadFile

# Load the exported fastai learner model
model = load_learner("fastai_model.pkl")

kw_router = APIRouter()


@kw_router.post("/classify_image")
async def classify_image(request: Request, image: UploadFile = File(...)):
    # Read the image data and classify it using the fastai model
    img_bytes = await image.read()
    img = model.predict(img_bytes)

    # Return the classification results
    # return {"class": img[0], "confidence": img[1]}
    return {"class": img[0]}
