from collections import deque

given_string = deque(input().split())
given_string.reverse()

print(*given_string)
