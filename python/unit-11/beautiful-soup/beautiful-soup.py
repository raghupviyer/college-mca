import requests
from bs4 import BeautifulSoup

response = requests.get('http://olympus.realpython.org/profiles/aphrodite')

print(response)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
# parsing html
print(soup.find_all())

print('---')
title = soup.find('title')
print(title.text)
print(soup.get_text()) #get all text of the webpage

print('\n---urllib---\n')

from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())
image = soup.find('img')
print(image.name)

print(image["src"])