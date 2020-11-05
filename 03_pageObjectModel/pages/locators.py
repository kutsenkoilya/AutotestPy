from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_SUBMIT = (By.NAME, 'registration_submit')

class ProductPageLocators():
    ADD_TO_THE_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    SUCCESS_POPUP_TEXT = (By.CSS_SELECTOR, '.alert-success div strong')
    BASKET_POPUP_TEXT = (By.CSS_SELECTOR, '.alert-info div p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success.fade.in')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-default[href]")
    BASKET_BUTTON_2 = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")

class BasketPageLocators():
    IS_EMPTY_LINK = (By.CSS_SELECTOR, "div.content div#content_inner p a[href='/en-gb/']")
    BASKET_TOTALS_LINK = (By.CSS_SELECTOR, "div.content div#content_inner div#basket_totals")

    