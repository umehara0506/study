"""P52
Factory Methodパターンを使うためにはfrom __future__ import annotationsが必要になります。
ここまででimportしていない場合も必須です。
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from functools import total_ordering


@total_ordering
class Money(ABC):

    def __init__(self, amount: int) -> None:
        self._amount = amount

    @abstractmethod
    def times(self, multiplier: int) -> Money:
        pass

    @staticmethod
    def dollar(amount: int) -> Dollar:
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Franc:
        return Franc(amount)

    def __eq__(self, other: Money) -> bool:

        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを引数にしてください。')
        return (self._amount == other._amount) and (self.__class__ == other.__class__)

    def __lt__(self, other: Money) -> bool:
        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを引数にしてください。')
        return (self._amount > other._amount) and (self.__class__ == other.__class__)


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

MoneyTest.test_multiplication()
MoneyTest.test_equality()
MoneyTest.test_franc_multiplication()