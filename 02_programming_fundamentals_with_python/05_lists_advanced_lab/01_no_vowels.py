given_letters = input()
no_vowels = [letter for letter in given_letters if letter.lower() not in ["a", "e", "i", "o", "u"]]
print("".join(no_vowels))
