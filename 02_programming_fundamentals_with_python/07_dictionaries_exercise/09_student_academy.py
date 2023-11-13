info_students = {}
pairs = int(input())
for pair in range(pairs):
    student = input()
    grade = float(input())
    if student not in info_students.keys():
        info_students[student] = [grade]
    else:
        info_students[student].append(grade)
for student, grade in info_students.items():
    if sum(grade) / len(grade) >= 4.50:
        print(f"{student} -> {(sum(grade) / len(grade)):.2f}")
