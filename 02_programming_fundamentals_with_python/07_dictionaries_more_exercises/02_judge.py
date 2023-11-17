contests = {}
results = {}
command = input().split(" -> ")

while command[0] != "no more time":
    username, contest, points = command[0], command[1], int(command[2])
    contests.setdefault(contest, {})
    contests[contest][username] = max(points, contests[contest].get(username, 0))
    command = input().split(" -> ")

for contest in contests.keys():
    print(f"{contest}: {len(contests[contest])} participants")
    for position, (user, score) in enumerate(sorted(contests[contest].items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{position}. {user} <::> {score}")
        results[user] = results.get(user, 0) + score

print("Individual standings:")
for position, (user, score) in enumerate(sorted(results.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{position}. {user} -> {score}")
