import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime


URL = "https://www.playdeltaforce.com/events/hq/zh-tw/m/index.html"

WEBHOOK = os.getenv("DISCORD_WEBHOOK")


def get_password(soup, info):
    data = soup.find("span", {"data-info": info})

    if data and data.text.strip():
        return data.text.strip()

    return "暫無"


# 抓網頁
headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(URL, headers=headers).text

print("HTML長度:", len(html))


soup = BeautifulSoup(html, "html.parser")


# 取得密碼
passwords = {
    "零號大壩": get_password(soup, "operations-zero-dam"),
    "長弓溪谷": get_password(soup, "operations-layali-grove"),
    "巴克什": get_password(soup, "operations-layali-brakkesh"),
    "航天基地": get_password(soup, "operations-layali-space-city"),
    "潮汐監獄": get_password(soup, "operations-layali-tide-prison"),
    "AZ3": get_password(soup, "operations-layali-az3"),
}


print("=== PASSWORD ===")

for k, v in passwords.items():
    print(k, "=>", v)



today = datetime.now().strftime("%Y-%m-%d")


message = f"""△Daily password

日期：{today}

零號大壩：{passwords["零號大壩"]}
長弓溪谷：{passwords["長弓溪谷"]}
巴克什：{passwords["巴克什"]}
航天基地：{passwords["航天基地"]}
潮汐監獄：{passwords["潮汐監獄"]}
AZ3：{passwords["AZ3"]}

Hope every1 got red until u rest in peace"""


print(message)



# 傳 Discord
if WEBHOOK:

    response = requests.post(
        WEBHOOK,
        json={
            "content": message
        }
    )

    print("Discord:", response.status_code)

else:
    print("沒有找到 DISCORD_WEBHOOK")