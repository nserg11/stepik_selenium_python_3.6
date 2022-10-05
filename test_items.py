import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    browser.get(link)
    time.sleep(10)
    try:
        button_exists = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    except NoSuchElementException:
        button_exists = False
    assert button_exists, "Button not found"

