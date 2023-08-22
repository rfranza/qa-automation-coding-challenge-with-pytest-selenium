from selenium import webdriver
from pages.homepage import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


def setup_module():
    driver.get("http://localhost:3000/")
    time.sleep(5)


def test_search_form_inserting_text_then_clicking_go():
    driver.find_element(By.XPATH, Locator.username).send_keys("Test")
    driver.find_element(By.XPATH, Locator.go_button).click()
    time.sleep(2)
    assert "Found" in driver.find_element(By.XPATH, Locator.repo_amount).text


def test_search_form_inserting_text_then_enter():
    driver.find_element(By.XPATH, Locator.username).clear()
    driver.find_element(By.XPATH, Locator.username).send_keys("example")
    driver.find_element(By.XPATH, Locator.username).send_keys(Keys.ENTER)
    time.sleep(2)
    assert "Found" in driver.find_element(By.XPATH, Locator.repo_amount).text


def teardown_module():
    driver.quit()
