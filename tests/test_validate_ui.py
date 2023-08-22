from selenium import webdriver
from pages.homepage import Locator
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def setup_module():
    driver.get("http://localhost:3000/")
    time.sleep(5)


def test_validate_ui_header_is_present():
    assert driver.find_element(By.XPATH, Locator.header).text is not None


def test_validate_ui_search_form_is_present():
    assert driver.find_element(By.XPATH, Locator.search_form) is not None


def test_validate_ui_search_results_list_is_present():
    assert driver.find_element(By.XPATH, Locator.search_results) is not None


def test_validate_ui_header_is_the_same_as_title():
    assert driver.find_element(By.XPATH, Locator.header).text == driver.title


def teardown_module():
    driver.quit()
