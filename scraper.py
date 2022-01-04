from bs4 import BeautifulSoup
import requests

URL = 'https://www.brasiltronic.com.br/camera-digital-canon-dslr-eos-rebel-sl3-com-lente-ef-s-18-55mm-f-4-5-6-is-stm-p1330537'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content,'html.parser')

title = soup.find('h1', class_ = 'name').get_text().strip()

price = soup.find('strong', class_ = 'sale-price').get_text().strip()

print(title , price)