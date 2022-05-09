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


class Weapon:
    
    def __init__(self, attack_power: AttackPower):
        self.attack_power = attack_power

    def rein_Force(self, increment):
        """武器を強化する
        Args:
            increment(int): 攻撃力の増加
        Returns:
            int: 強化した攻撃力        
        """

        rein_Force = self.attack_power.rein_Force(increment)
        return Weapon(rein_Force)


attack_powerA = AttackPower(20)
attack_powerB = AttackPower(20)

weaponA = Weapon(attack_powerA)
weaponB = Weapon(attack_powerB)

increment = AttackPower(5)
rein_forced_weaponA = weaponA.rein_Force(increment)

print(f'Weapon A attack power: {weaponA.attack_power.value}')
print(f'Reinforced Weapon A attack power: {rein_forced_weaponA.attack_power.value}')
print(f'Weapon B attack power: {weaponB.attack_power.value}')

