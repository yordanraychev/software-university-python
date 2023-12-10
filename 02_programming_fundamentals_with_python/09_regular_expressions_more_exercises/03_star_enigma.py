import re

n = int(input())
planets = {"Attacked planets": [], "Destroyed planets": []}
pattern = r".*@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*"

for line in range(n):
    message = input()
    final_message = ""
    counter = 0
    for char in message:
        if char.lower() in ["s", "t", "a", "r"]:
            counter += 1
    for char in message:
        new_char = chr(ord(char) - counter)
        final_message += new_char

    match = re.search(pattern, final_message)
    if match:
        planet_name, planet_population, attack_type, soldier_count = match.groups()
        planet_population, soldier_count = int(planet_population), int(soldier_count)
        if attack_type == "A":
            planets["Attacked planets"].append(planet_name)
        elif attack_type == "D":
            planets["Destroyed planets"].append(planet_name)

for key in planets.keys():
    print(f"{key}: {len((planets[key]))}")
    for value in sorted(planets[key]):
        print(f"-> {value}")
