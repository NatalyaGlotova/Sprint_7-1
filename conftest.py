import random
import string
import requests
import pytest

from courier import *

@pytest.fixture
def courier_credentials():
    # Фикстура сама вызывает метод и возвращает его результат [login, password]
    data = valid_courier_payload()
    return data


@pytest.fixture
def valid_log_in_payload(courier_credentials):
    CourierPage.create_courier(courier_credentials)
    login_payload = {
        "login": courier_credentials["login"],
        "password": courier_credentials["password"],
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