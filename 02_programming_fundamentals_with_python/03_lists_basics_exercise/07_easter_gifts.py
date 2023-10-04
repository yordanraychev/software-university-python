names_gifts = input().split()
command = input()
while command != "No Money":
    contents = command.split()
    name, gift = contents[0], contents[1]
    if name == "OutOfStock":
        for index, current_gift in enumerate(names_gifts):
            if current_gift == gift:
                names_gifts[index] = "None"
    elif name == "Required":
        provided_index = contents[2]
        if 0 <= int(provided_index) < len(names_gifts):
            names_gifts[int(provided_index)] = gift
    elif name == "JustInCase":
        names_gifts[-1] = gift
    command = input()
while "None" in names_gifts:
    names_gifts.remove("None")
print(*names_gifts)
