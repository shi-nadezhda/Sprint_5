from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait 
from locators import Header, ProfilePage, LoginPage
from data import Urls

class TestProfile:
    def test_unauthorise_profile_open_login_redirect_success(self, driver):
        # Проверяем редирект неавторизованного пользователя на страницу логина по клику на кнопку "Личный кабинет"
        driver.get(Urls.base_url)
        driver.find_element(*Header.profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains(LoginPage.url))

        assert driver.current_url == LoginPage.url
        

    def test_authorise_profile_open_success(self, driver, login):        
        # Проверяем переход авторизованного пользователя в личный кабинет по клику на кнопку "Личный кабинет"
        driver.find_element(*Header.profile_button).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(ProfilePage.exit_button))
        driver.find_element(*Header.profile_button).click()
        WebDriverWait(driver, 20).until(expected_conditions.url_contains(ProfilePage.url))

        assert driver.current_url == ProfilePage.url


    def test_builder_click_constructor_button_open_success(self, driver, login):
        # Проверяем переход из личного кабинета в конструктор по клику "Конструктор"
        driver.find_element(*Header.profile_button).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(ProfilePage.exit_button))
        driver.find_element(*Header.constructor_button).click()
        WebDriverWait(driver, 20).until(expected_conditions.url_contains(Urls.base_url))

        assert driver.current_url == Urls.base_url


    def test_builder_click_page_title_button_open_success(self, driver, login):
        # Проверяем переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
        driver.find_element(*Header.profile_button).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(ProfilePage.exit_button))
        driver.find_element(*Header.page_title_button).click() 

        assert driver.current_url == Urls.base_url


    def test_logout_click_exit_button_success(self, driver, login):
        # Проверяем выход из аккаунта при клике на кнопку "Выйти" в личном кабинете
        driver.find_element(*Header.profile_button).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(ProfilePage.exit_button))
        driver.find_element(*ProfilePage.exit_button).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(LoginPage.login_button))

        login_button_on_display = driver.find_element(*LoginPage.login_button).is_displayed()
        assert driver.current_url == Urls.login_url and login_button_on_display
