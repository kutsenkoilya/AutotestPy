"""
1. Fill a huge form
2. Find correct Submit button by XPath
3. Submit
"""


from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_tag_name('input')
    print(len(elements))
    
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
