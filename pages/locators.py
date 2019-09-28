from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, '//div[contains(@class, "basket-mini")]//a[contains(@class, "btn-default") and contains(@href, "basket")]')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = "/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    BASKET_SUM_MESSAGE = (By.XPATH, '//div[contains(@class,"alert-info")]//strong')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class,"alert-success")]//strong')
    # LET'S TRY CSS SELECTORS, FOLKS!
    # PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    # BASKET_SUM_MESSAGE = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success > div > strong')


class BasketPageLocators():
    BASKET_LINK = "/basket/"
    BASKET_SUMMARY = (By.CLASS_NAME, "basket_summary")
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')







