from bs4 import BeautifulSoup
import requests


import csv
import re


csv_file = open('corey_pagination.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


page = 0
r = requests.get('http://coreyms.com/')
while r.status_code != 404:
    page += 1
    url = 'http://coreyms.com/page/'f"{page}"
    r = requests.get('http://coreyms.com/page/'+ f"{page}")
    soup = BeautifulSoup(r.text, 'lxml')

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
# total_pages = page -1
