import requests

URL = "https://www.playdeltaforce.com/events/hq/zh-tw/m/index.html"

response = requests.get(URL)
response.encoding = "utf-8"

html = response.text


for word in ["password", "code", "零號大壩"]:

    print("\n==========", word, "==========")

    index = html.find(word)

    if index != -1:
        print(html[index-500:index+500])
    else:
        print("找不到")
