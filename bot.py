import os
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime


WEBHOOK = os.getenv("DISCORD_WEBHOOK")

URL = "https://www.playdeltaforce.com/events/hq/zh-tw/m/index.html"


def get_page_text():

    response = requests.get(URL)

    response.encoding = "utf-8"

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    return soup.get_text("\n")


text = get_page_text()


today = datetime.now().strftime("%Y-%m-%d")


# 找所有四位數字
numbers = re.findall(r"\b\d{4}\b", text)


passwords = "\n".join(numbers)


message = f"""△Daily password

日期：{today}

找到的四位數：

{passwords}

Hope every1 got red until u rest in peace
"""


requests.post(
    WEBHOOK,
    json={
        "content": message
    }
)
