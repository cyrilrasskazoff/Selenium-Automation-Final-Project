# Первый тест на основе Page Object + переход между страницами (метод .current_url) + негативные проверки
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


def test_guest_should_see_login_link_on_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object главной страницы, передаем в конструктор экземпляр
    # драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object страницы логина, передаем в
    # конструктор экземпляр драйвера и текущий URL
    login_page.should_be_login_page() # проверка URL страницы логина


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_no_items()
    basket_page.should_be_empty_basket_state()
    basket_page.should_be_empty_basket_text()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
# для запуска групы login_guest: pytest -v -m login_guest test_main_page.py
# для запуска всего модуля: pytest -v --tb=line --language=en test_main_page.py