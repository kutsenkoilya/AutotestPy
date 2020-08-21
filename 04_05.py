# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:48:29 2020

@author: kompich
"""

from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    
    input3 = browser.find_element_by_name('email')
    input3.send_keys("ivanpetrov@mail.com")
    
    file_name = '04_05.txt'
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, file_name)
    
    input4 = browser.find_element_by_id('file')
    input4.send_keys(file_path)
    
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()