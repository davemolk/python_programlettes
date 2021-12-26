import requests
from bs4 import BeautifulSoup, SoupStrainer

import re

url = 'https://en.wikipedia.org/wiki/Extract,_transform,_load'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# ********* using regex *********
# for tag in soup.find_all('span', {'class': re.compile('headline')}):
#     print(tag.text)


# ********* search using a list *********
# for item in soup.find_all(['h1', 'h2', 'h3',]):
    # print(item)
    # print(item.text.strip())


# ********* write your own functions *********
# def links_in_para(tag):
#     return tag.has_attr('title') and tag.has_attr('href') and not tag.has_attr('class')


# for item in soup.find_all(links_in_para):
#     print(item)


# ********* function and regex *********
# def internal_links(href):
#     return href and re.compile("Category").search(href)

# for item in soup.find_all(href=internal_links):
#     print(item)


# ********* search via string *********
# print(soup.find_all('a', string='Data'))


# ********* search via lists *********
# print(soup.find_all('a', string=['Data', 'Extract', 'Load']))


# ********* search via regex *********
# print(soup.find_all('a', string=re.compile('Data')))


# ********* CSS Selectors (notice how these use select instead of find) *********
# find all a tags in the body tag
# for link in soup.select('body a'):
    # print(link)


# find all a tags contained within a p tag
# for link in soup.select('p > a'):
#     print(link)


# specific selector (from inspector)
# print(soup.select('#t-whatlinkshere > a > span'))


# ********* SoupStrainer *********
# only extracts data that fits your criteria
only_a_tags = SoupStrainer('a')

second_soup = BeautifulSoup(r.text, 'html.parser', parse_only=only_a_tags)
# print(second_soup)

