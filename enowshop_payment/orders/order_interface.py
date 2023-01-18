from abc import ABCMeta, abstractmethod
from typing import Dict


class IOrder(metaclass=ABCMeta):
    @abstractmethod
    def create_order(self, order_data: Dict):
        raise NotImplementedError

    def get_order(self, order_id: int):
        raise NotImplementedError
