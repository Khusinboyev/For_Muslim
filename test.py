# import requests
# from bs4 import BeautifulSoup
#
# html_text = requests.get('https://islom.uz/lotin').text
# soup = BeautifulSoup(html_text, 'html.parser')
# regs = soup.find_all('a')
#
#
# print(regs)
from databas import *

import requests
from bs4 import BeautifulSoup

C_id = sql.execute(f"""SELECT number FROM city_id WHERE name = 'Хонқа'""").fetchone()
html_text = requests.get(f'https://islom.uz/region/{int(C_id[0])}').text
soup = BeautifulSoup(html_text, 'html.parser')