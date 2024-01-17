unique_usernames = set()

for _ in range(int(input())):
    username = input()
    unique_usernames.add(username)

print(*unique_usernames, sep="\n")
