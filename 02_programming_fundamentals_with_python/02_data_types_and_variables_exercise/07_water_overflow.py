inputs = int(input())
litres_counter = 0
capacity = 255
for _ in range(inputs):
    litres = int(input())
    if capacity - litres < 0:
        print("Insufficient capacity!")
        continue
    capacity -= litres
    litres_counter += litres
print(litres_counter)
