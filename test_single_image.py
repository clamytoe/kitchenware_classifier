import os

import requests

url = "http://127.0.0.1:8000/classify_image"
path_img = "sample.jpg"

with open(path_img, "rb") as img:
    name_img = os.path.basename(path_img)
    file = {"image": (name_img, img, "multipart/form-data", {"Expires": "0"})}
    with requests.Session() as s:
        r = s.post(url, files=file)
        print(r.json())
