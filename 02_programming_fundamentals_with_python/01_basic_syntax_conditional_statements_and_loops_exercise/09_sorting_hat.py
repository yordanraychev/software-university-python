name = input()
while name != "Welcome!":
    if name != "Voldemort":
        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        elif len(name) > 6:
            print(f"{name} goes to Hufflepuff.")
    else:
        print("You must not speak of that name!")
        break
    name = input()
if "Voldemort" not in name:
    print("Welcome to Hogwarts.")

