from selenium import webdriver
from selenium.webdriver.common.by import By
from auto.myData import LOGIN, PASSWORD, MAIN_PAGE, CURRENT_URL
from auto.myLocator import *
from auto.Selectors import *

import time
driver = webdriver.Chrome()

def test_logout():
    driver.get(MAIN_PAGE)

    url_before = driver.current_url

    username_field = driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    password_field = driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    burger_menu = driver.find_element(By.ID, BURGER_MENU)
    burger_menu.click()
    time.sleep(6)

    logout = driver.find_element(By.CSS_SELECTOR, LOGOUT)
    logout.click()

    time.sleep(5)

    url_after = driver.current_url

    assert(url_before == url_after)