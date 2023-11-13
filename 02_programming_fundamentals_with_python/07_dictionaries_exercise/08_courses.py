courses = {}
command = input()
while command != "end":
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
    command = input()
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
