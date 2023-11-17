from collections import defaultdict

dragons = defaultdict(dict)
n = int(input())

for dragon in range(n):
    type_, name, damage, health, armor = input().split()
    damage = int(damage) if damage != 'null' else 45
    health = int(health) if health != 'null' else 250
    armor = int(armor) if armor != 'null' else 10
    dragons[type_][name] = [damage, health, armor]

for type_, value in dragons.items():
    avg_damage = sum(dragon[0] for dragon in value.values()) / len(value)
    avg_health = sum(dragon[1] for dragon in value.values()) / len(value)
    avg_armor = sum(dragon[2] for dragon in value.values()) / len(value)
    print(f"{type_}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    sorted_names = dict(sorted(dragons[type_].items(), key=lambda x: x[0]))
    for name, info in sorted_names.items():
        print(f"-{name} -> damage: {info[0]}, health: {info[1]}, armor: {info[2]}")
