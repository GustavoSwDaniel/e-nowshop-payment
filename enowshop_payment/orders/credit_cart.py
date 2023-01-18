from abc import ABC
from typing import Dict

from enowshop_payment.orders.order_interface import IOrder


class CreditCardPayment(IOrder, ABC):
    def __init__(self):
        ...

    def create_order(self, order_data: Dict):
        raise NotImplementedError

    def get_order(self, order_id: int):
        raise NotImplementedError
