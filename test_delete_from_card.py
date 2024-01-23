from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from auto.myData import LOGIN, PASSWORD, MAIN_PAGE
from auto.myLocator import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from auto.Selectors import *
driver = webdriver.Chrome()

def test_delete_from_card():
    driver.get(MAIN_PAGE)

    username_field = driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    password_field = driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    button = driver.find_element(By.CSS_SELECTOR, BUTTON_ADD_TO_CARD).click()

    time.sleep(4)

    card = driver.find_element(By.CSS_SELECTOR, CARD)
    card.click()

    time.sleep(4)

    button_remove = driver.find_element(By.CSS_SELECTOR,REMOVE_FROM_CARD)
    button_remove.click()
    time.sleep(4)

    time.sleep(3)
    assert(driver.find_element(By.CSS_SELECTOR,BUTTON_CHECKOUT))

