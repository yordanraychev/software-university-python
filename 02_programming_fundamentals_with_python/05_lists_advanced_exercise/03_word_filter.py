words_given = input().split()
filtered_words = [word for word in words_given if len(word) % 2 == 0]
print("\n".join(filtered_words))
