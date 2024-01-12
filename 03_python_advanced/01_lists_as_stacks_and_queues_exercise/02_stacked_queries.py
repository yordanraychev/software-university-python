stack = []

for _ in range(int(input())):
    command = input().split()
    action = int(command[0])
    if action == 1:
        stack.append(command[1])
    if stack:
        if action == 2:
            stack.pop()
        elif action == 3:
            print(max(stack))
        elif action == 4:
            print(min(stack))

stack.reverse()
print(*stack, sep=", ")
