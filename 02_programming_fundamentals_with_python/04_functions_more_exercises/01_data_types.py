def type_operation(t: str, n: str):
    if t == "int":
        return int(n) * 2
    elif t == "real":
        return f"{(float(n) * 1.5):.2f}"
    elif t == "string":
        final_string = []
        for character in n:
            final_string.append(character)
        return f"${''.join(final_string)}$"


given_type = input()
number = input()
print(type_operation(given_type, number))
