from selenium import webdriver
from pages.homepage import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


def setup_module():
    driver.get("http://localhost:3000/")
    time.sleep(5)


def test_success_message():
    driver.find_element(By.XPATH, Locator.username).send_keys("Test")
    driver.find_element(By.XPATH, Locator.go_button).click()
    time.sleep(1)
    assert "Success" in driver.find_element(By.XPATH, Locator.success_msg).text


def test_failure_message():
    time.sleep(2)
    driver.find_element(By.XPATH, Locator.username).clear()
    driver.find_element(By.XPATH, Locator.username).send_keys("-1")
    driver.find_element(By.XPATH, Locator.go_button).click()
    time.sleep(1)
    assert "not found" in driver.find_element(By.XPATH, Locator.failure_msg).text


def teardown_module():
    driver.quit()
