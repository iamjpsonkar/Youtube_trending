from bs4 import BeautifulSoup
from xlsxwriter import Workbook
import requests

w_name = Workbook("Youtube_trending.xlsx")
ws_name = w_name.add_worksheet()
ws_name.write(0, 0, 'S.NO.')
ws_name.write(0, 1, 'Title')
ws_name.write(0, 2, 'Link')
source = requests.get("https://www.youtube.com/feed/trending").text
soup = BeautifulSoup(source, 'html.parser')

count = 1
for content in soup.find_all('div', class_="yt-lockup-content"):
    title = content.h3.a
    ws_name.write(count, 0, count)
    ws_name.write(count, 1, title.text)
    ws_name.write(count, 2, "https://www.youtube.com"+title['href'])
    count += 1
    if count > 50:
        break

w_name.close()
