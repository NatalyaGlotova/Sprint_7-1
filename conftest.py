import random
import string
import requests
import pytest

from pages import CourierPage
from courier import *

@pytest.fixture
# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def valid_courier_payload():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    len_random = 100
    login = generate_random_string(len_random)
    password = generate_random_string(len_random)
    first_name = generate_random_string(len_random)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # тела запроса для регистрации
    return payload

@pytest.fixture
def valid_log_in_payload(valid_courier_payload):
    CourierPage.create_courier(valid_courier_payload)
    login_payload = {
        "login": valid_courier_payload["login"],
        "password": valid_courier_payload["password"],
    }
    return login_payload


# 2. Фикстура с автоматическим удалением
@pytest.fixture
def courier_setup():
    # Создаем курьера перед тестом
    courier_data = register_new_courier_and_return_login_password()
    
    yield courier_data  # Передаем список в тест

    # Код ниже выполнится строго ПОСЛЕ теста:
    # 1. Узнаем ID курьера через логин
    login_payload = {"login": courier_data[0], "password": courier_data[1]}
    login_response = requests.post('COURIER_LOGIN_URL', json=login_payload)
    courier_id = login_response.json()["id"]
    
    # 2. Удаляем курьера по его ID
    requests.delete(f'https://praktikum-services.ru/{courier_id}')