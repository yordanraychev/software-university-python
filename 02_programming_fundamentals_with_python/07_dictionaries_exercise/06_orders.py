product_info = {}
command = input()
while command != "buy":
    command = command.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in product_info.keys():
        product_info[product] = [price, quantity]
    else:
        product_info[product][0] = price
        product_info[product][1] += quantity
    command = input()
for key, value in product_info.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
