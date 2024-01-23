def print_lair(lair, sep=" "):
    for row in range(len(lair)):
        print(*lair[row], sep=sep)


def move_player(lair, player_pos, direction):
    r0, c0 = player_pos
    r1 = r0 + directions[direction][0]
    c1 = c0 + directions[direction][1]
    if r1 < 0 or r1 > len(lair) - 1 or c1 < 0 or c1 > len(lair[0]) - 1:
        lair[r0][c0] = FREE
        return f"won: {r0} {c0}"
    if lair[r1][c1] == BUNNY:
        lair[r0][c0] = FREE
        return f"dead: {r1} {c1}"
    lair[r1][c1], lair[r0][c0] = lair[r0][c0], lair[r1][c1]
    return r1, c1


def get_neighbours(lair, symbol):
    cells = set()
    for row in range(len(lair)):
        for col in range(len(lair[0])):
            if lair[row][col] == symbol:
                for direction, coordinates in directions.items():
                    x, y = coordinates
                    r, c = row + x, col + y
                    if 0 <= r <= len(lair) - 1 and 0 <= c <= len(lair[0]) - 1:
                        cells.add((r, c))
    return cells


def get_player_position(lair):
    for i in range(len(lair)):
        for j in range(len(lair[0])):
            if lair[i][j] == PLAYER:
                return i, j


def spread_bunnies(lair):
    dead_pos = None
    positions = get_neighbours(lair, BUNNY)
    for pos in positions:
        x, y = pos
        if lair[x][y] == PLAYER:
            dead_pos = (x, y)
        lair[x][y] = BUNNY
    if dead_pos:
        return f"dead: {dead_pos[0]} {dead_pos[1]}"


PLAYER, BUNNY, FREE = "P", "B", "."
directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
rows, cols = [int(x) for x in input().split()]
lair = [[x for x in input()] for _ in range(rows)]
commands = [x for x in input()]
player_position = get_player_position(lair)

for command in commands:
    result = move_player(lair, player_position, command)
    if type(result) == str:
        spread_bunnies(lair)
        print_lair(lair, sep="")
        print(result)
        break
    player_position = result
    spread_result = spread_bunnies(lair)
    if spread_result:
        print_lair(lair, sep="")
        print(spread_result)
        break
