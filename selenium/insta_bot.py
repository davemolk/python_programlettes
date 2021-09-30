import os
from time import sleep
from urllib.parse import urlparse

import requests
import environ
from selenium import webdriver

env = environ.Env()
environ.Env.read_env()
username = env('username')
password = env('password')

class InstaBot():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()
    
    def login(self):
        username = self.username
        password = self.password
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.instagram.com')
        sleep(2)
        self.browser.find_element_by_name('username').send_keys(username)
        sleep(1)
        self.browser.find_element_by_name('password').send_keys(password)
        sleep(2)
        self.browser.find_element_by_css_selector("button[type='submit']").click()
        sleep(3)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(3)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def follower(self, url="https://www.instagram.com/therock"):
        pass

insta = InstaBot(username, password)
insta.login()

# def main():
#     my_bot = InstaBot()
#     sleep(60*60)

# if __name__ == '__main__':
#     main()