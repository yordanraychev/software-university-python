title = input()
content = input()
html_output = f"<h1>\n    {title}\n</h1>\n<article>\n    {content}\n</article>\n"
while True:
    comment = input()
    if comment == "end of comments":
        break
    html_output += f"<div>\n    {comment}\n</div>\n"
print(html_output)
