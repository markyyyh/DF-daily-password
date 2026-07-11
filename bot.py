import os
import time
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


URL = "https://www.playdeltaforce.com/events/hq/zh-tw/m/index.html"

WEBHOOK = os.getenv("DISCORD_WEBHOOK")


# Selenium 設定
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")


driver = webdriver.Chrome(options=options)


print("開啟網頁...")

driver.get(URL)


# 等 JS 載入
time.sleep(5)


html = driver.page_source


driver.quit()


print("HTML長度:", len(html))


soup = BeautifulSoup(html, "html.parser")



def get_password(info):

    data = soup.find(
        "span",
        {
            "data-info": info
        }
    )

    if data:

        value = data.text.strip()

        if value:
            return value


    return "暫無"



passwords = {

    "零號大壩":
        get_password("operations-zero-dam"),

    "長弓溪谷":
        get_password("operations-layali-grove"),

    "巴克什":
        get_password("operations-layali-brakkesh"),

    "航天基地":
        get_password("operations-layali-space-city"),

    "潮汐監獄":
        get_password("operations-layali-tide-prison"),

    "AZ3":
        get_password("operations-layali-az3")

}



print("=== PASSWORD ===")

for name, code in passwords.items():

    print(
        name,
        "=>",
        code
    )



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



if WEBHOOK:

    r = requests.post(
        WEBHOOK,
        json={
            "content": message
        }
    )

    print(
        "Discord:",
        r.status_code
    )

else:

    print(
        "沒有 DISCORD_WEBHOOK"
    )