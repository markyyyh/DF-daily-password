import os
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright


WEBHOOK = os.getenv("DISCORD_WEBHOOK")

URL = "https://www.playdeltaforce.com/events/hq/zh-tw/m/index.html"


def get_password():

    result = {}

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            URL,
            wait_until="networkidle"
        )


        keys = {
            "零號大壩": "operations-zero-dam",
            "萊亞利叢林": "operations-layali-grove",
            "布拉克什": "operations-layali-brakkesh",
            "空城": "operations-layali-space-city",
            "潮汐監獄": "operations-layali-tide-prison",
            "AZ3": "operations-layali-az3"
        }


        for name, key in keys.items():

            try:
                value = page.locator(
                    f'[data-info="{key}"]'
                ).inner_text()

            except:
                value = "無資料"


            result[name] = value


        browser.close()


    return result



passwords = get_password()


today = datetime.now().strftime("%Y-%m-%d")


message = f"""
△ Daily Password

日期：{today}

零號大壩：{passwords["零號大壩"]}
長弓溪谷：{passwords["長弓溪谷"]}
巴克什：{passwords["巴克什"]}
航天基地：{passwords["航天基地"]}
潮汐監獄：{passwords["潮汐監獄"]}
AZ3：{passwords["AZ3"]}
"""


print(message)


requests.post(
    WEBHOOK,
    json={
        "content": message
    }
)