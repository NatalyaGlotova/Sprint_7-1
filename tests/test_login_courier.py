import allure
import pytest

from pages import CourierPage
from data import *


class TestLoginCourier:
    

    @allure.title("курьер может авторизоваться, успешный запрос возвращает id")
    def test_login_courier_success(self,valid_log_in_payload):
        response = CourierPage.log_in_courier(valid_log_in_payload)
        assert response.status_code == HTTP_STATUS_OK and response.json()["id"]

    @pytest.mark.parametrize('remove_fields', ['login', 'password'])
    @allure.title("для авторизации нужно передать все обязательные поля, проверка поля: {remove_fields}")
    @allure.description("если какого-то поля нет, запрос возвращает ошибку")
    def test_remove_fields_login_courier_error_missing(self,courier_credentials, remove_fields):
        # Удаление одного из полей запроса
        courier_credentials.pop(remove_fields)
        response = CourierPage.log_in_courier(courier_credentials)
        assert response.status_code == HTTP_STATUS_BAD_REQUEST and response.json()["message"] == ERROR_MESSAGE_MISSING_FIELDS_LOG_IN_COURIER

    @pytest.mark.parametrize('invalid_data_fields', ['login', 'password'])
    @allure.title("система вернёт ошибку, если неправильно указать поле: {invalid_data_fields}")
    @allure.description("если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_invalid_data_login_courier_error_not_found(self,courier_credentials, invalid_data_fields):
        # Удаление одного из полей запроса
        courier_credentials[invalid_data_fields] = 'неверный логин/пароль'
        response = CourierPage.log_in_courier(courier_credentials)
        assert response.status_code == HTTP_STATUS_NOT_FOUND and response.json()["message"] == ERROR_MESSAGE_NOT_FOUND
