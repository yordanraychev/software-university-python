numbers = input().split()
numbers_int = []
for number in numbers:
    current_number = int(number)
    numbers_int.append(current_number)
numbers_to_remove = int(input())
for i in range(numbers_to_remove):
    numbers_int.remove(min(numbers_int))
print(*numbers_int, sep=", ")
