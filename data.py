class Url:

    HOST = 'https://qa-scooter.praktikum-services.ru'
    LOGIN_COURIER = HOST + '/api/v1/courier/login'
    REGISTER_COURIER = HOST + '/api/v1/courier'
    DELETE_COURIER = HOST + '/api/v1/courier/'
    MAKE_ORDER = HOST + '/api/v1/orders'


class ErrorMessage:

    LOGIN_ALREADY_EXISTS = 'Этот логин уже используется. Попробуйте другой.'
    NOT_ENOUGH_DATA_TO_REG = 'Недостаточно данных для создания учетной записи'
    NOT_ENOUGH_DATA_TO_LOGIN = 'Недостаточно данных для входа'
    WRONG_AUTH_DATA = 'Учетная запись не найдена'


class OrderData:

    ORDER_DATA_ONE_COLOR = {
        "firstName": "Naruto",
        "lastName": "Udzumaki",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    ORDER_DATA_TWO_COLORS = {
        "firstName": "Naruto",
        "lastName": "Udzumaki",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK", "GREY"
        ]
    }

    ORDER_DATA_WITHOUT_COLOR = {
        "firstName": "Naruto",
        "lastName": "Udzumaki",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
