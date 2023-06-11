students = int(input())
excellent_students = 0
very_well_students = 0
medium_students = 0
fail_students = 0
total_grades = 0

for i in range(students):
    grade = float(input())
    if 6.00 >= grade >= 5.00:
        total_grades += grade
        excellent_students += 1
    elif 4.00 <= grade <= 4.99:
        total_grades += grade
        very_well_students += 1
    elif 3.00 <= grade <= 3.99:
        total_grades += grade
        medium_students += 1
    elif grade < 3.00:
        total_grades += grade
        fail_students += 1

total_students = excellent_students + very_well_students\
                 + medium_students + fail_students
percent_excellent_students = excellent_students / total_students * 100
percent_very_well_students = very_well_students / total_students * 100
percent_medium_students = medium_students / total_students * 100
percent_fail_students = fail_students / total_students * 100
avg_grade = total_grades / total_students

print(f"Top students: {percent_excellent_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_very_well_students:.2f}%")
print(f"Between 3.00 and 3.99: {percent_medium_students:.2f}%")
print(f"Fail: {percent_fail_students:.2f}%")
print(f"Average: {avg_grade:.2f}")
