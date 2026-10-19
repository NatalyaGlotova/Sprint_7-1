import allure
import pytest

from pages import CourierPage
from data import *


class TestCreateCourier:

    @allure.title("курьера можно создать, запрос возвращает правильный код ответа")
    def test_create_courier_success(self, valid_courier_payload):
        response  = CourierPage.create_courier(valid_courier_payload)
        assert response.status_code == HTTP_STATUS_CREATED and response.text == BASE_SUCCESSFUL_BODY

    @allure.title("нельзя создать двух одинаковых курьеров")
    @allure.description("если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_create_courier_duplicate_error_message(self, valid_courier_payload):
        CourierPage.create_courier(valid_courier_payload)
        response_courier_duplicate = CourierPage.create_courier(valid_courier_payload)
        assert response_courier_duplicate.status_code == HTTP_STATUS_CONFLICT and response_courier_duplicate.json()["message"] == ERROR_MESSAGE_LOGIN_DUPLICATE

    @pytest.mark.parametrize('remove_fields', ['login', 'password', 'firstName'])
    @allure.title("чтобы создать курьера, нужно передать в ручку все обязательные поля, проверка поля: {remove_fields}")
    @allure.description("если одного из полей нет, запрос возвращает ошибку")
    def test_create_remove_fields_courier_error_missing(self, valid_courier_payload, remove_fields):
        # Удаление одного из полей запроса
        valid_courier_payload.pop(remove_fields)
        response  = CourierPage.create_courier(valid_courier_payload)
        assert response.status_code == HTTP_STATUS_BAD_REQUEST and response.json()["message"] == ERROR_MESSAGE_MISSING_FIELDS_CREATE_COURIER
