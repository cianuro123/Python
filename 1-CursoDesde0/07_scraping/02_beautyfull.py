from bs4 import BeautifulSoup
import requests
from os import system
if system != 0:
    system("cls")
url = "https://www3.animeflv.net/browse?type%5B%5D=tv&order=rating"
info = requests.get(url)
html = info.text
soup = BeautifulSoup(html, 'html.parser')
div_title = soup.find({'div':'Title'})
print(div_title)
title_find = soup.body.find('h3', class_="Title")
print(title_find)
##########################################
url = "https://midu.dev"
info = requests.get(url)
html = info.text
soup = BeautifulSoup(html, 'html.parser')
find = soup.find('li', property='h2')
print(find)


