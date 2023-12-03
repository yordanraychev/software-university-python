import re

n = int(input())
for _ in range(n):
    line = input()
    name_match = re.search(r'@(\w+?)\|', line)
    age_match = re.search(r'#(\d+?)\*', line)
    name = name_match.group(1)
    age = age_match.group(1)
    print(f"{name} is {age} years old.")
