import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    get_x_value = browser.find_element(By.ID, "input_value").text
    y = calc(get_x_value)
    input_x_value = browser.find_element(By.ID, "answer")
    input_x_value.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
