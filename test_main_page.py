from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage(MainPage):
    def test_guest_can_go_to_login_page(self):
        self.go_to_login_page()
