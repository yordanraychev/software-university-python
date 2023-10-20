def find_position(labyrinth):
    for row in range(len(labyrinth)):
        if 'k' in labyrinth[row]:
            return [row, labyrinth[row].index('k')]


def dfs(position, labyrinth, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_path = []
    for dx, dy in directions:
        new_position = [position[0] + dx, position[1] + dy]
        if (new_position[0] in range(len(labyrinth)) and
            new_position[1] in range(len(labyrinth[0])) and
            labyrinth[new_position[0]][new_position[1]] == ' ' and
            tuple(new_position) not in visited):
            visited.add(tuple(new_position))
            path = dfs(new_position, labyrinth, visited)
            if len(path) > len(max_path):
                max_path = path
    return [position] + max_path


labyrinth = [list(input()) for _ in range(int(input()))]
position = find_position(labyrinth)
visited = set()
path = dfs(position, labyrinth, visited)
if any(pos[0] in [0, len(labyrinth) - 1] or pos[1] in [0, len(labyrinth[0]) - 1] for pos in path):
    print(f'Kate got out in {len(path)} moves')
else:
    print('Kate cannot get out')
