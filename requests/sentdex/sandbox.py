import requests
from bs4 import BeautifulSoup

r = requests.get('https://pythonprogramming.net/parsememcparseface/')
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
body = soup.find('body')
# print(body.prettify())


# ****** intro stuff ******
intro = soup.find('div', class_='body').p.text
# print(intro)

first_link = soup.find('p', class_ = 'introduction').a['href']
# print(first_link)


# ****** languages at top ******
languages = soup.find('div', class_ = 'body').ul
# print(languages)

# for language in languages:
#     print(language.string)
# for language in languages.find_all('li'):
#     print(language.text.strip())


# ****** table ******
table = soup.find('table')
table_rows = table.find_all('tr')
my_languages = []
for tr in table_rows[1:8]:
    td = tr.find_all('td')
    row = [i.text for i in td]
    my_languages.append(row[0])
print(my_languages)





koan = soup.find('pre').text
# print(koan)

image = soup.find('img', class_='responsive-img')['src']
# print(image)
