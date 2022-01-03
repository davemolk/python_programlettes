from bs4 import BeautifulSoup
import requests

url = 'https://realpython.github.io/fake-jobs/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
jobs = soup.find_all('div', class_='column')

data = []

for job in jobs:
    title = job.find('h2').text
    company = job.find('h3').text
    location = job.find('p', class_='location').text.strip()
    link = job.find('footer').find_all('a')[1].attrs.get('href')
    
    item = {
        'title': title,
        'company': company,
        'location': location,
        'link': link,
    }
    data.append(item)

print(data)