from bs4 import BeautifulSoup
import requests

import datetime


def get_title(page: int):
    """print title of books on a page"""
    
    url = f'https://scrapethissite.com/pages/forms/?page_num={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title.text)
    return

# no session, took 0:00:12.080817
if __name__ == '__main__':
    start = datetime.datetime.now()
    for x in range(1, 21):
        get_title(x)
    finish = datetime.datetime.now() - start
    print(finish)