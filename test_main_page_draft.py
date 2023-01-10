from selenium.webdriver.common.by import By

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

# Что происходит в коде выше?
# Мы открываем ссылку, находим элемент с определенным селектором и нажимаем на этот элемент.
# Что мы на самом деле имеем в виду?
# Мы хотим открыть страницу логина. Давайте выделим это действие в отдельную функцию с понятным названием:

link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


# и наш тест упрощается:

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
