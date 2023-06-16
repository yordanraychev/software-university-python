max_fails = int(input())
avg_grade = 0
count_solved = 0
count_bad = 0
failed = False
last_problem = ""
current_problem = input()

while current_problem != "Enough":
    grade = int(input())
    if grade <= 4:
        count_bad += 1
        if count_bad == max_fails:
            failed = True
            break
    avg_grade += grade
    count_solved += 1
    last_problem = current_problem

    current_problem = input()

if failed:
    print(f"You need a break, {count_bad} poor grades.")
else:
    avg_grade /= count_solved
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_solved}")
    print(f"Last problem: {last_problem}")
