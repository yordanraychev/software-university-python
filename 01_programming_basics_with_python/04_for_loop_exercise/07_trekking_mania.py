number_of_groups = int(input())
musala_climbers = 0
montblanc_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total = 0

for current_group in range(number_of_groups):
    current_group_climbers = int(input())
    if current_group_climbers <= 5:
        musala_climbers += current_group_climbers
    elif current_group_climbers <= 12:
        montblanc_climbers += current_group_climbers
    elif current_group_climbers <= 25:
        kilimandjaro_climbers += current_group_climbers
    elif current_group_climbers <= 40:
        k2_climbers += current_group_climbers
    elif current_group_climbers >= 41:
        everest_climbers += current_group_climbers

    total += current_group_climbers

per_musala_climbers = musala_climbers / total * 100
per_montblanc_climbers = montblanc_climbers / total * 100
per_kilimandjaro_climbers = kilimandjaro_climbers / total * 100
per_k2_climbers = k2_climbers / total * 100
per_everest_climbers = everest_climbers / total * 100

print(f"{per_musala_climbers:.2f}%")
print(f"{per_montblanc_climbers:.2f}%")
print(f"{per_kilimandjaro_climbers:.2f}%")
print(f"{per_k2_climbers:.2f}%")
print(f"{per_everest_climbers:.2f}%")
