from bs4 import BeautifulSoup

import re

with open('info.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

all_data = []
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    if len(values) != 0:
        all_data.append(values)

phone_numbers = []
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    if len(values) != 0:
        phone_numbers.append(values[2])


# using straight regex
numbers = re.findall(r'(1-\(?\d{3}\)?-\d{3}-\d{4})', soup.text)

emails = re.findall(r'([\d\w\.]+@[\d\w\-\.]+\.\w+)', soup.text)


# using regex and soup
numbers = []
for td in soup.find_all('td', string=re.compile(r'(1-\(?\d{3}\)?-\d{3}-\d{4})')):
    numbers.append(td.text)

emails = []
for td in soup.find_all('td', string=re.compile(r'([\d\w\.]+@[\d\w\-\.]+\.\w+)')):
    emails.append(td.text)
