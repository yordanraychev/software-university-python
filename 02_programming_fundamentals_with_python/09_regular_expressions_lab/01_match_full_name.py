import re

names = input()
regex_pattern = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'
matches = re.findall(regex_pattern, names)
for name in matches:
    print(name, end=" ")
