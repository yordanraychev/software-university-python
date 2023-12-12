import re

demon_names = [name.strip() for name in input().split(",")]
pattern_damage = r"[+|-]?\d+\.?\d*"

for name in sorted(demon_names):
    multiplication = 0
    division = 0
    health = 0
    damage = 0

    for char in name:
        if not char.isdigit() and char not in ["+", "-", "*", "/", "."]:
            health += ord(char)
        elif char == "*":
            multiplication += 1
        elif char == "/":
            division += 1

    numbers = re.findall(pattern_damage, name)
    damage = sum([float(number) for number in numbers])

    if multiplication != 0:
        damage *= 2 ** multiplication
    if division != 0:
        damage /= 2 ** division

    print(f"{name} - {health} health, {damage:.2f} damage")
