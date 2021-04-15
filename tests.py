from bs4 import *
import requests as r

source = r.get('https://docs.python-requests.org/en/master/').text

soup = BeautifulSoup(source, features="html.parser")



# match var.find('div', class_='footer'))
# match a div with an id of footer
# check = article.p.text

match = soup.find('div', class_='footer')

finish = match.a.text
print(finish)