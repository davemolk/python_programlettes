from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs

with sync_playwright() as p:
    # headless by default, use slow_mo so you can see what's happening
    # browser = p.chromium.launch(headless=False, slow_mo=50)
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://demo.opencart.com/admin/')
    page.fill('input#input-username', 'demo')
    page.fill('input#input-password', 'demo')
    page.click('button[type=submit]')

    # wait until something is visible/loaded (not an issue here)
    # page.is_visible('div.tile-body')
    html = page.inner_html('#content')
    soup = bs(html, 'html.parser')
    total_orders = soup.find('h2', {'class': 'pull-right'}).text
    print(f'total orders = {total_orders}')
