from bs4 import *
import requests as r
from datetime import datetime
import os

if os.path.isfile('headlines.txt'):
    pass
else:
    with open('headlines.txt', 'w'):
        pass

now = datetime.now()


source = r.get('https://www.tijd.be/').text

soup = BeautifulSoup(source, features='html.parser')

match = soup.find_all('div', class_='c-articleteaser__title')

with open('headlines.txt', 'a', encoding="utf-8") as docu:
    docu.write(f"De Tijd headlines van {now}\n\n")

    for a in match:
        headline = a.text
        docu.write(f'-{headline}\n')

    docu.write('\n')
