import json
import logging
import uuid
from abc import ABC
from typing import Dict

import requests

from enowshop_payment.exceptions import PaymentException
from enowshop_payment.providers.payment_interface import IPayment


class Pix(IPayment, ABC):
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.pix_mercado_pago_url =  'https://api.mercadopago.com'
        self.__headers = {
          'Content-Type': 'application/json'
        }

    def create_order(self, order_data, access_key: str) -> Dict:
        self.__headers['Authorization'] = 'Bearer ' + access_key
        order = {
            "transaction_amount": order_data['total_value'],
            "description": "Título do produto",
            "external_reference": str(uuid.uuid4()),
            "payment_method_id": "pix",
            "payer": {
                "email": order_data['user_info']['email'],
                "first_name": order_data['user_info']['first_name'],
                "last_name": order_data['user_info']['last_name'],
            }

        }

        url = f'{self.pix_mercado_pago_url}/v1/payments'

        response = requests.post(url, headers=self.__headers, data=json.dumps(order))

        if response.status_code != 201:
            self.logger.info(f"Error in create order")
            raise PaymentException('Error in create order' + response.text)

        return response.json()

    def get_order_by_uuid(self, order_id: int) -> Dict:
        url = f'{self.pix_mercado_pago_url}/v1/payments/{order_id}'
        response = requests.get(url, headers=self.__headers)

        if response.status_code != 200:
            self.logger.info(f"Order does not found - order uuid [{order_id}]")
            raise PaymentException('Order does not found' + response.text)

        return response.json()

    def cancel_order(self, order_id: int) -> Dict:
        url = f'{self.pix_mercado_pago_url}/{order_id}'
        response = requests.post(url, headers=self.__headers,
                                 data=json.dumps({'status': 'cancelled'}))

        if response.status_code != 200:
            self.logger.info(f"Error in cancel order - order uuid [{order_id}]")
            raise PaymentException('Error in cancel order' + response.text)

        return response.json()

    def refund_order(self, order_id: int, value: int) -> Dict:
        url = f'{self.pix_mercado_pago_url}/v1/payments/{order_id}/refunds'

        response = requests.post(url, headers=self.__headers,
                                 data=json.dumps({'amount': value}))

        if response.status_code != 200:
            self.logger.info(f"Error in refund order - order uuid [{order_id}]")
            raise PaymentException('Error in refund order' + response.text)

        return response.json()