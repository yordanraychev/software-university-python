list_with_zeros = [int(i) for i in input().split(", ")]
for number in list_with_zeros:
    list_with_zeros.append(list_with_zeros.pop(list_with_zeros.index(0)))
print(list_with_zeros)
