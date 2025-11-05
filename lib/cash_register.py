#!/usr/bin/env python3


class CashRegister:
    def __init__(
        self,
        discount=0,
    ):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and value >= 0:
            self._discount = value
        else:
            raise ValueError("Discount must be a non-negative integer")

    def add_item(self, title, price, qty=1):
        self.total += price * qty
        self.items += [title] * qty
        self.previous_transactions.append({"title": title, "price": price, "qty": qty})

    def apply_discount(
        self,
    ):
        if self.discount > 0:
            self.total = self.total * (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["qty"]

        for _ in range(last["qty"]):
            if last["title"] in self.items:
                self.items.remove(last["title"])

            if not self.items:
                self.total = 0.0
