import requests
from bs4 import BeautifulSoup


URL = "https://www.playdeltaforce.com/events/hq/en/m/index.html"


def get_passwords():

    response = requests.get(URL)

    response.encoding = "utf-8"

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    result = {}

    for span in soup.find_all("span"):

        info = span.get("data-info")

        if info and info.startswith("operations-"):

            result[info] = span.text.strip()


    return result



passwords = get_passwords()


print("=== Daily Password Test ===")


for name, password in passwords.items():

    print(
        name,
        "=>",
        password
    )