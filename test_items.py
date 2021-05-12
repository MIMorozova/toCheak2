import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(link)
    browser.implicitly_wait(10)
#   time.sleep(30)
    x = browser.find_elements_by_css_selector("button.btn-ad56d-to-basket")
    assert x, "Все пропало,корзины нет!"