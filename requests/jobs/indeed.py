import requests
from bs4 import BeautifulSoup


# extract, transform, load
def extract(page):
    # google 'my user agent'
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=python%20developer&l=Denver%2C%20CO&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='jobsearch-SerpJobCard')
    return len(divs)

c = extract(0)
print(transform(c))