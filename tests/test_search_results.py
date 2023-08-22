from selenium import webdriver
from pages.homepage import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


def setup_module():
    driver.get("http://localhost:3000/")
    time.sleep(5)


def test_search_results_repo_info_is_displayed():
    driver.find_element(By.XPATH, Locator.username).send_keys("fear")
    driver.find_element(By.XPATH, Locator.go_button).click()
    time.sleep(2)
    assert "betaflight" in driver.find_element(By.XPATH, Locator.repo_name).text
    assert "betaflight" in driver.find_element(By.XPATH, Locator.repo_name).get_attribute('href')
    assert "Open Source" in driver.find_element(By.XPATH, Locator.repo_description).text


def test_search_results_repo_no_info_displayed():
    driver.find_element(By.XPATH, Locator.username).clear()
    driver.find_element(By.XPATH, Locator.username).send_keys("android")
    driver.find_element(By.XPATH, Locator.go_button).click()
    time.sleep(2)
    assert ".allstar" in driver.find_element(By.XPATH, Locator.repo_name).text
    assert "allstar" in driver.find_element(By.XPATH, Locator.repo_name).get_attribute('href')
    assert "–" in driver.find_element(By.XPATH, Locator.repo_description).text


def teardown_module():
    driver.quit()
