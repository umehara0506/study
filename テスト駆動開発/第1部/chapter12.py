"""P87
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from functools import total_ordering


class Expression(ABC):
    pass


class Bank:
    
    def reduce(self, source: Expression, to: str) -> Money:
        return Money.dollar(10)


@total_ordering
class Money(Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def plus(self, addend: Money) -> Money:
        if not isinstance(addend, Money):
            TypeError('Moneyクラスを引数にしてください。')
        return Money(self._amount + addend._amount, self.currency)

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, 'CHF')

    def __eq__(self, other: Money) -> bool:

        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを引数にしてください。')
        return (self._amount == other._amount) and (self._currency == other._currency)

    def __lt__(self, other: Money) -> bool:
        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを引数にしてください。')
        return (self._amount > other._amount) and (self._currency == other._currency)


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

        assert Money.franc(5) != Money.dollar(6)

    @staticmethod
    def test_currency():
        assert 'USD' == Money.dollar(1).currency()
        assert 'CHF' == Money.franc(1).currency()

    @staticmethod
    def test_simple_addition():
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, 'USD')
        assert Money.dollar(10) == reduced


MoneyTest.test_multiplication()
MoneyTest.test_equality()
MoneyTest.test_currency()
MoneyTest.test_simple_addition()