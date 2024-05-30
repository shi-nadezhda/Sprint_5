# Тесты для сайта Stellar Burgers.
https://stellarburgers.nomoreparties.site

## Структура
- tests/ - автотесты
    - test_builder.py - тесты раздела "Конструктор"
    - test_login.py - тесты для авторизации
    - test_profile.py - тесты личного кабинета
    - test_register.py - тесты для регистрации
- conftest.py - фикстуры
- locators.py - локаторы
- user.py - пользователи для авторизации и регистрации
- data.py - данные

### Запуск тестов: 
`pytest -v`