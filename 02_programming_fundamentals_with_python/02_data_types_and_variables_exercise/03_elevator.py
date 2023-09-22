number_of_individuals = int(input())
capacity = int(input())
rounds = number_of_individuals // capacity
if number_of_individuals % capacity != 0:
    rounds += 1
print(rounds)
