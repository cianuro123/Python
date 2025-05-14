from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
from os import system
if system != 0:system("cls")
url = "https://www3.animeflv.net/browse?type%5B%5D=tv&order=rating"
info = requests.get(url)
html = info.text
soup = BeautifulSoup(html, 'html.parser')
div_title = soup.find({'div': 'Title'})
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
##########################################
import requests
from bs4 import BeautifulSoup
url = "https://es.wikipedia.org/wiki/Inteligencia_artificial"
get_url = requests.get(url)
soup = BeautifulSoup(get_url.text, 'html.parser')
# parrafos=[parrafo.get('p') for parrafo in soup.find_all('div', class_="mw-content-ltr mw-parser-output")]
# print(parrafos)
find = soup.find('div', {'id': 'mw-content-text'}).get_text() 
with open("Info_wikipedia.txt", "w", encoding="utf-8") as f:
    f.write(find)

#get.text() recupera todo el texto que albergue el elemento
#request.get(url) recupera el contenido de la url
#soup.find()  # Aquí puedes especificar el tipo de elemento que deseas buscar
#BeautifulSoup(html, 'html.parser') # Aquí puedes especificar el tipo de parser que deseas usar
#with es un manejador de contexto que se utiliza para abrir y cerrar archivos automáticamente
# with open ("Info_wikipedia.txt", "w", encoding="utf-8") as f: # Abre el archivo en modo escritura y lo codifica en utf-8
#as f refiere a la variable que se usará para referirse al archivo abierto
#f.write(find) # Escribe el contenido de la variable find en el archivo

##########################################

#funcion para buscar texto en una url



