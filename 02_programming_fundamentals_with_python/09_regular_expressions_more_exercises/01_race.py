participants = input().split(", ")
participant_distances = {}
line = input()

while line != "end of race":
    racer = ''.join(filter(str.isalpha, line))
    distance = sum(int(digit) for digit in line if digit.isdigit())
    if racer in participants:
        if racer not in participant_distances:
            participant_distances[racer] = 0
        participant_distances[racer] += distance
    line = input()

sorted_racers = sorted(participant_distances.items(), key=lambda x: -x[1])
for index, (racer_name, racer_distance) in enumerate(sorted_racers[:3]):
    place = {0: "1st", 1: "2nd", 2: "3rd"}[index]
    print(f"{place} place: {racer_name}")
