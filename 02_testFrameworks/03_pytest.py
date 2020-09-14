"""
Tests through PyTest test runner

test_registration2 fails!!!

Test structure:
1. Fill mandatory fields
2. Press submit
3. Wait 1 sec
4. Compare form result with target message
"""

import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .form-group.first_class > .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .form-group.second_class > .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .form-group.third_class > .form-control.third")
        input3.send_keys("test@test.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Registration error')

        time.sleep(5)
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        field_selector_list = ['first','second','third']
        
        for className in field_selector_list:
            selectorName = '.{0}[required=""]'.format(className)
            element = browser.find_element_by_css_selector(selectorName)
            element.send_keys("Мой Ответ")
        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Registration error')

        time.sleep(5)
        browser.quit()

if __name__=="__main__":
    unittest.main()