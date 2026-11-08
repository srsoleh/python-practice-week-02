from enum import StrEnum, auto


class PaymentMethod(StrEnum):
    CASH = auto()
    CARD = auto()
    BANK_TRANSFER = auto()


for op in PaymentMethod:
    print(op)
print(PaymentMethod.CARD == "card")
