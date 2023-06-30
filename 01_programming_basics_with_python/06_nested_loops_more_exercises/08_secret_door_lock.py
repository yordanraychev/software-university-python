hundreds = int(input())
tens = int(input())
units = int(input())

for a in range(1, hundreds + 1):
    if a % 2 == 0:
        for b in range(1, tens + 1):
            if b == 2 or b == 3 or b == 5 or b == 7:
                for c in range(1, units + 1):
                    if c % 2 == 0:
                        print(f"{a} {b} {c}")
