juniors = int(input())
seniors = int(input())
track = input()
juniors_fee = 0
seniors_fee = 0

if track == "trail":
    juniors_fee = 5.5
    seniors_fee = 7
elif track == "cross-country":
    juniors_fee = 8
    seniors_fee = 9.5
    if (juniors + seniors) >= 50:
        juniors_fee *= 0.75
        seniors_fee *= 0.75
elif track == "downhill":
    juniors_fee = 12.25
    seniors_fee = 13.75
elif track == "road":
    juniors_fee = 20
    seniors_fee = 21.5

juniors_total_fee = juniors * juniors_fee
seniors_total_fee = seniors * seniors_fee
total_sum = (juniors_total_fee + seniors_total_fee) * 0.95

print(f"{total_sum:.2f}")
