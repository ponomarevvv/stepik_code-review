from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


def test_addtobasket_button(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    sleep(30)
    basket_button_located = EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".btn-add-to-basket")
    )
    assert basket_button_located

