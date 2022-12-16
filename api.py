from fastapi import FastAPI
from uvicorn import run

from kw_router import kw_router

app = FastAPI()
app.include_router(kw_router)


@app.get("/")
def welcome() -> dict:
    response = {
        "message": "Welcome to the Kitchenware Classifier API",
        "author": "Martin Uribe",
        "email": "clamytoe@gmail.com",
        "version": "1.0.0",
        "entrypoint": "/classify_image",
        "repo": "https://github.com/clamytoe/kitchenware_classifier",
        "example": {
            "cli": 'curl -X POST -F "image=@./sample.jpg" http://localhost:8000/classify_image'
        },
    }

    return response


if __name__ == "__main__":
    run(app)
