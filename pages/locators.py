# вынос селекторов во внешнюю переменную
# каждый селектор — это пара: как искать и что искать
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_FORM_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM_PSW = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_FORM_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_FORM_SIGN_UP = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    BOOK_TITLE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    BOOK_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    ALERT_WITH_BOOK_TITLE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    ALERT_WITH_CART_PRICE = (By.XPATH, "//*[@id='messages']/div[3]")


class BasketPageLocators:
    ITEMS_IN_BASKET = (By.XPATH, "//*[@id='content_inner']/div[1]/div/h2")
    EMPTY_BASKET_STATE = (By.XPATH, "//*[@id='content_inner']/p")
