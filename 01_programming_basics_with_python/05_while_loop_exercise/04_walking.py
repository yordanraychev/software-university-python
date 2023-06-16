total = 0
target = 10000
while total < target:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        total += last_steps
        break
    current_steps = int(command)
    total += current_steps
diff = abs(total - target)
if total >= target:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
