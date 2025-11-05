#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0, total=0, items=None, previous_transactions=None):
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []
        self.previous_transactions = (
            previous_transactions if previous_transactions is not None else []
        )


@property
def discount(self):
    return self._discount


@discount.setter
def discount(self, value):
    if isinstance(value, int) and value >= 0:
        self._discount = value
    else:
        raise ValueError("Discount must be a non-negative integer")


def add_item(self, title, price, qty):
    self.total += price * qty
    self.items.append(title)
    self.previous_transactions.append({"title": title, "price": price, "qty": qty})
