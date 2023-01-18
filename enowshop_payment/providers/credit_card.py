from abc import abstractmethod

from enowshop_payment.providers.payment_interface import IPayment


class CreditCard(IPayment):
    @abstractmethod
    def create_order(self, order_data):
        raise NotImplementedError

    @abstractmethod
    def get_order_by_uuid(self, order_uuid: str):
        raise NotImplementedError

    @abstractmethod
    def cancel_order(self, order_uuid: str):
        raise NotImplementedError
