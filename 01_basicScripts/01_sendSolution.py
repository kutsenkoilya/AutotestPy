
"""
Sample stepik script
"""

import time

from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5) #5 sec pause

driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

textarea = driver.find_element_by_css_selector(".textarea")
textarea.send_keys("get()") #Press text area

time.sleep(5)

submit_button = driver.find_element_by_css_selector(".submit-submission")
submit_button.click() #Press submit button

time.sleep(5)

driver.quit()