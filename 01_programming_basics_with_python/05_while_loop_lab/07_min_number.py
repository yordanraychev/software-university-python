from sys import maxsize

number = input()
min_number = maxsize

while number != "Stop":
    num = int(number)
    if num < min_number:
        min_number = num
    number = input()

print(min_number)
