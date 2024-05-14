from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait 

from locators import RegisterPage, Urls, LoginPage
from user import RandomUser

class TestRegister:
    def test_register_incorrect_password_error(self, driver):
        # Проверяем появление ошибки для некорректного пароля
        driver.get(Urls.register_url)
        driver.find_element(*RegisterPage.name_input).send_keys(RandomUser.user_name)
        driver.find_element(*RegisterPage.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegisterPage.password_input).send_keys('8')
        driver.find_element(*RegisterPage.register_button).click()  
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((RegisterPage.error_incorrect_password)))
        
        assert driver.find_element(*RegisterPage.error_incorrect_password)
        
        
    def test_register_success(self, driver):
        # Выполняем успешную регистрацию
        driver.get(Urls.register_url)
        driver.find_element(*RegisterPage.name_input).send_keys(RandomUser.user_name)
        driver.find_element(*RegisterPage.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegisterPage.password_input).send_keys(RandomUser.password)
        driver.find_element(*RegisterPage.register_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains(LoginPage.url))

        assert driver.current_url == LoginPage.url
