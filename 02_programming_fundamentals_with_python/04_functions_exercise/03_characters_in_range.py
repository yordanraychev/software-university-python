def characters_between_range(first: int, second: int) -> list:
    characters = []
    for char in range(first + 1, second):
        characters.append(chr(char))
    return characters


first_char = ord(input())
second_char = ord(input())
result = characters_between_range(first_char, second_char)
print(" ".join(result))
