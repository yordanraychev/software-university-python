def total_price_calculation(product: str, quantity: int) -> float:
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "water":
        return quantity * 1.00
    elif product == "snacks":
        return quantity * 2.00


product_type = input()
product_quantity = int(input())
total_price = total_price_calculation(product_type, product_quantity)
print(f"{total_price:.2f}")
