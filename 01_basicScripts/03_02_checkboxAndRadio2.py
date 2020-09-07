"""
1. Find x
2. Calculate equation
3. Handle checkbox and radio button
4. Submit
"""

from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    treasure_element = browser.find_element_by_id("treasure")
    value_x = treasure_element.get_attribute("valuex")
    y = calc(value_x)
    
    input_textbox = browser.find_element_by_id("answer")
    input_textbox.send_keys(y)
    
    checkBox = browser.find_element_by_id("robotCheckbox")
    checkBox.click()
    
    radioButton = browser.find_element_by_id("robotsRule")
    radioButton.click()
    
    button = browser.find_element_by_class_name("btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()