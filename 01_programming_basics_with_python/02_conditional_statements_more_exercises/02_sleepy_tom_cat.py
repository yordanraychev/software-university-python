days_off = int(input())

time_left = 0
work_days = 365 - days_off
pet_time = work_days * 63 + days_off * 127
hrs = pet_time // 60
mins = pet_time % 60

if pet_time > 30000:
    time_left = pet_time - 30000
    hrs = time_left // 60
    mins = time_left % 60
    print("Tom will run away")
    print(f"{hrs} hours and {mins} minutes more for play")
else:
    time_left = 30000 - pet_time
    hrs = time_left // 60
    mins = time_left % 60
    print("Tom sleeps well")
    print(f"{hrs} hours and {mins} minutes less for play")
