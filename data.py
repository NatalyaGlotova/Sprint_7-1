# Успешный запрос возвращает
from datetime import datetime, timedelta

BASE_SUCCESSFUL_BODY = '{"ok":true}'

# Ожидаемые статусы для различных сценариев
HTTP_STATUS_OK = 200           # универсальный статус удачного запроса
HTTP_STATUS_CREATED = 201      # статус создания новых записей
HTTP_STATUS_CONFLICT = 409     # статус 409 для конфликтов
HTTP_STATUS_BAD_REQUEST = 400  # только статус 400 для некорректных запросов
HTTP_STATUS_NOT_FOUND = 404   # статус 404 для "не найдено"

# Сообщения об ошибках
ERROR_MESSAGE_LOGIN_DUPLICATE = "Этот логин уже используется."
ERROR_MESSAGE_MISSING_FIELDS_CREATE_COURIER = "Недостаточно данных для создания учетной записи"
ERROR_MESSAGE_MISSING_FIELDS_LOG_IN_COURIER = "Недостаточно данных для входа"
ERROR_MESSAGE_NOT_FOUND = "Учетная запись не найдена"

# Тестовые данные заказа
VALID_ORDER_PAYLOAD = {
    "firstName": "Наталья",
    "lastName": "Глотова",
    "address": "Обнинск, проспект Маркса, 8",
    "metroStation": "2",
    "phone": "+79996663322",
    "rentTime": 3,
    "deliveryDate": datetime.now()  + timedelta(days=1),
    "comment": "Код домофина 39",
}
