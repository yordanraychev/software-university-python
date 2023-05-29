from math import ceil

movie_name = input()
episode_time = int(input())
break_time = int(input())
lunch_time = break_time / 8
rest_time = break_time / 4
time_left = break_time - lunch_time - rest_time
difference = ceil(abs(time_left - episode_time))

if time_left >= episode_time:
    print(f"You have enough time to watch {movie_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {difference} more minutes.")
