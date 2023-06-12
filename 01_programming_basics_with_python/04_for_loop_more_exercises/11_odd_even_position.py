from sys import maxsize

count_numbers = int(input())
odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
even_sum = 0
even_min = maxsize
even_max = -maxsize

for number in range(1, count_numbers + 1):
    num = float(input())
    if number % 2 == 0:
        even_sum += num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num
    elif number % 2 != 0:
        odd_sum += num
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num

print(f"OddSum={odd_sum:.2f},")

if count_numbers == 0:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
if count_numbers != 0:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")

if count_numbers == 0 or count_numbers == 1:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
