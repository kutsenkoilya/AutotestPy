
from selenium.webdriver.common.by import By

from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTALS_LINK), "Basket is not empty"

    def basket_contains_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.IS_EMPTY_LINK), "Basket is empty message is missing"
