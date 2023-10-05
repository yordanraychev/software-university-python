sequence_of_numbers = input().split(" ")
string_list = [*input()]
message_to_print = []
sums = []

for number in sequence_of_numbers:
    digits = []
    for digit in number:
        digits.append(int(digit))
    sums.append(sum(digits))

for s in sums:
    if s >= len(string_list):
        s = s - len(string_list)
    for character in range(len(string_list)):
        if s == character:
            message_to_print.append(string_list[character])
            string_list.pop(character)

print("".join(message_to_print))
