command = input()
counter = 0
while command != "END":
    if (command == "coding" or command == "cat" or command == "dog"
            or command == "movie" or command == "CODING" or command == "CAT"
            or command == "DOG" or command == "MOVIE") and command.isupper():
        counter += 2
    elif (command == "coding" or command == "cat" or command == "dog"
            or command == "movie" or command == "CODING" or command == "CAT"
            or command == "DOG" or command == "MOVIE") and command.islower():
        counter += 1
    command = input()
if counter > 5:
    print("You need extra sleep")
else:
    print(counter)
