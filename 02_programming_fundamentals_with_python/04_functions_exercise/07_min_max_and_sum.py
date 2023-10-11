def operations(n: list) -> int:
    minimum_number = min(n)
    maximum_number = max(n)
    sum_numbers = sum(n)
    return minimum_number, maximum_number, sum_numbers


numbers = [int(number) for number in input().split()]
result_min, result_max, result_sum = operations(numbers)
print(f"The minimum number is {result_min}")
print(f"The maximum number is {result_max}")
print(f"The sum number is: {result_sum}")
