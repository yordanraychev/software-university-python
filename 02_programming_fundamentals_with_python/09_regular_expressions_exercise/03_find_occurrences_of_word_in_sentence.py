import re

sentence = input()
word_to_find = input()
pattern = fr"(?i)\b{word_to_find}\b"
matches = re.findall(pattern, sentence)
print(len(matches))
