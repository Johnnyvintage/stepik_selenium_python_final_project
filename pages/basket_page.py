from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        url = self.browser.current_url
        assert BasketPageLocators.BASKET_LINK in url, f"Basket link is incorrect: {url}"

    def should_be_empty_basket(self):
        self.should_be_empty_basket_message()
        self.shouldnt_be_filled_basket()

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "There is no message that basket is empty"

    def shouldnt_be_filled_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "There is items in basket but shouldn't"

    def should_be_products_in_basket(self):
        self.shouldnt_be_empty_basket_message()
        self.should_be_filled_basket()

    def shouldnt_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_MESSAGE), "There is empty message in basket"

    def should_be_filled_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEM), "There are no items in basket, but should be"
