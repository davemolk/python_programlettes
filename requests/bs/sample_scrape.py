from bs4 import BeautifulSoup
import requests


with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# improve formatting
# print(soup.prettify())


# title = soup.title
# print(title)


# (without tags)
title = soup.title.text
# print(title)


# returns first div
div = soup.div
# print(div)


# find method, passing in attributes as arguments
div = soup.find('div', class_='footer')
# print(div)


# chaining things together for single result
# article = soup.find('div', class_='article')
# headline = article.h2.a.text
# text = article.p.text
# print(headline)
# print(text)


# find_all
articles = soup.find_all('div', class_='article')
for article in articles:
    headline = article.h2.a.text
    print(headline)
    text = article.p.text
    print(text)

    print()
