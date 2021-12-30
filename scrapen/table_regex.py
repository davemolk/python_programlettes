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
emails = re.findall(r'([\d\w\-\.]+@[\d\w\-\.]+\.\w+)', soup.text)
numbers = re.findall(r'(1-\(?\d{3}\)?-\d{3}-\d{4})', soup.text)

# using regex and soup
emails_regex = soup.find_all('td', string=re.compile(r'([\d\w\-\.]+@[\d\w\-\.]+\.\w+)'))
emails_cleaned = [email.text for email in emails_regex]

numbers_regex = soup.find_all('td', string=re.compile(r'(1-\(?\d{3}\)?-\d{3}-\d{4})'))
nums_cleaned = [num.text for num in numbers_regex]
print(nums_cleaned)
