n = int(input())
field = []
destroyed_ships = 0

for _ in range(n):
    row = input()
    field.append([int(ship) for ship in row.split()])

attacks = input()
for attack in attacks.split():
    row, col = map(int, attack.split("-"))
    if field[row][col] > 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)
