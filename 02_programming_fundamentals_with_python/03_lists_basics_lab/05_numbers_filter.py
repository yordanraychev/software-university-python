n = int(input())
numbers = [int(input()) for num in range(n)]
numbers_modified = []
command = input()
if command == "even":
    for num in numbers:
        if num % 2 == 0:
            numbers_modified.append(num)
if command == "odd":
    for num in numbers:
        if num % 2 != 0:
            numbers_modified.append(num)
if command == "positive":
    for num in numbers:
        if num >= 0:
            numbers_modified.append(num)
if command == "negative":
    for num in numbers:
        if num < 0:
            numbers_modified.append(num)
print(numbers_modified)
