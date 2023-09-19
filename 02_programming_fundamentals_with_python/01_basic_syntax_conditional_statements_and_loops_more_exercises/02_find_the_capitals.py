word = input()
lst = []
for char in range(len(word)):
    if "A" <= word[char] <= "Z":
        lst.append(char)
print(lst)
