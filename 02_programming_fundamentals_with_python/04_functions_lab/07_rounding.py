given_numbers = [float(i) for i in input().split()]
rounded_numbers = []
for element in given_numbers:
    rounded_numbers.append(round(element))
print(rounded_numbers)
