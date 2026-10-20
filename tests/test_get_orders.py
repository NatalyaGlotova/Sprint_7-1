import allure

from pages import OrderPage
from data import *


class TestGETOrder:

    @allure.title("Проверь, что в тело ответа возвращается список заказов.")
    def test_get_courier_id_orders_list_all_orders(self):
        response  = OrderPage.get_all_orders()
        assert response.status_code == HTTP_STATUS_OK and len(response.json()["orders"]) > 0
