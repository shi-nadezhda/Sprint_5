import random

class User:
    name = "Nadezhda_8"
    email = "nadezhda_atmozhitova_8_999@yandex.ru"
    password = "atmozhitova_8"
    
class RandomUser:
    user_name = f'Test Name {random.randint(0, 999)}'
    email = f'testmail{random.randint(0, 999)}@yandex.com'
    password = f'pass{random.randint(1000, 9999)}'