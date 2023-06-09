count = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for num in range(count):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    elif number >= 800:
        p5 += 1
p1_per = p1 / count * 100
p2_per = p2 / count * 100
p3_per = p3 / count * 100
p4_per = p4 / count * 100
p5_per = p5 / count * 100
print(f"{p1_per:.2f}%")
print(f"{p2_per:.2f}%")
print(f"{p3_per:.2f}%")
print(f"{p4_per:.2f}%")
print(f"{p5_per:.2f}%")
