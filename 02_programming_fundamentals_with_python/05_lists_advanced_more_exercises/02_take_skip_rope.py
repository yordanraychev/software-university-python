hidden_message_to_find = input()
letters_in_message = []
digits_message = []
take_list = []
skip_list = []
result = ""

for char in hidden_message_to_find:
    if not char.isdigit():
        letters_in_message.append(char)
    if char.isdigit():
        digits_message.append(int(char))

for index, digit in enumerate(digits_message):
    if index % 2 == 0:
        take_list.append(digit)
    elif index % 2 != 0:
        skip_list.append(digit)

letters_in_message = "".join(letters_in_message)

for i, j in zip(take_list, skip_list):
    result += letters_in_message[:i]
    letters_in_message = letters_in_message[j:]
    letters_in_message = letters_in_message[i:]

print("".join(result))
