ttt_1 = input().split()
ttt_2 = input().split()
ttt_3 = input().split()


def winner(number):
    if number == "1":
        print(f"First player won")
        exit()
    if number == "2":
        print(f"Second player won")
        exit()


for row in [ttt_1, ttt_2, ttt_3]:
    if row[0] == row[1] and row[1] == row[2]:
        winner(row[0])

for col in range(3):
    if ttt_1[col] == ttt_2[col] and ttt_2[col] == ttt_3[col]:
        winner(ttt_1[col])

if ttt_1[0] == ttt_2[1] and ttt_2[1] == ttt_3[2]:
    winner(ttt_1[0])
elif ttt_2[1] == ttt_1[2] and ttt_1[2] == ttt_3[0]:
    winner(ttt_2[1])

print(f"Draw!")
