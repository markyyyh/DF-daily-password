import requests
from bs4 import BeautifulSoup

url = "https://www.playdeltaforce.com/events/hq/en/m/index.html"

html = requests.get(url).text

print("HTML長度:", len(html))

soup = BeautifulSoup(html, "html.parser")


# 找所有 button
print("\n=== BUTTON ===")
for b in soup.find_all("button"):
    print(b)
    

# 找所有可能按鈕 class
print("\n=== CLASS含btn/button ===")
for tag in soup.find_all(True):
    cls = tag.get("class")

    if cls:
        text = " ".join(cls).lower()

        if "btn" in text or "button" in text:
            print(tag.name, cls, tag.text.strip())


# 找所有包含密碼相關字的附近
print("\n=== password附近 ===")

for word in ["password", "code", "operations-zero-dam"]:

    index = html.lower().find(word.lower())

    print("\n搜尋:", word)

    if index != -1:
        print(html[index-300:index+500])
    else:
        print("沒有")