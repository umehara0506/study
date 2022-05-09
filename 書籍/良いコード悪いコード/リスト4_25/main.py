import math

class HitPoint:

    MIN = 0

    def __init__(self, amount):
        if amount < HitPoint.MIN:
            raise ValueError('HitPointが0より小さいです')
        self.amount = amount


    def damage(self, damage_amount):
        """ダメージを受ける
        Args:
            damege_amount(int): ダメージ量
        """

        next_amount = self.amount - damage_amount
        self.amount = max(HitPoint.MIN, next_amount)

    def isZero(self):
        """
        Returns:
            bool: ヒットポイントが0であればtrue
        """
        return self.amount == HitPoint.MIN

from enum import Enum, auto
class StatusType(Enum):
    dead = auto()


class Member:

    def __init__(self, hit_point):
        self.hit_point = HitPoint(30)
        self.status = []

    def damage(self, damage_amount: int):
        """ダメージを受ける
        Args:
            damege_amount(int): ダメージ量
        """
        self.hit_point.damage(damage_amount)
        if self.hit_point.isZero():
            self.status.append(StatusType.dead)

memberA = Member(30)
memberA.damage(5)
print(f'memberA HitPoint: {memberA.hit_point.amount}')

memberA.damage(5)
print(f'memberA HitPoint: {memberA.hit_point.amount}')
