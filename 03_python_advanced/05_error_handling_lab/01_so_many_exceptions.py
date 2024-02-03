numbers_list = [int(num) for num in input().split(", ")]
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number

result = int(result)
print(result)
