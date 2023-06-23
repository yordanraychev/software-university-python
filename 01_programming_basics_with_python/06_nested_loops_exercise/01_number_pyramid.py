number = int(input())
counter = 1
number_reached = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            number_reached = True
            break
    if number_reached:
        break
    print()
