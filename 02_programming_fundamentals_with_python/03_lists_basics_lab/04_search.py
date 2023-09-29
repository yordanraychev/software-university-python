n = int(input())
word = input()
all_inputs = []
with_word = []

for _ in range(n):
    current_word = input()
    all_inputs.append(current_word)
    if word in current_word:
        with_word.append(current_word)

print(all_inputs)
print(with_word)
