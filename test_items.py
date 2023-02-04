import pytest
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_exists(browser):
    browser.get(link)
    # time.sleep(30)
    elem_is_present = False
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        elem_is_present = True
    except NoSuchElementException:
        pass
    assert elem_is_present, "Add to cart button is not displayed"
