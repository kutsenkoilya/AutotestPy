# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:48:29 2020

@author: kompich
"""

from selenium import webdriver
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_class_name("trollface")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input_textbox = browser.find_element_by_id("answer")
    input_textbox.send_keys(y)
    
    button = browser.find_element_by_class_name("btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()