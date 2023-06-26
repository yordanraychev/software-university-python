first = int(input())
second = int(input())
third = int(input())

for first_number in range(1, first + 1):
    if first_number % 2 != 0:
        continue
    for second_number in range(2, second + 1):
        if second_number not in (2, 3, 5, 7):
            continue
        for third_number in range(1, third + 1):
            if third_number % 2 == 0:
                print(f"{first_number} {second_number} {third_number}")
