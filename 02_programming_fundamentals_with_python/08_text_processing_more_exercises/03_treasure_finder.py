key_sequence = list(map(int, input().split()))
while True:
    message = input()
    if message == "find":
        break
    decrypted_message = ""
    key_counter, treasure_type, symbol_indices = 0, "", []
    for i in range(len(message)):
        current_char = chr(ord(message[i]) - key_sequence[key_counter])
        decrypted_message += current_char
        if current_char in ["&", ">", "<"]:
            symbol_indices.append(i)
        key_counter = (key_counter + 1) % len(key_sequence)
    found_treasure = decrypted_message[symbol_indices[0] + 1: symbol_indices[1]]
    found_coordinates = decrypted_message[symbol_indices[2] + 1: symbol_indices[3]]
    print(f"Found {found_treasure} at {found_coordinates}")
