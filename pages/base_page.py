# базовая страница, от которой будут унаследованы все остальные классы.
# В ней опишем вспомогательные методы для работы с драйвером.
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .locators import MainPageLocators #- transferred MainPageLocators to BasePageLocators
from .locators import BasePageLocators
import math

# добавим конструктор — метод, который вызывается, когда мы создаем объект. В него в качестве параметров мы передаем
# экземпляр драйвера, url адрес, (опционально timeout).
# Внутри конструктора сохраняем эти данные как атрибуты нашего класса


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # командa для неявного ожидания со значением по умолчанию в 10

    # добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # реализуем метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд) и что искать (строку-селектор).
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):  # метод, который проверяет, что элемент не появляется на
        # странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):  # метод, который проверяет, что элемент исчезнет со страницы по
        # истечении заданного времени
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))  # # 3 аргумент означает частоту опроса, Т.е.
            # WebDriver ждёт 4 секунды и делает запросы каждую секунду
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):  # метод, который будет проверять переход по ссылке на страницу логина
        login_link = self.browser.find_element(
            *BasePageLocators.LOGIN_LINK)  # * указывает на то, что мы передали именно пару, и этот кортеж нужно
        # распаковать.
        login_link.click()

    # def should_be_login_link(self): # метод, который будет проверять наличие ссылки. Обычно все такие
    # методы-проверки называются shpould_be_(название элемента self.browser.find_element(By.CSS_SELECTOR,
    # "#login_link")

    # более сложная реализация (с пом. assert, Exceptions) метода выше
    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"  # * указывает на то, что мы передали именно
        # пару, и этот кортеж нужно распаковать.

    def should_be_authorized_user(self): # проверка авторизации пользователя
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def go_to_basket_page(self):  # метод, который будет проверять переход по ссылке на страницу корзины
        view_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET_BUTTON), "There is no basket page link"

    def solve_quiz_and_get_code(self):  # метод для решения уравнения (дополнительное усложнение для product_page)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
