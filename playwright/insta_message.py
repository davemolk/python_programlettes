from playwright.sync_api import sync_playwright
from decouple import config


import time


USERNAME = config("USERNAME")
PASSWORD = config("PASSWORD")
URL = config("URL")
RECIPIENT = config("RECIPIENT")
MESSAGE = config("MESSAGE")
RECIPIENT2 = config("RECIPIENT2")
MESSAGE2 = config("MESSAGE2")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.instagram.com/")

    # authentication
    page.click("[aria-label=\"Phone number, username, or email\"]")
    page.fill("[aria-label=\"Phone number, username, or email\"]", USERNAME)
    page.click("[aria-label=\"Password\"]")
    page.fill("[aria-label=\"Password\"]", PASSWORD)
    
    time.sleep(1.7)
    page.click("button:has-text(\"Log In\")")
    page.click("text=Not Now")
    
    # message
    page.click("[aria-label=\"Messenger\"]")
    page.click(":nth-match(button, 3)")
    page.fill("[placeholder=\"Search...\"]", RECIPIENT)
    page.press("[placeholder=\"Search...\"]", "Enter")

    # select user
    page.click("div.-qQT3")
    page.click("button:has-text(\"Next\")")
    page.click("textarea")
    page.fill("textarea", MESSAGE)
    page.click("text=Send")
    time.sleep(1.3)

    # send to myself
    page.click("[aria-label=\"Messenger\"]")
    page.click(":nth-match(button, 3)")
    page.fill("[placeholder=\"Search...\"]", RECIPIENT2)
    page.press("[placeholder=\"Search...\"]", "Enter")

    # select user
    page.click("div.-qQT3")
    page.click("button:has-text(\"Next\")")
    page.click("textarea")
    page.fill("[placeholder=\"Message...\"]", MESSAGE2)
    page.click("text=Send")
    time.sleep(2)