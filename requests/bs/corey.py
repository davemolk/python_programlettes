from bs4 import BeautifulSoup
import requests


import csv
import re

'''
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

article = soup.find('article')
# print(article.prettify())


# ways to the same thing (works in part because there's only one a tag within the article tag)
# print(article.header.h2.a.text)
# print(article.h2.a.text)
# print(article.a.text)
headline = article.a.text

summary = article.find('div', class_='entry-content').p.text
# print(summary)

video_src = article.find('iframe', class_='youtube-player')['src']
# print(video_src)
# https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en-US&autohide=2&wmode=transparent
video_id = video_src.split('/')[4].split('?')[0]

match = re.search('^(https://)(www.youtube.com/)(embed/)(?P<video>[^?]*)', video_src)

vid_id = match.group('video')

yt_link = f'https://youtube.com/watch?v={vid_id}'

'''

csv_file = open('corey.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

url = 'http://coreyms.com/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')


for article in soup.find_all('article'):
    headline = article.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        video_src = article.find('iframe', class_='youtube-player')['src']
        match = re.search('^(https://)(www.youtube.com/)(embed/)(?P<video>[^?]*)', video_src)
        vid_id = match.group('video')
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])


csv_file.close()