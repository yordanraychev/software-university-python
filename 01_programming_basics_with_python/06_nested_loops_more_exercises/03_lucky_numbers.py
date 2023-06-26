number = int(input())

for first in range(1, 10):
    for second in range(1, 10):
        if number % (first + second) != 0:
            continue
        for third in range(1, 10):
            for fourth in range(1, 10):
                if first + second == third + fourth:
                    print(f"{first}{second}{third}{fourth}", end=" ")
