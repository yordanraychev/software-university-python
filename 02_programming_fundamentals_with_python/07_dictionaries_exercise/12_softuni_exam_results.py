results = {}
submissions = {}
command = input()

while command != "exam finished":
    command = command.split("-")
    if "banned" not in command[1]:
        username, language, points = command[0], command[1], command[2]
        points = int(points)
        if username not in results.keys():
            results[username] = points
        elif results[username] < points and username in results.keys():
            results[username] = points
        if language in submissions.keys():
            submissions[language] += 1
        else:
            submissions[language] = 1
    else:
        username = command[0]
        if username in results.keys():
            del results[username]
    command = input()

print("Results:")
for username, points in results.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
