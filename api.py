from fastapi import FastAPI
from fastapi.responses import FileResponse
from uvicorn import run

from kw_router import kw_router

app = FastAPI()
app.include_router(kw_router)
favicon_path = "favicon.ico"


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


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


if __name__ == "__main__":
    run(app)
