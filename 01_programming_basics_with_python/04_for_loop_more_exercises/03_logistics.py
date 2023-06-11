loads = int(input())
bus_price = 0
truck_price = 0
train_price = 0
bus_tons = 0
truck_tons = 0
train_tons = 0
tons_sum = 0

for i in range(loads):
    current_load = int(input())
    if current_load <= 3:
        bus_price += 200 * current_load
        bus_tons += current_load
    elif current_load <= 11:
        truck_price += 175 * current_load
        truck_tons += current_load
    elif current_load >= 12:
        train_price += 120 * current_load
        train_tons += current_load

total_price = bus_price + truck_price + train_price
tons_sum = bus_tons + truck_tons + train_tons
avg_price = total_price / tons_sum
percentage_bus_tons = bus_tons / tons_sum * 100
percentage_truck_tons = truck_tons / tons_sum * 100
percentage_train_tons = train_tons / tons_sum * 100

print(f"{avg_price:.2f}")
print(f"{percentage_bus_tons:.2f}%")
print(f"{percentage_truck_tons:.2f}%")
print(f"{percentage_train_tons:.2f}%")
