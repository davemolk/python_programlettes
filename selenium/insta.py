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

# navigate somewhere
sleep(2)
the_rock_url = "https://www.instagram.com/therock"
browser.get(the_rock_url)

# look at a post
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

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

def scrape_and_save(elements):
    for element in elements:
        url = element.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

# scrape_and_save(images)

def commenter(browser, content='So awesome!'):
    sleep(3)
    # comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment...')]"
    comment_el = browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']") # not working, come back to this
    comment_el.send_keys(content)
    sleep(1)
    submit_btns_xpath = "button[type='submit']"
    submit_btns_els = browser.find_elements_by_css_selector(submit_btns_xpath)
    sleep(2)
    for btn in submit_btns_els:
        try:
            btn.click()
        except:
            pass

commenter(browser)