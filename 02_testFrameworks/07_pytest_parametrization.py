"""
Run as:
pytest -s -v .\07_pytest_parametrization.py

"""


import time
import math
import pytest
from selenium import webdriver

def calculate_answer():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

#page url example
#https://stepik.org/lesson/236895/step/1

@pytest.mark.parametrize('page_url', ['236896','236897','236898','236899','236903','236904','236905'])
def test_hiddenmessage(browser, page_url):

    
    link = f"https://stepik.org/lesson/{page_url}/step/1"
    print(f'Connecting to: {link}')
    browser.get(link)
    time.sleep(5)

    v_text_area = browser.find_element_by_class_name("textarea")
    v_text_area.send_keys(str(calculate_answer()))

    v_button = browser.find_element_by_class_name("submit-submission")
    v_button.click()

    time.sleep(5)
    v_response = browser.find_element_by_class_name("smart-hints__hint")

    print(f'response: {v_response}')
    
    assert v_response.text == "Correct!"
    
