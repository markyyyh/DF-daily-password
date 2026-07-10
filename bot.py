import requests
from bs4 import BeautifulSoup

URL = "https://www.playdeltaforce.com/events/hq/zh-tw/m/index.html"

html = requests.get(URL).text

soup = BeautifulSoup(html, "html.parser")


scripts = soup.find_all("script")

print("找到 JS 數量:", len(scripts))

for s in scripts:
    if s.get("src"):
        print(s.get("src"))
