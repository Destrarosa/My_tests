from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from auto.myData import LOGIN, PASSWORD, MAIN_PAGE, CURRENT_URL
from auto.myLocator import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from auto.mySelectors import NAME_OF_PICTURE
driver = webdriver.Chrome()
def test_click_name():
    driver.get(MAIN_PAGE)

    password_field = driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    username_field = driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    login_button = driver.find_element(By.XPATH, LOGIN_BUTTON).click()


    text_before = driver.find_element(By.CSS_SELECTOR,NAME_OF_PICTURE)
    text_before.click()
    time.sleep(4)
    assert driver.current_url == CURRENT_URL
