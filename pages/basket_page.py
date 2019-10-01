from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        url = self.browser.current_url
        assert BasketPageLocators.BASKET_LINK in url, f"Basket link is incorrect: {url}"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE) \
               and self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"

    def should_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_MESSAGE) \
               or self.is_element_present(*BasketPageLocators.BASKET_ITEM), "There is no products in basket"
