
from selenium.webdriver.common.by import By

from .locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        #login_form
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_input.send_keys(password)

        password_redo_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_REPEAT)
        password_redo_input.send_keys(password)
        
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT)
        submit_button.click()
        