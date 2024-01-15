student_grades = {}

for _ in range(int(input())):
    name, grade_as_string = input().split()
    grade = float(grade_as_string)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for name, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {avg_grade:.2f})")
