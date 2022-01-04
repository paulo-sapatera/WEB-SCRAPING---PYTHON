import requests
from bs4 import BeautifulSoup

url = 'https://www.kabum.com.br/hardware/ssd-2-5?page_number=1&page_size=20&facet_filters=&sort=most_searched'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")
ssd =  soup.find_all("div", class_='sc-ctqQKy gLgKBM')
ultima_pagina = soup.find('span', class_='Page 42')

marca = ssd.find(class_='sc-kHOZwM brabbc sc-fHeRUh jwXwUJ nameCard')
print(marca)