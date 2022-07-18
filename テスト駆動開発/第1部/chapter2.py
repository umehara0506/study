"""P16
from __future__ import annotationsでクラスのアノテーションを使えるようにしています。
"""


from __future__ import annotations
from functools import total_ordering

@total_ordering
class Dollar:

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)

    def __eq__(self, other: int) -> bool:
        return self.amount == other

    def __lt__(self, other: int) -> bool:
        return self.amount > other


class MoneyTest:

    @staticmethod
    def test_multiplication():
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount

        product = five.times(3)
        assert 15 == product.amount


MoneyTest.test_multiplication()