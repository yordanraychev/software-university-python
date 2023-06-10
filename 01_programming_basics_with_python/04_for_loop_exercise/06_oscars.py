actor = input()
academy_p = float(input())
jury = int(input())
total_p = academy_p
for current_grade in range(jury):
    current_jury = input()
    points = float(input())
    current_p = len(current_jury) * points / 2
    total_p += current_p
    if total_p > 1250.5:
        break
if total_p > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_p:.1f}!")
else:
    diff = 1250.5 - total_p
    print(f"Sorry, {actor} you need {diff:.1f} more!")
