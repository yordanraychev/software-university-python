nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
hours = int(input())
nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags_price = 0.40
price_materials = nylon_price * (nylon_quantity + 2)\
                  + paint_price * paint_quantity * 1.1\
                  + thinner_price * thinner_quantity \
                  + bags_price
payment = price_materials * 0.3 * hours
total_sum=price_materials + payment
print(total_sum)
