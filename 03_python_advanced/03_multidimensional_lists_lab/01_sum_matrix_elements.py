row, col = [int(x) for x in input().split(", ")]

matrix = []
total_amount = 0
for i in range(row):
    data = [int(x) for x in input().split(", ")]
    total_amount += sum(data)
    matrix.append(data)

print(total_amount)
print(matrix)
