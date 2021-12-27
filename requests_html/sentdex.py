from requests_html import HTMLSession

session = HTMLSession()

url = 'https://pythonprogramming.net/parsememcparseface/'

r = session.get(url)


# ****** all links ******
# print(r.html.links)


# ****** intro stuff ******
intro = r.html.find('.introduction', first=True).text
# print(intro)

bs_link = r.html.find('.introduction a', first=True).links
# print(bs_link)

more_intro = r.html.find('.body p')[1].text
# print(more_intro)


# ****** languages at top ******
language_list = r.html.find('.body ul', first=True)
# for language in language_list.find('li'):
#     print(language.text)


# ****** table ******
table_rows = r.html.find('tr')
# for td in table_rows[1:20]:
#     print(td.text)
    # range can go over and nothing bad happens


cats= []
for tr in table_rows[1:8]:
    td = tr.find('td')
    kitten = td[2].text
    cats.append(kitten)

# print(cats)


# ****** image ******
image = r.html.find('.responsive-img', first=True).attrs['src']
# print(image)


# ****** js ******
# r.html.render() ''' Need for JS to render '''

jstest = r.html.find('.jstest', first=True).text
# print(jstest)


# ****** zen of python *******
zen = r.html.find('pre', first=True).text
# print(zen)
