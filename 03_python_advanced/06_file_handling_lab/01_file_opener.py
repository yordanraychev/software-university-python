import os

file_name = "text.txt"
path = os.path.join("..", "06_file_handling_lab", file_name)

try:
    file = open(path, "r")
    print("File found")
except FileNotFoundError:
    print("File is not found")
