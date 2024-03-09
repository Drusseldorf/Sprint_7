import requests
import random
import string
import json

from data import Url


class Generator:

    @staticmethod
    def login_and_password(length=10):

        def generate_random_string():
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for _ in range(length))
            return random_string

        login = generate_random_string()
        password = generate_random_string()

        return login, password


class Courier:

    @staticmethod
    def register_courier(login=None, password=None, firstName=None):

        body = {}

        if firstName:
            body["firstName"] = firstName
        if login:
            body["login"] = login
        if password:
            body["password"] = password

        response = requests.post(url=Url.REGISTER_COURIER, data=body)

        return response

    @staticmethod
    def login_courier(login=None, password=None):

        body = {}

        if login:
            body["login"] = login
        if password:
            body["password"] = password

        response = requests.post(url=Url.LOGIN_COURIER, data=body)

        return response

    @staticmethod
    def register_and_login():

        login, password = Generator.login_and_password()

        Courier.register_courier(login, password)
        login_result = Courier.login_courier(login, password)

        if login_result.status_code == 200:
            return login_result.json()['id'], login, password
        else:
            return False

    @staticmethod
    def delete_courier(courier_id):
        response = requests.delete(url=Url.DELETE_COURIER+str(courier_id))
        return response


class Order:

    @staticmethod
    def make_order(order_data):

        response = requests.post(url=Url.MAKE_ORDER, data=json.dumps(order_data))

        return response

    @staticmethod
    def get_orders():

        response = requests.get(url=Url.MAKE_ORDER)

        return response




