start = int(input())
end = int(input())
number = int(input())
counter = 0
done = False

for x in range(start, end + 1):
    for y in range(start, end + 1):
        counter += 1
        if x + y == number:
            print(f"Combination N:{counter} ({x} + {y} = {number})")
            done = True
            break
    if done:
        break

if not done:
    print(f"{counter} combinations - neither equals {number}")
