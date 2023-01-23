# Первый тест на основе Page Object + переход между страницами (метод .current_url)
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_should_see_login_link_on_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object главной страницы, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object страницы логина, передаем в конструктор экземпляр драйвера и текущий URL
    login_page.should_be_login_page() # проверка URL страницы логина

# команда для запуска: pytest -v --tb=line --language=en test_main_page.py