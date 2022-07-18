"""P11
total_orderingについてはこちらに記事がわかりやすかったです。
https://www.yoheim.net/blog.php?q=20171002
このコードでは__eq__だけで十分ですが、この後の不一致の際に欲しいので最初からつけておきます。
__lt__も不要ですが、total_orderingを使うときは書かないとエラーになります。
"""

from functools import total_ordering

@total_ordering
class Dollar:

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> None:
        self.amount *= multiplier

    def __eq__(self, other: int) -> bool:
        return self.amount == other
    
    def __lt__(self, other: int) -> bool:
        return self.amount > other


class MoneyTest:

    @staticmethod
    def test_multiplication():
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount


MoneyTest.test_multiplication()