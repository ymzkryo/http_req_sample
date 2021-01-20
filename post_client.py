# coding: utf-8
import requests

url = 'http://localhost:8765'

test1 = {
    "color1": "赤",
    "color2": "黄"
}

response = requests.post(url, test1)
print(response.text)
