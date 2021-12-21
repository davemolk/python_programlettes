from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import time
import deets

s = HTMLSession()

query = 'denver'
url = f'https://www.google.com/maps'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})

# search = r.html.find('span', containing='Directions')
# print(search)

# test = r.html.find('title', first=True).text
# print(test)

start = deets.start
end = deets.end

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.google.com/maps')
    page.click("[aria-label=\"Directions\"]")
    page.click("[placeholder=\"Choose starting point, or click on the map...\"]")
    page.fill("[placeholder=\"Choose starting point, or click on the map...\"]", start)
    page.click("[placeholder=\"Choose destination, or click on the map...\"]")
    page.fill("[placeholder=\"Choose destination, or click on the map...\"]", end)
    page.press("[placeholder=\"Choose destination, or click on the map...\"]", "Enter")
    time.sleep(5)
    # switch to parsing


'''
plan:
use playwright and bs to get data for directions

use requests_html for error-handling, to confirm the css selectors
(will google change xpath etc? can they?)
'''