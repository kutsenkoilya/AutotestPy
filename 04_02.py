# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:26:40 2020

@author: kompich
"""

from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
# scroll to see button with JS script execution
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True