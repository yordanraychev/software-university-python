def cluster(x, y):
    if board[x][y] and not visited[x][y]:
        visited[x][y] = True
        return cluster(x - 1, y) + cluster(x + 1, y) + cluster(x, y - 1) + cluster(x, y + 1) + 1
    else:
        return 0


rows_count = int(input())
board = []
for _ in range(rows_count):
    row = f"- {input()} -".split()
    board.append([1 if _ == "." else 0 for _ in row])

board.append([0 for _ in range(len(board[0]))])
board.insert(0, [0 for _ in range(len(board[0]))])
visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

dots = [[row, column] for row in range(len(board)) for column in range(len(board[0])) if board[row][column]]
longest_cluster = 0
for xy in dots:
    cluster_size = cluster(*xy)
    if longest_cluster < cluster_size:
        longest_cluster = cluster_size

print(longest_cluster)
