# Scrapping NASA By Using Phython Language.

import requests
from bs4 import BeautifulSoup
import re
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

for count in range(1, 50):
    response = requests.get(f"https://www.nasa.gov/news/all-news/page/{count}/")
    soup = BeautifulSoup(response.content, "html.parser")

    last_page_link = soup.find("a", class_="page-link", title="Go to last page")
    if last_page_link:
        last_page = int(last_page_link.text)
    else:
        last_page = count

    entry_contents = soup.find_all("div", class_="entry-content")
    print(count)

    for entry_content in entry_contents:

        sheet.append([])

        content_text = entry_content.get_text(strip=True)
        sentences = re.split(r'(?<=[.!?]) +', content_text)

        for sentence in sentences:
            print(sentence)

            sheet.append([sentence])

workbook.save(filename="nasa_news.xlsx")
