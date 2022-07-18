"""P119
MoneyクラスからExpressionに色々変えたけどよくわかっていないです。
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from functools import total_ordering


class Expression(ABC):
    
    @abstractmethod
    def plus(self, to: str):
        pass
    
    @abstractmethod
    def reduce(self, to: str):
        pass


class Bank:

    def __init__(self):
        self._rates = {}
    
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def addRate(self, _from: str, to: str, rate: int) -> None:
        self._rates[Pair(_from, to)] = rate
    
    def rate(self, _from: str, to: str) -> int:
        if _from == to:
            return 1
        return self._rates.get(Pair(_from, to))


class Sum(Expression):

    def __init__(self, augend: Expression, addend: Expression) -> None:
        self._augend = augend
        self._addend = addend

    def plus(self, addend: Exception) -> Exception:
        return None

    def reduce(self, bank: Bank, to: str) -> Money:
        amount = self._augend.reduce(bank, to)._amount  + self._addend.reduce(bank, to)._amount
        return Money(amount, to)


class Money(Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def plus(self, addend: Expression) -> Expression:
        if not isinstance(addend, Money):
            TypeError('Moneyクラスを引数にしてください。')
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str) -> Money:
        rate = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)

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


class Pair:

    def __init__(self, _from: str, to: str) -> str:
        self._from = _from
        self._to = to

    def __eq__(self, other: Pair) -> bool:
        return (self._from == other._from) and (self._to == other._to)

    def __hash__(self) -> int:
        return 0


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

    @staticmethod
    def test_plus_returns_sum():
        five = Money.dollar(5)
        result = five.plus(five)
        assert five == result._augend
        assert five == result._addend

    @staticmethod
    def test_reduce_sum():
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, 'USD')
        assert Money.dollar(7) == result

    @staticmethod
    def test_reduce_money():
        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        assert Money.dollar(1) == result

    @staticmethod
    def test_reduce_money_different_currency():
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        assert Money.dollar(1) == result

    @staticmethod
    def test_array_equals():
        assert 1 == Bank().rate('USD', 'USD')

    @staticmethod
    def test_mixed_addition():
        fiveBuckes: Expression = Money.dollar(5)
        tenFrances: Expression = Money.franc(10)
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        result = bank.reduce(fiveBuckes.plus(tenFrances), 'USD')
        assert Money.dollar(10) == result

MoneyTest.test_multiplication()
MoneyTest.test_equality()
MoneyTest.test_currency()
MoneyTest.test_simple_addition()
MoneyTest.test_plus_returns_sum()
MoneyTest.test_reduce_sum()
MoneyTest.test_reduce_money()
MoneyTest.test_reduce_money_different_currency()
MoneyTest.test_array_equals()
MoneyTest.test_mixed_addition()

