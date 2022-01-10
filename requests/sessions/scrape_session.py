from bs4 import BeautifulSoup
import requests

import datetime


def get_title_session(page: int):
    """Print title of books on given page"""

    url = f'https://scrapethissite.com/pages/forms/?page_num={page}'
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title.text)
    return

# without session, took 0:00:12.080817
# with session, took 0:00:06.070323
if __name__ == '__main__':
    # keep out of main function to avoid new session w each func call
    session = requests.Session()
    start = datetime.datetime.now()
    for x in range(1, 21):
        get_title_session(x)
    finish = datetime.datetime.now() - start
    print(finish)


'''
Use Session when mak,ing multiple attempts to the same server to 
reuse the underlyping TCP connection
'''
