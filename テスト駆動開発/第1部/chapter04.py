"""P28
プライベートは変数にアンダースコアをつけて表現
ダンダー(__)でも良いですが、下記2点でアンダースコアにしています。
1. このあとの継承でダンダーだと不都合がでるため
2. Effective Pythonではパブリック変数押しだったため
"""

from __future__ import annotations
from functools import total_ordering

@total_ordering
class Dollar:

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)

    def __eq__(self, other: Dollar) -> bool:
        if not isinstance(other, Dollar):
            raise TypeError('Dollarクラスを引数にしてください。')
        return self._amount == other._amount

    def __lt__(self, other: Dollar) -> bool:
        if not isinstance(other, Dollar):
            raise TypeError('Dollarクラスを引数にしてください。')
        return self._amount > other._amount

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

MoneyTest.test_multiplication()
MoneyTest.test_equality()