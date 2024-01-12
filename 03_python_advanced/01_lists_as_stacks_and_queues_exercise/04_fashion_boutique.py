clothes = [int(x) for x in input().split()]
rack_space = int(input())
counter = 1
current_rack = rack_space

while clothes:
    current_cloth = clothes.pop()
    if current_rack >= current_cloth:
        current_rack -= current_cloth
    else:
        counter += 1
        current_rack = rack_space - current_cloth

print(counter)
