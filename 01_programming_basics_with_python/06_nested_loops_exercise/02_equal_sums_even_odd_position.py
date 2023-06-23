first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    even_digits = 0
    odd_digits = 0
    current_number_str = str(current_number)
    for index, digit in enumerate(current_number_str):
        if index % 2 == 0:
            odd_digits += int(digit)
        else:
            even_digits += int(digit)
    if odd_digits == even_digits:
        print(current_number, end=" ")
