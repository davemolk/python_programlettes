from time import sleep

import environ
from selenium import webdriver

env = environ.Env()
environ.Env.read_env()
username = env('username')
password = env('password')


browser = webdriver.Chrome()

url = 'https://www.instagram.com'
browser.get(url)

sleep(2)
username_el = browser.find_element_by_name('username')
username_el.send_keys(username)

password_el = browser.find_element_by_name('password')
password_el.send_keys(password)

sleep(2)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

# pop-ups
# sleep(2)
# browser.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()

# sleep(2)
# browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
sleep(2)
browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

sleep(3)
browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

# body_el = browser.find_element_by_css_selector('body')
# html_text = body_el.get_attribute('innerHTML')

# xpath
# my_button_xpath = "//button"
# browser.find_elements_by_xpath(my_button_xpath)


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