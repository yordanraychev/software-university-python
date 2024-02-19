def get_next_position(position, direction):
    current_row_idx, current_col_idx = position
    if direction == "up":
        return (current_row_idx - 1, current_col_idx)
    elif direction == "down":
        return (current_row_idx + 1, current_col_idx)
    elif direction == "left":
        return (current_row_idx, current_col_idx - 1)
    elif direction == "right":
        return (current_row_idx, current_col_idx + 1)


def print_area(board):
    for row in board:
        print("".join(row))


n = int(input())
matrix = []
position = None
enemies_shot = 0
armor = 300

for row_idx in range(n):
    airspace_row = list(input())
    if "J" in airspace_row:
        col_idx = airspace_row.index("J")
        position = (row_idx, col_idx)
        airspace_row[col_idx] = "-"
    matrix.append(airspace_row)

while True:
    command_direction = input()

    next_row, next_col = get_next_position(position, command_direction)
    symbol = matrix[next_row][next_col]

    prev_row, prev_col = position
    matrix[prev_row][prev_col] = "-"
    matrix[next_row][next_col] = "J"
    position = (next_row, next_col)

    if symbol == "E":
        enemies_shot += 1

        if enemies_shot == 4:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        else:
            armor -= 100
            if armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                break

    elif symbol == "R":
        armor = 300

print_area(matrix)
