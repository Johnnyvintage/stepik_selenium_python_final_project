import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.need_review
@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
             pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу
    page.add_to_basket()                # добавляем в корзину


@pytest.mark.skip
@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_button()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()


@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_empty_basket()


@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_see_product_in_basket_opened_after_add_product(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_products_in_basket()


@pytest.mark.latest
@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user()
        login_page.should_be_authorized_user()
        login_page.go_to_home_page()
        yield
        page.logout()

    @pytest.mark.need_review
    @pytest.mark.parametrize(
        'link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()

    @pytest.mark.parametrize(
        'link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_disappear_success_message()

