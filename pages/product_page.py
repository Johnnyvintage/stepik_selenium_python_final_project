from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_str_in_list(value, strlist):
    if type(strlist) == list:
        for i in strlist:
            if value == i:
                return True
    return False


class ProductPage(BasePage):
    def add_to_basket(self):
        self.click_button()
        self.solve_quiz_and_get_code()
        self.check_basket_sum()
        self.check_success_add_message()

    def click_button(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def check_basket_sum(self):
        price = (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)).text
        basket_message = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.BASKET_SUM_MESSAGE))
        print("basket_message", basket_message)
        basket_sum = basket_message.text
        print("basket_sum", basket_sum)
        assert price == basket_sum, f"basket sum {basket_sum} and price of the product {price} don't match!"

    def check_success_add_message(self):
        success_messages = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(ProductPageLocators.SUCCESS_MESSAGE))
        success_texts = [i.text for i in success_messages]
        name_of_product = (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)).text
        print("name_of_product:", name_of_product, "\nsuccess_texts:", success_texts)
        assert find_str_in_list(name_of_product, success_texts), \
            f"there is no {name_of_product} in adding to cart messages!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"
