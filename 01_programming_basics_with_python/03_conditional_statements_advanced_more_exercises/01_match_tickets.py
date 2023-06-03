budget = float(input())
category = input()
people = int(input())
ticket_price = 0
transport = 0

if category == "VIP":
    ticket_price = 499.99
    if 1 <= people <= 4:
        transport = budget * 0.75
    elif 4 < people <= 9:
        transport = budget * 0.6
    elif 9 < people <= 24:
        transport = budget * 0.5
    elif 24 < people <= 49:
        transport = budget * 0.4
    elif 50 <= people:
        transport = budget * 0.25
elif category == "Normal":
    ticket_price = 249.99
    if 1 <= people <= 4:
        transport = budget * 0.75
    elif 4 < people <= 9:
        transport = budget * 0.6
    elif 9 < people <= 24:
        transport = budget * 0.5
    elif 24 < people <= 49:
        transport = budget * 0.4
    elif 50 <= people:
        transport = budget * 0.25

total_tickets_price = ticket_price * people
expenses = total_tickets_price + transport
difference = abs(budget - expenses)

if expenses <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
elif expenses > budget:
    print(f"Not enough money! You need {difference:.2f} leva.")
