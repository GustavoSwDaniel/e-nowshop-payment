from abc import ABCMeta, abstractmethod


class IPayment(metaclass=ABCMeta):
    @abstractmethod
    def create_order(self, order_data):
        raise NotImplementedError
    
    @abstractmethod
    def get_order_by_uuid(self, order_uuid: str):
        raise NotImplementedError

    @abstractmethod
    def cancel_order(self, order_uuid: str):
        raise NotImplementedError
    