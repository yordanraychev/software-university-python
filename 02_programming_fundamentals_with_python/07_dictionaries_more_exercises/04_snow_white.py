dwarfs = {}
counted_dwarfs = {}
command = input()

while command != "Once upon a time":
    name, hat, physics = command.split(" <:> ")
    physics = int(physics)
    key = (name, hat)
    if key not in dwarfs or physics > dwarfs[key]:
        dwarfs[key] = physics
    if hat in counted_dwarfs.keys():
        counted_dwarfs[hat] += 1
    else:
        counted_dwarfs[hat] = 1
    command = input()

sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1], -counted_dwarfs[x[0][1]]))
for (name, hat_color), physics in sorted_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")
