parentheses = input()
stack = []
mapping = {')': '(', '}': '{', ']': '['}

for char in parentheses:
    if char in mapping.values():
        stack.append(char)
    elif char in mapping.keys():
        if not stack or stack.pop() != mapping[char]:
            print("NO")
            break
else:
    print("YES")
