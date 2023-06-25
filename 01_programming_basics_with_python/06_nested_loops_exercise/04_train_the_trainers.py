judges = int(input())
presentations = 0
final_grade = 0
command = input()

while command != "Finish":
    presentations += 1
    current_presentation_grade = 0
    for presentation_grade in range(judges):
        current_grade = float(input())
        current_presentation_grade += current_grade
    average_grade = current_presentation_grade / judges
    print(f"{command} - {average_grade:.2f}.")
    final_grade += average_grade
    command = input()
final_average = final_grade / presentations
print(f"Student's final assessment is {final_average:.2f}.")
