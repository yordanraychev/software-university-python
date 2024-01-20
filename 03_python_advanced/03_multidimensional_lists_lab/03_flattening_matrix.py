row = int(input())
matrix = []

for i in range(row):
    row_data = [int(el) for el in input().split(", ")]
    matrix.extend(row_data)

print(matrix)
