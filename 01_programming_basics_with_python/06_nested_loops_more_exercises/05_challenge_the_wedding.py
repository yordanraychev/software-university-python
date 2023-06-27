men = int(input())
women = int(input())
tables = int(input())
seats = tables * 2
counter = 0
occupied = False

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        counter += 2
        print(f"({man} <-> {woman})", end=" ")
        if counter >= seats:
            occupied = True
            break
    if occupied:
        break
