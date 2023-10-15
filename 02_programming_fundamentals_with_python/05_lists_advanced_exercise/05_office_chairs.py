def rooms_check(rooms_count):
    free_chairs = 0
    for room_number in range(1, rooms_count + 1):
        chairs, people = input().split()
        diff = len(chairs) - int(people)
        if diff < 0:
            print(f"{abs(diff)} more chairs needed in room {room_number}")
        free_chairs += diff
    return free_chairs


rooms = int(input())
total_free_chairs = rooms_check(rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
