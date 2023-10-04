energy = 100
coins = 100
events = input().split("|")

for event in events:
    event_type, event_v = event.split("-")
    event_value = int(event_v)
    current_energy = 0

    if event_type == "rest":
        current_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_type == "order":
        if energy >= 30:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            break

else:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
