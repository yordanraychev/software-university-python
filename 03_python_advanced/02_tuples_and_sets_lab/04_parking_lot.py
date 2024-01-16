cars = set()

for _ in range(int(input())):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT" and car_number in cars:
        cars.remove(car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
