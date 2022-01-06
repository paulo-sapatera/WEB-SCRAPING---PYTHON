from bs4 import BeautifulSoup
import requests

url = 'https://www.balaodainformatica.com.br/perifericos/teclados'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
teclados = soup.find_all('div', class_='.products-grid .main-info')
ultima_pagina = soup.find('span', class_='page-selected last')

teclado = teclados[0]
marca = teclado.find('a', class_= 'link-all')


print(marca)