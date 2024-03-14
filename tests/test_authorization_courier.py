import allure

from helpers.helpers import Courier
from data import ErrorMessage


class TestAuthorizationCourier:

    courier_id = None
    login = None
    password = None

    @classmethod
    def setup_class(cls):
        cls.courier_id, cls.login, cls.password = Courier().register_and_login()

    @allure.title('Тест возможности пройти авторизацию курьера')
    def test_authorization_is_possible(self):

        result = Courier.login_courier(self.login, self.password)

        assert result.status_code == 200 and 'id' in result.text

    @allure.title('Тест поведения при авторизации без логина')
    def test_authorization_without_login(self):

        result = Courier.login_courier(password=self.password)

        assert result.json()['message'] == ErrorMessage.NOT_ENOUGH_DATA_TO_LOGIN and result.status_code == 400

    @allure.title('Тест поведения при авторизации c некорректным паролем')
    def test_authorization_with_wrong_password(self):

        result = Courier.login_courier(login=self.login, password=self.password + 'oops')

        assert result.json()['message'] == ErrorMessage.WRONG_AUTH_DATA and result.status_code == 404

    @allure.title('Тест авторизации с некорректным логином')
    def test_authorization_with_wrong_login(self):

        result = Courier.login_courier(login=self.login + 'oops', password=self.password)

        assert result.json()['message'] == ErrorMessage.WRONG_AUTH_DATA and result.status_code == 404

    @allure.title('Тест получения id при успешной авторизации')
    def test_authorization_return_id(self):

        result = Courier.login_courier(self.login, self.password)

        assert 'id' in result.text and result.status_code == 200

    @classmethod
    def teardown_class(cls):
        Courier.delete_courier(cls.courier_id)
