bottles = int(input())
ml = bottles * 750
count = 0
plates = 0
pots = 0
command = input()
done = False

while command != "End":

    if ml >= 0:
        count += 1
        dish_count = int(command)
        if count % 3 == 0:
            pots += dish_count
            ml -= dish_count * 15
        else:
            plates += dish_count
            ml -= dish_count * 5

    if ml < 0:
        done = True
        break

    command = input()

if done:
    print(f"Not enough detergent, {abs(ml)} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {ml} ml.")
