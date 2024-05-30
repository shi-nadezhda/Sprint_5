import pytest
from selenium import webdriver
from user import User
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait 
from locators import LoginPage, BuilderPage
from data import Urls



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    # Авторизация
    driver.get(LoginPage.url)
    driver.find_element(*LoginPage.email_input).send_keys(User.email)
    driver.find_element(*LoginPage.password_input).send_keys(User.password)
    driver.find_element(*LoginPage.login_button).click()
    WebDriverWait(driver, 20).until(expected_conditions.url_contains(Urls.base_url))
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BuilderPage.checkout_button))
