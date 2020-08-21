# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:41:10 2020

@author: kompich
"""
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input_textbox = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_textbox)
    input_textbox.send_keys(y)
    
    checkBox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkBox)
    checkBox.click()
    
    radioButton = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radioButton)
    radioButton.click()
    
    button = browser.find_element_by_class_name("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()