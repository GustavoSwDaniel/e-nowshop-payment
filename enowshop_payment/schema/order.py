import enum
from dataclasses import dataclass
from typing import Union


@dataclass
class OrderPixCreated:
    id: [int, None]
    qrcode_text: Union[str, None]
    qrcode: Union[str, None]
    instalments: Union[int, None]

    def __post_init__(self):
        self.qrcode = 'data:image/png;base64,' + self.qrcode


class CreditCard(enum.Enum):
    APPROVED = 'APPROVED'
    PENDING = 'PENDING'
    DENIED = 'DENIED'


@dataclass
class OrderCreditCardCreated:
    uuid: str
    status: CreditCard
