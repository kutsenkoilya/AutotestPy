from selenium.webdriver.common.by import By

import time

from .base_page import BasePage

from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_the_basket(self):

        self.book_title = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print(f'Title: {self.book_title}')

        self.book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        print(f'Price: {self.book_price}')

        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_THE_BASKET_BUTTON)
        add_button.click()
    
    def check_book_name_is_correct(self):
        popups_success_texts = self.browser.find_elements(*ProductPageLocators.SUCCESS_POPUP_TEXT)
        v_bookname_correct = False
        for v_str in popups_success_texts:
            print(f"Popup success text: {v_str.text}")
            if v_str.text == self.book_title:
                v_bookname_correct = True
        assert v_bookname_correct

    def check_basket_total_is_correct(self):
        popups_price_texts = self.browser.find_elements(*ProductPageLocators.BASKET_POPUP_TEXT)
        v_bookprice_correct = False
        for v_str in popups_price_texts:
            print(f"Popup total price: {v_str.text}")
            if v_str.text == self.book_price:
                v_bookprice_correct = True
        assert v_bookprice_correct

    def should_not_be_success_message_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"