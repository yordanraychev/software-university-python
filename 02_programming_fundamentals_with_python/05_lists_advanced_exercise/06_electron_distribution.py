electrons = int(input())
electron_groups = []
for electron in range(1, electrons + 1):
    max_electrons_currently = 2 * electron ** 2
    if electrons >= max_electrons_currently:
        electron_groups.append(max_electrons_currently)
        electrons -= max_electrons_currently
        if electrons == 0:
            break
    else:
        electron_groups.append(electrons)
        break
print(electron_groups)
