from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
salary = int(input())
counter = 0

while locks and bullets:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    counter += 1
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print("Ping!")
    if bullets and counter % barrel_size == 0:
        print("Reloading!")

if not locks:
    money_earned = salary - counter * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
