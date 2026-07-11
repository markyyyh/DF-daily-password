import requests

url = "https://www.playdeltaforce.com/events/hq/assets/m/index.html-BT5wd2G1.js"

js = requests.get(url).text

print(js)

print("\n長度:", len(js))