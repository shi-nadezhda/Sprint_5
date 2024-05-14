from selenium.webdriver.common.by import By

class Urls:
    """URL"""
    base_url = "https://stellarburgers.nomoreparties.site/"
    login_url = base_url + "login"
    register_url = base_url + "register"
    forgot_password_url = base_url + "forgot-password"
    profile_url = base_url + "account/profile"
    
class Header:
    """Шапка страницы"""
    page_title_button = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # заголовок страницы
    constructor_button = (By.XPATH, ".//p[text()='Конструктор']") # кнопка "Конструктор"
    order_feed_button = (By.XPATH, ".//p[text()='Лента Заказов']") # кнопка "Лента заказов"
    profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']") # кнопка "Личный кабинет"

class BuilderPage:
    """Страница с конструктором"""
    url = Urls.base_url
    buns_tab = (By.XPATH, ".//span[text()='Булки']") # Раздел "Булки"
    sauce_tab = (By.XPATH, ".//span[text()='Соусы']") # Раздел "Соусы"
    filling_tab = (By.XPATH, ".//span[text()='Начинки']") # Раздел "Начинки"
    current_tab = (By.XPATH, ".//div[contains(@class, 'tab_tab') and contains(@class, 'current')]/span") # активная вкладка
    login_account_button = (By.XPATH, ".//button[text()='Войти в аккаунт']") # кнопка "Войти в аккаунт"
    checkout_button = (By.XPATH, ".//button[text()='Оформить заказ']") # кнопка "Оформить заказ"

class RegisterPage:
    """Форма регистрации"""
    url = Urls.register_url
    name_input = (By.XPATH, ".//label[text()='Имя']/parent::*//input") # поле ввода имени
    email_input = (By.XPATH, ".//label[text()='Email']/parent::*//input") # поле ввода email
    password_input = (By.XPATH, ".//label[text()='Пароль']/parent::*//input") # поле ввода пароля
    register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']") # кнопка "Зарегистрироваться"
    error_incorrect_password = (By.XPATH, ".//p[text()='Некорректный пароль']") # ошибка для некорректного пароля
    login_link = (By.XPATH, ".//a[text()='Войти']") # ссылка "Войти"
        
class LoginPage:    
    """Форма входа"""
    url = Urls.login_url
    email_input = (By.XPATH, ".//label[text()='Email']/parent::*//input") # поле ввода email
    password_input = (By.XPATH, ".//label[text()='Пароль']/parent::*//input") # поле ввода пароля
    login_button = (By.XPATH, ".//button[text()='Войти']") # кнопка "Войти"
    register_link = (By.XPATH, ".//a[text()='Зарегистрироваться']") # ссылка "Зарегистрироваться"
    restore_password_link = (By.XPATH, ".//a[text()='Восстановить пароль']") # ссылка "Восстановить пароль"
    
class ProfilePage:
    """Личный кабинет"""
    url = Urls.profile_url   
    exit_button = (By.XPATH, ".//button[text()='Выход']") # кнопка "Выход"

class ForgotPasswordPage:
    """Страница восстановления пароля"""
    url = Urls.forgot_password_url
    login_link = (By.XPATH, ".//a[text()='Войти']") # ссылка "Войти"