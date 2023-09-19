first_string = input()
second_string = input()
last_printed = first_string
for char in range(len(first_string)):
    first_part = second_string[:char + 1]
    second_part = first_string[char + 1:]
    new_string = first_part + second_part
    if new_string != last_printed:
        print(new_string)
        last_printed = new_string
