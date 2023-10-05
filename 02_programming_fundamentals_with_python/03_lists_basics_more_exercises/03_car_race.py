sequence_of_numbers = input().split(" ")
first_car = sequence_of_numbers[:len(sequence_of_numbers) // 2]
second_car = reversed(sequence_of_numbers[(len(sequence_of_numbers) // 2) + 1:])
total_time_first = 0
total_time_second = 0

for i in first_car:
    total_time_first += int(i)
    if i == "0":
        total_time_first *= 0.80
for j in second_car:
    total_time_second += int(j)
    if j == "0":
        total_time_second *= 0.80

if total_time_first < total_time_second:
    print(f"The winner is left with total time: {total_time_first:.1f}")
else:
    print(f"The winner is right with total time: {total_time_second:.1f}")
