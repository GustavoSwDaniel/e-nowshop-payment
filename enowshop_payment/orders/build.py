from enowshop_payment.orders.credit_cart import CreditCardPayment
from enowshop_payment.orders.order_interface import IOrder
from enowshop_payment.orders.pix import PixPayment


class BuildPayment:
    def __init__(self, payment_type: str):
        self.payment_type = payment_type

    def build_payment(self) -> IOrder:
        payments = {
            'CREDIT_CART': CreditCardPayment,
            'PIX': PixPayment
        }
        return payments[self.payment_type]()
