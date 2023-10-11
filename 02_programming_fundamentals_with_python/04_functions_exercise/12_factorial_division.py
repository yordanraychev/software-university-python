from math import factorial


def calculate_factorial(i, j):
    return factorial(i) / factorial(j)


first_number = int(input())
second_number = int(input())
print(f"{calculate_factorial(first_number, second_number):.2f}")
