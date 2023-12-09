import re

furniture_bought = []
total_cost = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        furniture_bought.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for furniture in furniture_bought:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
