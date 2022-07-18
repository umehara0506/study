"""P41
"""

from __future__ import annotations
from functools import total_ordering

@total_ordering
class Money:

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier)

    def __eq__(self, other: Money) -> bool:
        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを引数にしてください。')
        return self._amount == other._amount

    def __lt__(self, other: Money) -> bool:
        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを引数にしてください。')
        return self._amount > other._amount


class Dollar(Money):

    def __init__(self, amount: int) -> None:
        super().__init__(amount)

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)


class Franc(Money):

    def __init__(self, amount: int) -> None:
        super().__init__(amount)

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)


class MoneyTest:

    @staticmethod
    def test_multiplication():
        five = Dollar(5)
        product = five.times(2)
        assert Dollar(10) == five.times(2)
        assert Dollar(15) == five.times(3)

    @staticmethod
    def test_equality():
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)

    @staticmethod
    def test_franc_multiplication():
        five = Franc(5)
        product = five.times(2)
        assert Franc(10) == five.times(2)
        assert Franc(15) == five.times(3)

MoneyTest.test_multiplication()
MoneyTest.test_equality()
MoneyTest.test_franc_multiplication()