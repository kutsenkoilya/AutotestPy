"""
DIY test runner implementation

Test structure:
1. Fill mandatory fields
2. Press submit
3. Wait 1 sec
4. Compare form result with target message
"""

from selenium import webdriver
import time

def test_registration2():
    try: 
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

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__=="__main__":
    test_registration2()
    print('All tests passed!')