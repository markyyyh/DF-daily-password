import requests

URL = "https://www.playdeltaforce.com/events/hq/zh-tw/m/index.html"

response = requests.get(URL)

response.encoding = "utf-8"

html = response.text


print("HTML 長度：", len(html))

# 找可能存資料的位置
for word in [
    "0213",
    "0911",
    "零號大壩",
    "password",
    "passwords",
    "code",
    "api"
]:
    print("\n搜尋：", word)

    if word in html:
        print("找到！")
    else:
        print("沒有")
