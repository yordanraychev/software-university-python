import os

symbols = {"-", ",", ".", "!", "?"}
file_name = "01_text.txt"
path = os.path.join("..", "06_file_handling_exercise", file_name)

with open(path, "r") as file:
    text = file.readlines()

for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")
    print(text[row][::-1])
