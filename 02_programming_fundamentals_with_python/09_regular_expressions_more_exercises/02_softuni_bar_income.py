import re

line = input()
pattern = r"%([A-Z][a-z]+)%([^\|\$\%\.]*)<([\w]+)>([^\|\$\%\.]*)\|([\d]+)\|([^\|\$\%\.]*)([1-9]+[.0-9]*)\$"
total_income = 0

while line != "end of shift":
    match = re.search(pattern, line)
    if match:
        customer, product, count, price = match.group(1, 3, 5, 7)
        total_price = int(count) * float(price)
        total_income += total_price
        print(f"{customer}: {product} - {total_price:.2f}")
    line = input()

print(f"Total income: {total_income:.2f}")
