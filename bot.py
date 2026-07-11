import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


URL = "https://www.playdeltaforce.com/events/hq/en/m/index.html?t=" + str(int(time.time()))

html = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text


soup = BeautifulSoup(html, "html.parser")


for script in soup.find_all("script"):

    src = script.get("src")

    if src:

        js_url = urljoin(URL, src)

        print("\nJS:", js_url)

        js = requests.get(
            js_url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        ).text


        for word in [
            "operations-zero-dam",
            "setData",
            "data-info",
            "ajax",
            "get"
        ]:

            if word in js:
                print("找到:", word)