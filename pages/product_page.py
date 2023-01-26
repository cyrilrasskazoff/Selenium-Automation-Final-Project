from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_page(self,):
        self.should_be_product_page_url()
        self.should_be_add_to_cart_btn()
        self.add_to_cart()
        self.correct_product()
        self.correct_price()

    def should_be_product_page_url(self):  # проверка правильности URL страницы логина
        assert "?promo=" in self.browser.current_url, "This is not a product page"

    def should_be_add_to_cart_btn(self): # проверка наличия кнопки корзины
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "There is no 'Add To Cart' button"

    def add_to_cart(self):  # метод для добавления в корзину
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.click()

    def correct_product(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text == self.browser.find_element(
            *ProductPageLocators.ALERT_WITH_BOOK_TITLE).text, "Wrong product title"

    def correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text in self.browser.find_element(
            *ProductPageLocators.ALERT_WITH_CART_PRICE).text, "Wrong sum in cart"

    def should_not_be_success_message(self): # упадет, как только увидит искомый элемент
        assert self.is_not_element_present(*ProductPageLocators.ALERT_WITH_BOOK_TITLE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self): # упадет, как только увидит искомый элемент
        assert self.is_disappeared(*ProductPageLocators.ALERT_WITH_BOOK_TITLE), \
            "Success message is presented, but should disappear"