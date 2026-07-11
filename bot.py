import requests
from bs4 import BeautifulSoup


URL = "https://www.playdeltaforce.com/events/hq/en/m/index.html"


html = requests.get(URL).text

soup = BeautifulSoup(html, "html.parser")


for span in soup.find_all("span"):
    if span.get("data-info"):
        print(
            span.get("data-info"),
            "=>",
            span.text
        )