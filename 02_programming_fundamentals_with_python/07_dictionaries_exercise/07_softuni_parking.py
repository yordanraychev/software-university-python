n = int(input())
users_plates = {}
for _ in range(0, n):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        plate = command[2]
        if username not in users_plates.keys():
            users_plates[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command[0] == "unregister":
        if username not in users_plates.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            users_plates.pop(username)
for user, plate in users_plates.items():
    print(f"{user} => {plate}")
