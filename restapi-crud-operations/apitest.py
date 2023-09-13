#!/usr/bin/python3

import requests

r = requests.post(
    "http://127.0.0.1:8000/api/",
    data={"name": "basil"},
)
response = requests.get("http://127.0.0.1:8000/api/")

print(response.json())
print(r.json())
print(r.headers["content-type"])
