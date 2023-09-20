long_word = input().lower()
counter = 0
words_to_count = ["sand", "water", "fish", "sun"]
for word in words_to_count:
    counter += long_word.count(word)
print(counter)
