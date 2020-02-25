class Enemy:

    hp = 200

    def __init__(self, attack_low, attack_high):
        self.attack_high = attack_high
        self.attack_low = attack_low

    def getAttackLow(self):
        print("Low Attack", self.attack_low)
        return self.attack_low

    def getAttackHigh(self):
        print("High Attack", self.attack_high)
        return self.attack_high

    def getHealth(self):
        print("Enemy Heath", self.hp)
        return self.hp
