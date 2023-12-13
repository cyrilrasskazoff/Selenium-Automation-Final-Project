from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self): # проверка правильности URL страницы корзины
        assert "basket" in self.browser.current_url, "This is not a basket page"

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "There basket contains products"

    def should_be_empty_basket_state(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_STATE), "The basket is not empty"

    def should_be_empty_basket_text(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_STATE).text, \
            "The empty basket text is wrong"

