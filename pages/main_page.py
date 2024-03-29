# Page Object для главной страницы сайта
from .locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    pass

# !!! at later stages we refactored the code by moving methods of MainPage to BasePage, thus class MainPage is no longer needed

# below is the initial realization of MainPage:

# class MainPage(BasePage):
#     def go_to_login_page(self): # метод, который будет проверять переход по ссылке на страницу логина
#         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
#         login_link.click()
#
#     # def should_be_login_link(self): # метод, который будет проверять наличие ссылки. Обычно все такие методы-проверки называются shpould_be_(название элемента
#     #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented" # здесь ссылка неверная --> тест упадет с Exception
#
#     # более сложная реализация (с пом. assert, Exceptions) метода выше
#     def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
