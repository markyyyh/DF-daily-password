import requests


base = "https://www.playdeltaforce.com/events/hq/assets/m/"


files = [
    "wand-Dnsle5-v.js",
    "main-DYD4Ogaa.js",
    "keywords-BY-fuJl3.js",
    "convert-DkzLyfDU.js",
    "timeServerPlugin-6YcmO4yg.js"
]


words = [
    "6905",
    "2119",
    "operations-zero-dam",
    "password",
    "daily",
    "api",
    "fetch",
    "axios",
    "request"
]


for file in files:

    url = base + file

    js = requests.get(url).text

    print("\n================")
    print(file)
    print("長度:", len(js))


    for word in words:

        if word.lower() in js.lower():

            print("找到:", word)

            i = js.lower().find(word.lower())

            print(js[i-300:i+500])