from sys import maxsize

count = int(input())
sum = 0
max = -maxsize
min = maxsize

for num in range(count):
    number = int(input())
    sum += number
    if number > max:
        max = number

if max == sum - max:
    print(f"Yes\nSum = {max}")
else:
    diff = abs(max - (sum - max))
    print(f"No\nDiff = {diff}")
