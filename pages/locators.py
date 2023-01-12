# вынос селекторов во внешнюю переменную
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # каждый селектор — это пара: как искать и что искать