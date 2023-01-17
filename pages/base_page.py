from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math


# базовая страница, от которой будут унаследованы все остальные классы. В ней опишем вспомогательные методы для работы с драйвером.
#
# добавим конструктор — метод, который вызывается, когда мы создаем объект. В него в качестве параметров мы передаем экземпляр драйвера, url адрес, (опционально timeout).
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

    def solve_quiz_and_get_code(self): # метод для решения уравнения (дополнительное усложнение для практического задания по product_page)
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
