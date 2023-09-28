received_key = int(input())
number_of_lines = int(input())
for i in range(number_of_lines):
    current_letter = input()
    int_letter = ord(current_letter)
    syllable = chr(int_letter + received_key)
    print(syllable, end="")
