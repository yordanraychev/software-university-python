import re

line = input()
pattern_title = r"<title>(.*?)<\/title>"
pattern_content = r"<body>(.*?)<\/body>"
pattern_content_edit = r"<.*?>"

title_match = re.search(pattern_title, line)
title = title_match.group(1).strip()

body_match = re.search(pattern_content, line)
content = body_match.group(1).replace("\n", "").strip()
edited_content = re.sub(pattern_content_edit, "", content)

print(f"Title: {title}")
print(f"Content: {edited_content}")
