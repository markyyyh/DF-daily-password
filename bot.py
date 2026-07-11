import requests


URL = "https://www.playdeltaforce.com/events/hq/en/m/index.html"


html = requests.get(URL).text


print("HTML長度:", len(html))


for word in [
    "2119",
    "6905",
    "operations-zero-dam",
    "operations-layali-grove",
    "Daily Password",
    "password"
]:

    print("\n搜尋:", word)

    i = html.find(word)

    if i != -1:
        print(html[i-300:i+500])
    else:
        print("沒有")