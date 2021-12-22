from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render() # use for getting dynamic data

# full html
# print(html.html)

# text
# print(html.text)

# match = html.find('div')
# print(match)
# print(match[0]) or match = html.find('div', first=True)
# print(match[0].text)


# searching by id
# match = html.find('#footer', first=True)
# print(match.text)

# for article in html.find('div.article'):
#     headline = article.find('h2', first=True).text
#     print(headline)
#     summary = article.find('p', first=True).text
#     print(summary)
#     print()


# getting dynamic data
match = html.find('#footer', first=True)
print(match.html)