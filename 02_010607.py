# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:56:24 2020

@author: kompich
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
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
