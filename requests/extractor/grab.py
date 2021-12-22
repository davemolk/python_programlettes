import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://books.toscrape.com"

session = requests.Session()

# set to User agent, not Python bot
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'

# get content
html = session.get(url).content

# parse w bs
soup = BeautifulSoup(html, 'html.parser')

# get js
js_files = []

for script in soup.find_all('script'):
    if script.attrs.get('src'):
        # absolute path
        script_url = urljoin(url, script.attrs.get('src'))
        js_files.append(script_url)

# get css
css_files = []

for css in soup.find_all('link'):
    if css.attrs.get('href'):
        # absolute path
        css_url = urljoin(url, css.attrs.get('href'))
        css_files.append(css_url)


print('Number of scripts: ', len(js_files))
print('Number of CSS files: ', len(css_files))


# write file links
with open('js_files.txt', 'w') as f:
    for js_file in js_files:
        print(js_file, file=f)

with open('css_files.txt', 'w') as f:
    for css_file in css_files:
        print(css_file, file=f)