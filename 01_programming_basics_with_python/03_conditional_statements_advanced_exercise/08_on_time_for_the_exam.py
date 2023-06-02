exam_hr = int(input())
exam_min = int(input())
arrival_hr = int(input())
arrival_min = int(input())
time_exam = exam_hr * 60 + exam_min
time_arrival = arrival_hr * 60 + arrival_min

if time_arrival > time_exam:
    print("Late")
elif time_exam - 30 <= time_arrival <= time_exam:
    print("On time")
else: # time_exam - 30 > time_arrival
    print("Early")

difference = abs(time_exam - time_arrival)
hours = difference // 60
minutes = difference % 60

if time_exam - 60 < time_arrival < time_exam:
    print(f"{minutes} minutes before the start")
elif time_arrival <= time_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_exam < time_arrival < time_exam + 60:
    print(f"{minutes} minutes after the start")
elif time_arrival >= time_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")
