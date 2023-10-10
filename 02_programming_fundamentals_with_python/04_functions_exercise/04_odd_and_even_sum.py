def odd_and_even_sum(n):
    odd_sum = 0
    even_sum = 0
    for digit in n:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        elif int(digit) % 2 != 0:
            odd_sum += int(digit)
    return odd_sum, even_sum


number = input()
odd_total, even_total = odd_and_even_sum(number)
print(f"Odd sum = {odd_total}, Even sum = {even_total}")
