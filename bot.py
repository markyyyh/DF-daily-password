import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE = "https://www.playdeltaforce.com/events/hq/en/m/index.html"

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0"
}


print("========== HTML ==========")

html = session.get(BASE, headers=headers).text

print("HTML長度:", len(html))


soup = BeautifulSoup(html, "html.parser")


# ----------------------------
# 找 data-info
# ----------------------------

print("\n========== DATA INFO ==========")

for tag in soup.find_all(True):

    info = tag.get("data-info")

    if info and "operation" in info:
        print(
            tag.name,
            info,
            "=>",
            tag.text.strip()
        )


# ----------------------------
# 找圖片
# ----------------------------

print("\n========== IMAGES ==========")

for img in soup.find_all("img"):

    src = img.get("src")

    if src:

        if any(x in src.lower() for x in [
            "password",
            "guide",
            "step",
            "map"
        ]):
            print(src)


# ----------------------------
# 找 onclick
# ----------------------------

print("\n========== CLICK EVENTS ==========")

for tag in soup.find_all(True):

    for key,value in tag.attrs.items():

        if "click" in key.lower():

            print(
                tag.name,
                key,
                value
            )


# ----------------------------
# 找所有 JS
# ----------------------------

print("\n========== JS FILES ==========")

scripts=[]

for script in soup.find_all("script"):

    src=script.get("src")

    if src:

        scripts.append(urljoin(BASE,src))


print("JS數量:",len(scripts))


# ----------------------------
# 搜尋 JS
# ----------------------------

keywords=[
    "operations-zero-dam",
    "data-info",
    "password-list",
    "password",
    "innerHTML",
    ".text(",
    "setData",
    "ajax",
    "fetch",
    "XMLHttpRequest",
    "axios"
]


for js_url in scripts:

    try:

        js=session.get(js_url,headers=headers).text

    except:

        continue


    print("\n================")
    print(js_url)
    print("長度:",len(js))


    for word in keywords:

        if word in js:

            print("找到:",word)

            index=js.find(word)

            print(
                js[index-200:index+500]
            )