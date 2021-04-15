## Copies all headlines from 'De Tijd' ##

from bs4 import *
import requests as r
from datetime import datetime
import os

# Checks it the file exists in the directory.

if os.path.isfile('headlines.txt'):
    pass
else:
    with open('headlines.txt', 'w'):
        pass

now = datetime.now()

# Gets the HTML of a webpage in text format.

source = r.get('https://www.tijd.be/').text

soup = BeautifulSoup(source, features='html.parser')

#Finds all html code in a <div> with the class 'c-articleteaser__title'

match = soup.find_all('div', class_='c-articleteaser__title') 

# Writes all found info and the current time in the .txt file.

with open('headlines.txt', 'a', encoding="utf-8") as docu:
    docu.write(f"De Tijd headlines van {now}\n\n")

    for a in match:
        headline = a.text
        docu.write(f'-{headline}\n')

    docu.write('\n')
