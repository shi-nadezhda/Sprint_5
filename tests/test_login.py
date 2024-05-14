from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait 
from locators import RegisterPage, BuilderPage, Urls, Header, LoginPage, ForgotPasswordPage
from conftest import User


class TestLogin:
    def test_login_click_login_account_button_main_page_success(self, driver):
        # Выполняем вход по кнопке "Войти в аккаунт на главной"
        driver.get(Urls.base_url)
        driver.find_element(*BuilderPage.login_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains(LoginPage.url))
        
        assert driver.current_url == LoginPage.url


    def test_login_click_personal_account_button_success(self, driver):    
        # Выполняем вход через кнопку "Личный кабинет"
        driver.get(Urls.base_url)
        driver.find_element(*Header.profile_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains(LoginPage.url))
        
        assert driver.current_url == LoginPage.url


    def test_login_click_login_link_success(self, driver): 
        # Выполняем вход через кнопку в форме регистрации
        driver.get(Urls.register_url)
        driver.find_element(*RegisterPage.login_link).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains(LoginPage.url))

        assert driver.current_url == LoginPage.url


    def test_login_click_login_link_success(self, driver): 
        # Выполняем вход через кнопку в форме восстановления пароля
        driver.get(Urls.forgot_password_url)
        driver.find_element(*ForgotPasswordPage.login_link).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains(LoginPage.url))

        assert driver.current_url == LoginPage.url


    def test_login_success(self, driver):
        # Выполняем авторизацию
        driver.get(Urls.login_url)
        driver.find_element(*LoginPage.email_input).send_keys(User.email)
        driver.find_element(*LoginPage.password_input).send_keys(User.password)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BuilderPage.checkout_button))
        checkout_button_on_display = driver.find_element(*BuilderPage.checkout_button).is_displayed()

        assert driver.current_url == BuilderPage.url and checkout_button_on_display
