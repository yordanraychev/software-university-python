word = input()
while word != "End":
    if word != "SoftUni":
        new_word = ""
        for letter in word:
            new_word += letter * 2
        print(new_word)
    word = input()
