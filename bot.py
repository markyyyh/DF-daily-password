import os
import requests
from datetime import datetime

# 從 GitHub Secret 讀取 Discord Webhook
WEBHOOK = os.getenv("DISCORD_WEBHOOK")

today = datetime.now().strftime("%Y-%m-%d")

message = f"""△Daily password

日期：{today}

零號大壩：測試
長弓溪谷：測試
巴克什：測試
航天基地：測試
潮汐監獄：測試
AZ3：測試

Hope every1 got red until u rest in peace
"""

response = requests.post(
    WEBHOOK,
    json={"content": message}
)

print(response.status_code)
