primary_1pair = int(input())
primary_2pair = int(input())
diff1 = int(input())
diff2 = int(input())

for a in range(primary_1pair, primary_1pair + diff1 + 1):
    for b in range(primary_2pair, primary_2pair + diff2 + 1):
        first_is_prime = True
        second_is_prime = True
        for c in range(2, a):
            if a % c == 0:
                first_is_prime = False
                break
        for d in range(2, b):
            if b % d == 0:
                second_is_prime = False
                break
        if first_is_prime and second_is_prime:
            print(f"{a}{b}")
