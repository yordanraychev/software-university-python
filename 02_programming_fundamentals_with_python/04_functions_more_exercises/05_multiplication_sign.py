def plus_minus_zero(first, second, third):
    if first == 0 or second == 0 or third == 0:
        return "zero"
    elif ((first < 0) + (second < 0) + (third < 0)) % 2 == 0:
        return "positive"
    return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(plus_minus_zero(first_number, second_number, third_number))
