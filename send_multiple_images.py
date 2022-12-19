import os
from glob import glob

import requests

# returns a list of file paths
paths = glob("sample*.jpg", recursive=True)
url = "http://127.0.0.1:8000/classify_image"

results = []
for idx, path_img in enumerate(paths):
    with open(path_img, "rb") as img:
        name_img = os.path.basename(path_img)
        file = {"image": (name_img, img, "multipart/form-data", {"Expires": "0"})}
        with requests.Session() as s:
            r = s.post(url, files=file).json()
            results.append({"image": paths[idx], **r})

print(results)
