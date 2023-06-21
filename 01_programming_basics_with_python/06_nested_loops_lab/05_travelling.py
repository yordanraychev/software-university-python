while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    expenses = 0
    while True:
        expense = float(input())
        expenses += expense
        if expenses >= budget:
            print(f"Going to {destination}!")
            break
