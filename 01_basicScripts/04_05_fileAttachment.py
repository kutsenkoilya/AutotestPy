"""
1. Fill form
2. Attach file
3. Submit
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
    time.sleep(10)
    browser.quit()