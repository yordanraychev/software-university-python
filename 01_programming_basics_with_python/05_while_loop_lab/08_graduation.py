name = input()
sum_grades = 0
years = 0
fails = 0

while True:
    grade = float(input())
    years += 1

    if grade < 4:
        fails += 1
        if fails > 1:
            print(f"{name} has been excluded at {years} grade")
            break
        years -= 1
    else:
        sum_grades += grade

    if years == 12:
        avg_grade = sum_grades / 12
        print(f"{name} graduated. Average grade: {avg_grade:.2f}")
        break
