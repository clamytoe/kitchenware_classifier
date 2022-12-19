import os

import requests

url = {
    "local": "http://127.0.0.1:8000/classify_image",
    "cloud": "https://kitchenware-cl-prod-kitchenware-classifier-7f8cze.mo1.mogenius.io/classify_image",
}
path_img = "sample.jpg"

with open(path_img, "rb") as img:
    name_img = os.path.basename(path_img)
    file = {"image": (name_img, img, "multipart/form-data", {"Expires": "0"})}
    with requests.Session() as s:
        r = s.post(url["local"], files=file)
        print(r.json())
