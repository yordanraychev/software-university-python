capacity = int(input())
fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for i in range(fans):
    sector = input()
    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    elif sector == "G":
        fans_g += 1

percentage_fans_a = fans_a / fans * 100
percentage_fans_b = fans_b / fans * 100
percentage_fans_v = fans_v / fans * 100
percentage_fans_g = fans_g / fans * 100
percentage_fans = fans / capacity * 100

print(f"{percentage_fans_a:.2f}%")
print(f"{percentage_fans_b:.2f}%")
print(f"{percentage_fans_v:.2f}%")
print(f"{percentage_fans_g:.2f}%")
print(f"{percentage_fans:.2f}%")
