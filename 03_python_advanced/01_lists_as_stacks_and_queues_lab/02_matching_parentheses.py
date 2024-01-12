expression = input()
paren_indices = []

for i in range(0, len(expression)):
    if expression[i] == "(":
        paren_indices.append(i)
    elif expression[i] == ")":
        start_index = paren_indices.pop()
        end_index = i + 1
        print(expression[start_index:end_index])
