secret_message = input().split()
new_secret_message = []
for every_message in secret_message:
    every_message = list(every_message)
    new_word = []
    first_letter = ""
    for character in every_message:
        if character.isdigit():
            first_letter += character
        else:
            new_word.append(character)
    first_letter = int(first_letter)
    new_word.insert(0, chr(first_letter))
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    new_word = str("".join(new_word))
    new_secret_message.append(new_word)
print(" ".join(new_secret_message))
