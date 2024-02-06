import os
from string import punctuation

text_file_name = "02_text.txt"
output_file_name = "02_output.txt"
text_path = os.path.join("..", "06_file_handling_exercise", text_file_name)
output_path = os.path.join("..", "06_file_handling_exercise", output_file_name)


with open(text_path, "r") as file:
    text = file.readlines()

output_file = open(output_path, "w")

for row in range(len(text)):
    letters, marks = 0, 0
    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {row + 1}: {''.join(text[row][:-1])} ({letters})({marks})\n")

output_file.close()
