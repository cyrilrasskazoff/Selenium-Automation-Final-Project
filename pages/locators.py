# вынос селекторов во внешнюю переменную
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # каждый селектор — это пара: как искать и что искать
    VIEW_BASKET_BUTTON = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BOOK_TITLE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    BOOK_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    ALERT_WITH_BOOK_TITLE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    ALERT_WITH_CART_PRICE = (By.XPATH, "//*[@id='messages']/div[3]")


class BasketPageLocators:
    ITEMS_IN_BASKET = (By.XPATH, "//*[@id='content_inner']/div[1]/div/h2")
    EMPTY_BASKET_STATE = (By.XPATH, "//*[@id='content_inner']/p")
