snowballs = int(input())
max_weight = 0
max_duration = 0
max_quality = 0
max_value = 0
for snowball in range(snowballs):
    weight = int(input())
    duration = int(input())
    quality = int(input())
    value = ( weight / duration) ** quality
    if value > max_value:
        max_weight = weight
        max_duration = duration
        max_quality = quality
        max_value = value
print(f"{max_weight} : {max_duration} = {int(max_value)} ({max_quality})")
