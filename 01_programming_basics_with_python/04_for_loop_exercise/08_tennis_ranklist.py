tournaments = int(input())
start_points = int(input())
total_points = 0
tournaments_won = 0
for tournament in range(tournaments):
    stage = input()
    if stage == "W":
        total_points += 2000
        tournaments_won += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720
avg_points = total_points // tournaments
total_points += start_points
percentage = tournaments_won / tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {avg_points}")
print(f"{percentage:.2f}%")
