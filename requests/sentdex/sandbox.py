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

# table = soup.find('table')
# table_rows = table.find_all('tr')
# my_languages = []
# kittens = []
# for tr in table_rows[1:8]:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     my_languages.append(row[0])
#     kittens.append(row[2])
# print(my_languages)
# print(kittens)


# ****** image ******
image = soup.find('img', class_='responsive-img')['src']
# print(image)


# ****** js ******
js = soup.find('p', class_ = 'jstest').text
# print(js)
# need requests_html for dynamic data


# ****** python credo *******
koan = soup.find('pre').text
# print(koan)


# ****** footer ******
end = soup.find('h5', class_ = 'white-text').text
# print(end)

contact = soup.find('div', class_ = 's12').p.text
# print(contact)

links = soup.find('div', class_ = 's12').ul
link_list = []
for link in links.find_all('li'):
    link_list.append(link.a['href'])
print(link_list)