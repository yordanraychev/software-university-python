plan = input().split(", ")
commands = []

while True:
    command = input()
    if command == "course start":
        break
    commands.append(command)

for command in commands:
    pt = command.split(":")
    if pt[0] == "Add" and pt[1] not in plan:
        plan.append(pt[1])
    elif pt[0] == "Insert" and pt[1] not in plan:
        index = int(pt[2])
        if 0 <= index < len(plan):
            plan.insert(index, pt[1])
    elif pt[0] == "Remove" and pt[1] in plan:
        lesson_index = plan.index(pt[1])
        plan.pop(lesson_index)
        if lesson_index < len(plan) and plan[lesson_index].endswith("-Exercise"):
            plan.pop(lesson_index)
    elif pt[0] == "Swap" and pt[1] in plan and pt[2] in plan:
        index1, index2 = plan.index(pt[1]), plan.index(pt[2])
        plan[index1], plan[index2] = plan[index2], plan[index1]
        if f"{pt[1]}-Exercise" in plan:
            exercise_index = plan.index(f"{pt[1]}-Exercise")
            plan.pop(exercise_index)
            plan.insert(index2 + 1, f"{pt[1]}-Exercise")
        if f"{pt[2]}-Exercise" in plan:
            exercise_index = plan.index(f"{pt[2]}-Exercise")
            plan.pop(exercise_index)
            plan.insert(index1 + 1, f"{pt[2]}-Exercise")
    elif pt[0] == "Exercise":
        if pt[1] not in plan:
            plan.append(pt[1])
            plan.append(f"{pt[1]}-Exercise")
        elif pt[1] in plan and f"{pt[1]}-Exercise" not in plan:
            lesson_index = plan.index(pt[1])
            plan.insert(lesson_index + 1, f"{pt[1]}-Exercise")

for index, lesson in enumerate(plan, start=1):
    print(f"{index}.{lesson}")
