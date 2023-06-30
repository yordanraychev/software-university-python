interval_beginning = int(input())
interval_end = int(input())
magic_number = int(input())
counter = 0
done = False

for a in range(interval_beginning, interval_end + 1):
    for b in range(interval_beginning, interval_end + 1):
        counter += 1
        if a + b == magic_number:
            done = True
            break
    if done:
        break
if done:
    print(f"Combination N:{counter} ({a} + {b} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
