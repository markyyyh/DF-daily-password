import os
import requests
from datetime import datetime


WEBHOOK = os.getenv("DISCORD_WEBHOOK")


today = datetime.now().strftime("%Y-%m-%d")


passwords = {
    "零號大壩": "0213",
    "長弓溪谷": "0911",
    "巴克什": "0341",
    "航天基地": "0729",
    "潮汐監獄": "0035",
    "AZ3": "0510"
}


message = f"""△Daily password

日期：{today}

零號大壩：{passwords["零號大壩"]}
長弓溪谷：{passwords["長弓溪谷"]}
巴克什：{passwords["巴克什"]}
航天基地：{passwords["航天基地"]}
潮汐監獄：{passwords["潮汐監獄"]}
AZ3：{passwords["AZ3"]}

Hope every1 got red until u rest in peace
"""


requests.post(
    WEBHOOK,
    json={
        "content": message
    }
)
