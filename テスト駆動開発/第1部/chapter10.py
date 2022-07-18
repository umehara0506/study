"""P72
"""

from __future__ import annotations
from abc import abstractmethod
from functools import total_ordering


@total_ordering
class Money:

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    @staticmethod
    def dollar(amount: int) -> Dollar:
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> Franc:
        return Franc(amount, 'CHF')

    def __eq__(self, other: Money) -> bool:

        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを引数にしてください。')
        return (self._amount == other._amount) and (self._currency == other._currency)

    def __lt__(self, other: Money) -> bool:
        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを引数にしてください。')
        return (self._amount > other._amount) and (self._currency == other._currency)


class Dollar(Money):

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)


class Franc(Money):

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)


class MoneyTest:

    @staticmethod
    def test_multiplication():
        five = Money.dollar(5)
        product = five.times(2)
        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    @staticmethod
    def test_equality():
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        
        assert Money.franc(5) == Money.franc(5)
        assert Money.franc(5) != Money.franc(6)

        assert Money.franc(5) != Money.dollar(6)

    @staticmethod
    def test_franc_multiplication():
        five = Money.franc(5)
        product = five.times(2)
        assert Money.franc(10) == five.times(2)
        assert Money.franc(15) == five.times(3)

    @staticmethod
    def test_currency():
        assert 'USD' == Money.dollar(1).currency()
        assert 'CHF' == Money.franc(1).currency()

    @staticmethod
    def test_different_class_equality():
        assert Money(10, 'CHF') == Franc(10, 'CHF')

MoneyTest.test_multiplication()
MoneyTest.test_equality()
MoneyTest.test_franc_multiplication()
MoneyTest.test_currency()
MoneyTest.test_different_class_equality()
