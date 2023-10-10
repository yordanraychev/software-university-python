def sorting(n: list) -> list:
    return sorted(n)


numbers = [int(number) for number in input().split()]
ascending_numbers = sorting(numbers)
print(ascending_numbers)
