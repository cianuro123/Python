###
# 01 - Web Scraping
# Es la recuperacion de la informacion almacenada en una pagina web.
###
import requests
import re
from os import system
if system != 0:
    system("cls")

url = "https://xiaomistore.com.ar/?srsltid=AfmBOorSRfPxhRzM_r4BmX0fmdjinU6LyaTsf5fzsfzx-sXj_UYL2Xl1"
info_url = requests.get(url)
txt_url = info_url.text

pattern = r'<span class="product-price" content="1649999" aria-label="Precio"> \$&nbsp;(.+?) </span>'
match = re.search(pattern, txt_url)
print(f"El precio del primer celular de la tienda de xiaomi es de:\n${match.group(1)}")
