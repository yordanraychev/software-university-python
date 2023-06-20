letter = input()
skip_letters = "con"
word = ""
counter = ""
guess = ""

while letter != "End":
    if letter in skip_letters:
        counter += letter
    elif letter.islower() or letter.isupper():
        guess += letter
    if "c" in counter and "o" in counter and "n" in counter:
        word += f"{guess} "
        guess = ""
        counter = ""
    if counter.count(letter) > 1:
        guess += letter
    letter = input()

print(word)