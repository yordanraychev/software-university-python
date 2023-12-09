import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
matches = re.findall(pattern, sentence)
for email in matches:
    print(email[0])
