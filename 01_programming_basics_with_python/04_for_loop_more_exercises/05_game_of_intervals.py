turns = int(input())
result = 0
numbers_9 = 0
numbers_19 = 0
numbers_29 = 0
numbers_39 = 0
numbers_50 = 0
numbers_invalid = 0
total_numbers = turns

for num in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        numbers_9 += 1
        result += number * 0.2
    elif 10 <= number <= 19:
        numbers_19 += 1
        result += number * 0.3
    elif 20 <= number <= 29:
        numbers_29 += 1
        result += number * 0.4
    elif 30 <= number <= 39:
        numbers_39 += 1
        result += 50
    elif 40 <= number <= 50:
        numbers_50 += 1
        result += 100
    else:
        numbers_invalid += 1
        result *= 0.5

percent_9 = numbers_9 / total_numbers * 100
percent_19 = numbers_19 / total_numbers * 100
percent_29 = numbers_29 / total_numbers * 100
percent_39 = numbers_39 / total_numbers * 100
percent_50 = numbers_50 / total_numbers * 100
percent_invalid = numbers_invalid / total_numbers * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_9:.2f}%")
print(f"From 10 to 19: {percent_19:.2f}%")
print(f"From 20 to 29: {percent_29:.2f}%")
print(f"From 30 to 39: {percent_39:.2f}%")
print(f"From 40 to 50: {percent_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
