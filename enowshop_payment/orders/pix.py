from abc import ABC
from typing import Dict

from enowshop_payment.orders.order_interface import IOrder
from enowshop_payment.providers.pix import Pix
from enowshop_payment.schema.order import OrderPixCreated


class PixPayment(IOrder, ABC):
    def __init__(self):
        self.payment = Pix()

    def create_order(self, order_data: Dict):
        response = self.payment.create_order(order_data=order_data)
        return OrderPixCreated(id=response['id'],
                               qrcode_text=response['point_of_interaction']['transaction_data']['qr_code'],
                               qrcode=response['point_of_interaction']['transaction_data']['qr_code_base64'],
                               instalments=response['installments'])

    def get_order(self, order_id: int):
        raise  NotImplementedError
