numbers = [int(s) for s in input().split(", ")]
current_group = 10
while numbers:
    filtered_numbers = [s for s in numbers if s <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers}")
    current_group += 10
    numbers = [s for s in numbers if s not in filtered_numbers]
