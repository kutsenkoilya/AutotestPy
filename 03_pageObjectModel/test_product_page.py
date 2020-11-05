"""
Run as :
pytest -s -v --tb=line --language=en test_product_page.py

pytest -s -v -m user_can

pytest -s -v --tb=line -m basket test_product_page.py
pytest -s -v --tb=line -m need_review test_product_page.py
pytest -v --tb=line --language=en -m need_review
"""

import pytest
import time

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage

@pytest.mark.user_can
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(str(time.time()) + "@fakemail.org",'Qwerty1@Qwerty1@')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    @pytest.mark.parametrize('page_url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
                                        "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"])
    def test_user_can_add_product_to_basket(self,browser,page_url):
        page = ProductPage(browser, page_url)
        page.open()
        page.add_to_the_basket()
        page.check_book_name_is_correct()
        page.check_basket_total_is_correct()

    def test_user_cant_see_success_message(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message_present()

@pytest.mark.need_review
@pytest.mark.parametrize('page_url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
                                        "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"])
def test_guest_can_add_product_to_basket(browser,page_url):
    page = ProductPage(browser, page_url)
    page.open()
    page.add_to_the_basket()
    page.check_book_name_is_correct()
    page.check_basket_total_is_correct()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_present()

@pytest.mark.parametrize('page_url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                                        "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_add_product_to_basket_with_alert(browser,page_url):
    page = ProductPage(browser, page_url)
    page.open()
    page.add_to_the_basket()
    page.solve_quiz_and_get_code()
    page.check_book_name_is_correct()
    page.check_basket_total_is_correct()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_bug(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_basket()
    page.solve_quiz_and_get_code()
    page.check_book_name_is_correct()
    page.check_basket_total_is_correct()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_basket()
    page.should_not_be_success_message_present()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_basket()
    page.should_not_be_success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_contains_empty_message()


