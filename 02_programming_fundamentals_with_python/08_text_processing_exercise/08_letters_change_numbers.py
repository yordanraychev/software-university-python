def process_string(s):
    total_sum = 0
    parts = [part.strip() for part in s.split()]

    for index in range(0, len(parts)):
        part = parts[index]
        number_str = ''.join(filter(str.isdigit, part))
        number = int(number_str)
        letter_before = part[0]
        letter_after = part[-1]

        if letter_before.isupper():
            number /= ord(letter_before) - ord('A') + 1
        else:
            number *= ord(letter_before) - ord('a') + 1

        if letter_after.isupper():
            number -= ord(letter_after) - ord('A') + 1
        else:
            number += ord(letter_after) - ord('a') + 1

        total_sum += number

    return total_sum


user_prompt = input()
result = process_string(user_prompt)
print(f"{result:.2f}")
