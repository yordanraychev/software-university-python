def smallest(numbers: list) -> int:
    return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
all_numbers = [first_number, second_number, third_number]
result = smallest(all_numbers)
print(result)
