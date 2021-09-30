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


browser = webdriver.Chrome()

url = 'https://www.instagram.com'
browser.get(url)

# logging in
sleep(2)
username_el = browser.find_element_by_name('username')
username_el.send_keys(username)

password_el = browser.find_element_by_name('password')
password_el.send_keys(password)

sleep(2)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

# pop-ups
sleep(3)
browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

sleep(3)
browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

# body_el = browser.find_element_by_css_selector('body')
# html_text = body_el.get_attribute('innerHTML')


def click_to_follow(browser):
    # my_follow_btn_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    # my_follow_btn_xpath = "//a[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"

    my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    follow_btn_elments = browser.find_elements_by_xpath(my_follow_btn_xpath)
    for btn in follow_btn_elments:
        sleep(2) # self-throttle
        try:
            btn.click()
        except:
            pass


# ted_url = "https://www.instagram.com/ted/"
# browser.get(ted_url)
# click_to_follow(browser)

sleep(2)
the_rock_url = "https://www.instagram.com/therock"
browser.get(the_rock_url)


sleep(2)
# lnks=browser.find_elements_by_tag_name("a")
# for lnk in lnks:
#     print(lnk.get_attribute('href'))

post_links_url = "//a[contains(@href, '/p/')]"
post_links = browser.find_elements_by_xpath(post_links_url)
# for link in post_links:
#     print(link.get_attribute('href'))

if len(post_links) > 0:
    post_link = post_links[0]
    post_href = post_link.get_attribute('href')
    browser.get(post_href)




videos = browser.find_elements_by_xpath("//video")
images = browser.find_elements_by_xpath("//img")

base_dir = os.path.dirname(os.ath.abspath(__file__))
img_dir = os.path.join(base_dir, "images")
os.makedirs(img_dir, exist_ok=True)

for img in images:

    print(img.get_attribute('src'))