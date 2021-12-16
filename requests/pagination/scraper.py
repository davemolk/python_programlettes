import requests
from bs4 import BeautifulSoup

url = ''

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title)