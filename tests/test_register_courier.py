import allure

from helpers.helpers import Courier, Generator
from data import ErrorMessage


class TestRegisterCourier:

    @allure.title('Тест возможности пройти регистрацию курьера')
    def test_registration_is_possible(self):

        login, password = Generator.login_and_password()

        response = Courier.register_courier(login, password)

        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Тест корректного поведения при создании двух одинаковых логинов курьера')
    def test_register_two_identical_login(self):

        login, password = Generator.login_and_password()
        Courier.register_courier(login, password)

        response = Courier.register_courier(login, password)

        assert response.json()['message'] == ErrorMessage.LOGIN_ALREADY_EXISTS and response.status_code == 409

    @allure.title('Тест поведения при регистрации без передачи логина')
    def test_register_without_login(self):

        password = Generator.login_and_password()[1]

        response = Courier.register_courier(password=password)

        assert response.json()['message'] == ErrorMessage.NOT_ENOUGH_DATA_TO_REG and response.status_code == 400
