import requests

js_url = "https://www.playdeltaforce.com/events/hq/m/js/index.js?v=1.5"

js = requests.get(js_url).text

print("JS長度:", len(js))


for word in [
    "operations-zero-dam",
    "password",
    "每日密码",
    "password-box",
    "layali"
]:
    print("\n搜尋:", word)

    index = js.find(word)

    if index != -1:
        print(js[index-300:index+500])
    else:
        print("沒有")
