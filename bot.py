import requests

url = "https://www.playdeltaforce.com/events/hq/assets/m/index.html-BT5wd2G1.js"

js = requests.get(url).text

for word in [
    "2119",
    "6905",
    "fetch",
    "axios",
    ".json",
    "api",
    "operations-zero-dam"
]:
    print("\n搜尋:", word)

    i = js.find(word)

    if i != -1:
        print(js[i-300:i+500])
    else:
        print("沒有")