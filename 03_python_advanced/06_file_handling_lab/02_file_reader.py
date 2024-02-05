import os

file_name = "numbers.txt"
path = os.path.join("..", "06_file_handling_lab", file_name)

with open(path, "r") as file:
    total_amount = 0
    for line in file.readlines():
        total_amount += int(line.strip())

    print(total_amount)
