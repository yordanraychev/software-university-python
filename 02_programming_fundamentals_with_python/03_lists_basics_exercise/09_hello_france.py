collection_items = input().split("|")
budget = int(input())
sold_item = 0
collection_sold = []
collection_sold_str = []
profit = 0
for item in collection_items:
    is_bought = False
    item_type, item_price_str = item.split("->")
    item_price = float(item_price_str)
    if budget - item_price < 0:
        continue
    if item_type == "Clothes" and item_price <= 50:
        is_bought = True
    elif item_type == "Shoes" and item_price <= 35:
        is_bought = True
    elif item_type == "Accessories" and item_price <= 20.50:
        is_bought = True
    if is_bought:
        if budget >= item_price:
            budget -= item_price
            sold_item = item_price * 1.4
            collection_sold.append(sold_item)
            collection_sold_str.append(f"{sold_item:.2f}")
            profit += item_price * 0.4
print(" ".join(collection_sold_str))
print(f"Profit: {profit:.2f}")
if budget + sum(collection_sold) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
