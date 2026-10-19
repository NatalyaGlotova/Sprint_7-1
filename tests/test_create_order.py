import allure
import pytest

from pages import OrderPage
from data import *


class TestCreateOrderColors:

    @pytest.mark.parametrize(
        "colors",
        [["BLACK"], ["GREY"], ["BLACK", "GREY"], None],
    )
    @allure.title("возможность создать заказ с выбором цвета, тело ответа содержит track")
    @allure.description("можно указать один из цветов — BLACK или GREY; можно указать оба цвета; можно совсем не указывать цвет;")
    def test_create_order_with_colors(self, colors):
        payload = VALID_ORDER_PAYLOAD.copy()
        payload["color"] = colors
        response  = OrderPage.create_order(VALID_ORDER_PAYLOAD)
        assert response.status_code == HTTP_STATUS_CREATED and response.json()["track"]


    @allure.title("возможность создать заказ без выбора цвета, тело ответа содержит track")
    def test_create_order_without_field_color(self):
        response  = OrderPage.create_order(VALID_ORDER_PAYLOAD)
        assert response.status_code == HTTP_STATUS_CREATED and response.json()["track"]
