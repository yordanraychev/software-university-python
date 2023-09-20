user_prompt = input()
animals = user_prompt.split(", ")
wolf = animals.index("wolf")
sheep = len(animals) - wolf - 1
if sheep == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
