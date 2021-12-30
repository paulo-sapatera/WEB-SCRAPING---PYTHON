import requests
from bs4 import BeautifulSoup

url = 'https://www.netshoes.com.br/chuteiras/masculino?mi=hm_ger_mntop_H-CAL-calcados-chuteiras&psn=Menu_Top'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")
chuteiras = soup.find_all("div", class_='item-card__description')