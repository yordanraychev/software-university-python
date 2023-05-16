vegetables_price = float(input())
fruits_price = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

vegetables_cost = vegetables_price * kg_vegetables
fruits_cost = fruits_price * kg_fruits
total_sum = ( vegetables_cost + fruits_cost ) / 1.94

print(f"{total_sum:.2f}")
