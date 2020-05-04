from classes.game import Person, bcolors
magic = [
    {'name': 'Fire', 'cost': '100', 'dmg': 60},
    {'name': 'Thunder', 'cost': '100', 'dmg': 80},
    {'name': 'Blizzard', 'cost': '100', 'dmg': 40}
]
player = Person(460, 65, 95, 34, magic)

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())

print('-----', player.generate_spell_damage(0))
print('-----', player.generate_spell_damage(1))