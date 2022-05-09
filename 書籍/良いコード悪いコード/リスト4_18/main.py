class AttackPower:

    MIN = 0
    
    def __init__(self, value):
        if value < AttackPower.MIN:
            raise ValueError('攻撃力が0より小さいです。')
        self.value = value

    def rein_Force(self, increment):
        """攻撃力を強化する
        Args:
            increment(int): 攻撃力の増加
        Returns:
            int: 強化された攻撃力        
        """
        # バリデーションチェック入れるなら
        if not isinstance(increment, AttackPower):
            raise TypeError('AttackPowerクラスを引数にしてください。')
        return AttackPower(self.value + increment.value)

    def disable(self):
        """無力化する
        Returns:
            int: 無力化された攻撃力
        """
        return AttackPower(AttackPower.MIN)

attack_power = AttackPower(20)
increment = AttackPower(15)
rein_force = attack_power.rein_Force(increment)

print(f'attack power:{rein_force.value}')

disable = attack_power.disable()
print(f'disabled attack power:{disable.value}')