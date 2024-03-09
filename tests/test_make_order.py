import pytest
import allure

from helpers.helpers import Order
from data import OrderData


class TestMakeAndGetOrders:

    @allure.title('Тест создания заказа с одним цветом, двумя цветами, без выбора цвета')
    @pytest.mark.parametrize('order_data',
                             [OrderData.ORDER_DATA_ONE_COLOR,
                              OrderData.ORDER_DATA_TWO_COLORS,
                              OrderData.ORDER_DATA_WITHOUT_COLOR])
    def test_can_choose_colors_or_no_color(self, order_data):

        response = Order.make_order(order_data)

        assert 'track' in response.text and response.status_code == 201

    @allure.title('Тест получения списка всех заказов')
    def test_get_orders(self):

        response = Order.get_orders()

        assert 'orders' in response.text and response.status_code == 200
