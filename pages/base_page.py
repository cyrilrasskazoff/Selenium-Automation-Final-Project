from selenium.common.exceptions import NoSuchElementException
# базовая страница, от которой будут унаследованы все остальные классы. В ней опишем вспомогательные методы для работы с драйвером.
#
# добавим конструктор — метод, который вызывается, когда мы создаем объект. В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
# Внутри конструктора сохраняем эти данные как атрибуты нашего класса
class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) # командa для неявного ожидания со значением по умолчанию в 10

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
