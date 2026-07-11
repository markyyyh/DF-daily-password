import requests
from bs4 import BeautifulSoup
import time


URL = "https://www.playdeltaforce.com/events/hq/en/m/index.html?t=" + str(int(time.time()))


def get_passwords():

    response = requests.get(
        URL,
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.encoding = "utf-8"

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    passwords = {}

    maps = [
        "operations-zero-dam",
        "operations-layali-grove",
        "operations-layali-brakkesh",
        "operations-layali-space-city",
        "operations-layali-tide-prison",
        "operations-layali-az3"
    ]

    for map_name in maps:

        result = soup.find(
            "span",
            {
                "data-info": map_name
            }
        )

        if result:
            passwords[map_name] = result.text.strip()

        else:
            passwords[map_name] = "沒有"


    return passwords



passwords = get_passwords()


print("=== Daily Password Test ===")


for name, password in passwords.items():

    print(
        name,
        "=>",
        password
    )