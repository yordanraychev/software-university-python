contests = {}
while True:
    contest_info = input()
    if contest_info == "end of contests":
        break
    contest, password = contest_info.split(":")
    contests[contest] = password

submissions = {}
while True:
    submission_info = input()
    if submission_info == "end of submissions":
        break
    contest, password, username, points = submission_info.split("=>")
    points = int(points)
    if contest in contests.keys() and contests[contest] == password:
        if username not in submissions:
            submissions[username] = {}
        if contest not in submissions[username] or points > submissions[username][contest]:
            submissions[username][contest] = points

best_user = max(submissions, key=lambda x: sum(submissions[x].values()))
total_points = sum(submissions[best_user].values())
print(f"Best candidate is {best_user} with total {total_points} points.")
print("Ranking:")
for user in sorted(submissions.keys()):
    print(user)
    for contest, points in sorted(submissions[user].items(), key=lambda x: x[0]):
        print(f"#  {contest} -> {points}")
