# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:48:29 2020

@author: kompich
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    fair_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    book_button = browser.find_element_by_id("book")
    book_button.click()
        
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print('X:',x)
    y = calc(x)
    print('Y:',y)
    
    input_textbox = browser.find_element_by_id("answer")
    input_textbox.send_keys(y)
    
    submit_button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()