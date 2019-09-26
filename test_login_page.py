from pages.main_page import MainPage
from pages.login_page import LoginPage
LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_authorization_forms(browser):
    page = MainPage(browser, LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()