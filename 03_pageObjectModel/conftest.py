
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,help="Choose language")
    parser.addoption('--browser_name', action='store', default=None,help="Choose browser")

@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    if user_language is None:
        user_language = 'en'

    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print(f"\nstart firefox browser for tes with {user_language} profile..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else: # always run chrome browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print(f"\nstart chrome browser for test with {user_language} profile..")
        browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\nquit browser..")
    browser.quit()
