M = int(input())
password = ""
counter = 0
done = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b and c > d) and (a * b + c * d == M):
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        password = f"{a}{b}{c}{d}"
                        done = True
if done:
    print()
    print(f"Password: {password}")
else:
    print()
    print("No!")
