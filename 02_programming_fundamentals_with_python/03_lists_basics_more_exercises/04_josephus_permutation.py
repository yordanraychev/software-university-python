circle_of_people = input().split()
people = len(circle_of_people)
k = int(input())
killed = []
k, i = k - 1, 0
while people > 0:
    i = (k + i) % len(circle_of_people)
    killed.append(circle_of_people.pop(i))
    people -= 1
print(f"[{','.join(killed)}]")
