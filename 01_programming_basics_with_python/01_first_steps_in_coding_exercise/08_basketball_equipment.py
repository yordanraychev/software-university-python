annual_fee = int(input())
sneakers_price = annual_fee - 0.4 * annual_fee
outfit_price = sneakers_price - 0.2 * sneakers_price
ball_price = outfit_price / 4
accessories_price = ball_price / 5
total_sum = annual_fee + sneakers_price \
            + outfit_price + ball_price + accessories_price
print(total_sum)
