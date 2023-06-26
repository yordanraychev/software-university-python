interval_beginning = input()
interval_end = input()
invalid = input()
counter = 0

for first_letter in range(ord(interval_beginning), ord(interval_end) + 1):
    if first_letter == ord(invalid):
        continue
    for second_letter in range(ord(interval_beginning), ord(interval_end) + 1):
        if second_letter == ord(invalid):
            continue
        for third_letter in range(ord(interval_beginning), ord(interval_end) + 1):
            if third_letter == ord(invalid):
                continue
            counter += 1
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
print(counter)
