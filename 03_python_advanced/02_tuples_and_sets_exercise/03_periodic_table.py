table = set()

for _ in range(int(input())):
    for element in input().split():
        table.add(element)

print(*table, sep="\n")
