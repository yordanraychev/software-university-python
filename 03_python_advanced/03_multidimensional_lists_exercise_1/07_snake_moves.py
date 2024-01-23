from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())
word_copy = deque(word)

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)
    print(*[word_copy.popleft() for _ in range(cols)][::(-1)**row], sep="")
