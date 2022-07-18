"""P23
__eq__の仮引数をDollarクラスへ変更
pythonの場合は型制限ができないのでisinstanceで型チェックを追加
"""

from __future__ import annotations
from functools import total_ordering

@total_ordering
class Dollar:

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)

    def __eq__(self, other: Dollar) -> bool:
        if not isinstance(other, Dollar):
            raise TypeError('Dollarクラスを引数にしてください。')
        return self.amount == other.amount

    def __lt__(self, other: Dollar) -> bool:
        if not isinstance(other, Dollar):
            raise TypeError('Dollarクラスを引数にしてください。')
        return self.amount > other.amount

class MoneyTest:

    @staticmethod
    def test_multiplication():
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount

        product = five.times(3)
        assert 15 == product.amount

    @staticmethod
    def test_equality():
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)

MoneyTest.test_multiplication()
MoneyTest.test_equality()