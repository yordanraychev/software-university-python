import os

path = os.path.join("..", "06_file_handling_lab", "my_first_file.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File already deleted!")
