day = int(input())
hour = int(input())
parking_fee = 0
total_sum = 0

for a in range(1, day + 1):
    for b in range(1, hour + 1):
        if a % 2 == 0 and b % 2 != 0:
            parking_fee += 2.5
        elif a % 2 != 0 and b % 2 == 0:
            parking_fee += 1.25
        else:
            parking_fee += 1
    print(f"Day: {a} - {parking_fee:.2f} leva")
    total_sum += parking_fee
    parking_fee = 0

print(f"Total: {total_sum:.2f} leva")