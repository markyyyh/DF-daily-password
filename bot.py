import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


URL = "https://www.playdeltaforce.com/events/hq/en/m/index.html"


html = requests.get(URL).text

soup = BeautifulSoup(html, "html.parser")


scripts = []

for script in soup.find_all("script"):

    src = script.get("src")

    if src:
        scripts.append(urljoin(URL, src))


print("JS 數量:", len(scripts))


keywords = [
    "operations",
    "password",
    "6905",
    "2119",
    "daily",
    "code",
    "fetch",
    "ajax",
    "xmlhttprequest"
]


for js_url in scripts:

    try:
        js = requests.get(js_url).text

        print("\n==========")
        print(js_url)
        print("長度:", len(js))


        for word in keywords:

            if word.lower() in js.lower():

                print("找到:", word)

                index = js.lower().find(word.lower())

                print(
                    js[index-200:index+500]
                )

    except Exception as e:

        print("錯誤:", e)