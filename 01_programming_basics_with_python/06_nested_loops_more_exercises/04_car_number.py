interval_beginning = int(input())
interval_end = int(input())
done = False

for one in range(interval_beginning, interval_end + 1):
    for two in range(interval_beginning, interval_end + 1):
        for three in range(interval_beginning, interval_end + 1):
            if (two + three) % 2 != 0:
                continue
            for four in range(interval_beginning, interval_end + 1):
                if one > four and (one + four) % 2 != 0:
                    print(f"{one}{two}{three}{four}", end=" ")
