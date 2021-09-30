import time

from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://google.com'

browser.get(url)

time.sleep(3) # number of seconds to sleep
name = 'q'
search_element = browser.find_element_by_name(name)
print(search_element)

# search_element.send_keys("selenium python")
search_element.send_keys("selenium python")

submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()

lnks=browser.find_elements_by_tag_name("a")
for lnk in lnks:
    print(lnk.get_attribute('href'))