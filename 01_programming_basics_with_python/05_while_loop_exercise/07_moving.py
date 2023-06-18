w = int(input())
l = int(input())
h = int(input())
there_is_more_free_space = True
volume = w * l * h
command = input()
while command != "Done":
    current_number_of_boxes = int(command)
    volume -= current_number_of_boxes
    if volume < 0:
        there_is_more_free_space = False
        break
    command = input()
if there_is_more_free_space:
    print(f"{volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
