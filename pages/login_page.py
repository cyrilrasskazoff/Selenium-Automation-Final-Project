# Page Object для страницы логина
from .base_page import BasePage
from .locators import LoginPageLocators
import time
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self): # проверка правильности URL страницы логина
        assert "login" in self.browser.current_url, "This is not a login page"

    def should_be_login_form(self): # проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self): # проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "Testtest123!"
        email_address = self.browser.find_element(*LoginPageLocators.REG_FORM_EMAIL_ADDRESS)
        email_address.send_keys(email)
        psw_field = self.browser.find_element(*LoginPageLocators.REG_FORM_PSW)
        psw_field.send_keys(password)
        confirm_psw_field = self.browser.find_element(*LoginPageLocators.REG_FORM_CONFIRM)
        confirm_psw_field.send_keys(password)
        sign_up = self.browser.find_element(*LoginPageLocators.REG_FORM_SIGN_UP)
        sign_up.click()






