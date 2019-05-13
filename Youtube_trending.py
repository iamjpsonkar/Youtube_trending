import os
import datetime


if os.path.isfile("log.txt") != True:
    os.system("source venv/bin/activate")
    os.system("easy_install-3.7 bs4")
    os.system("easy_install-3.7 requests")
    os.system("easy_install-3.7 xlsxwriter")
    f = open("log.txt", 'w')
    f.write("==> setup run "+str(datetime.datetime.now())+"\n")
    f.close()


f = open("log.txt",'a')
f.write("==> app run "+str(datetime.datetime.now())+"\n")
f.close()


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

