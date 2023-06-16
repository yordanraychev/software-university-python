from sys import maxsize

number = input()
max_number = -maxsize

while number != "Stop":
    num = int(number)
    if num > max_number:
        max_number = num
    number = input()

print(max_number)
