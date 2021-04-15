<<<<<<< HEAD
# webscraping tutorial

import bs4 as bs
import requests as r

#source= r.get('url).text

# format to see nesting
# print(var.prettify())
=======
#Websraping tutorial

from bs4 import *
import requests as r

source = r.get('https://docs.python-requests.org/en/master/').text

soup = BeautifulSoup(source, features="html.parser")

>>>>>>> tests


# match var.find('div', class_='footer'))
# match a div with an id of footer
# check = article.p.text
<<<<<<< HEAD
=======

match = soup.find('div', class_='footer')

finish = match.a.text
print(finish)
>>>>>>> tests
