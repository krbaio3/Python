import random
from Player import Player
from Enemy import Enemy

player = Player(400)
enemy = Enemy(40, 70)

playerhp = player.getHealth()
enemyAttackLow1 = enemy.getAttackLow()
enemyAttackLow2 = enemy.getAttackLow()
enemyAttackHigh1 = enemy.getAttackHigh()
enemyAttackHigh2 = enemy.getAttackHigh()

while playerhp > 0:
    dmg = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerhp -= dmg

    print("Ataque enemigo", dmg, "Valor de vida", playerhp)

    if playerhp > 30:
        playerhp = 30

    if playerhp == 30:
        continue

    print("You have low health. U have been teletransport to other place")
    break
