from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait 
from locators import Urls, BuilderPage

class TestBuilder:
    def test_bun_tab_is_clicked_and_available(self, driver):
        # Проверяем переход в раздел "Булки"
        driver.get(Urls.base_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BuilderPage.sauce_tab))
        driver.find_element(*BuilderPage.sauce_tab).click()
        driver.find_element(*BuilderPage.buns_tab).click()

        current_tab = driver.find_element(*BuilderPage.current_tab)
        assert current_tab.text == 'Булки'
    
    
    def test_sauce_tab_is_clicked_and_available(self, driver):
        # Проверяем переход в раздел "Соусы"
        driver.get(Urls.base_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BuilderPage.sauce_tab))
        driver.find_element(*BuilderPage.sauce_tab).click()

        current_tab = driver.find_element(*BuilderPage.current_tab)
        assert current_tab.text == 'Соусы'


    def test_filling_tab_is_clicked_and_available(self, driver):
        # Проверяем переход в раздел "Начинки"
        driver.get(Urls.base_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BuilderPage.filling_tab))
        driver.find_element(*BuilderPage.filling_tab).click()

        current_tab = driver.find_element(*BuilderPage.current_tab)
        assert current_tab.text == 'Начинки'
