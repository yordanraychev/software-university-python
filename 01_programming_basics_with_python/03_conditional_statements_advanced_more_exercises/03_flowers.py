chrys = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
chrys_price = 0
roses_price = 0
tulips_price = 0
flowers = chrys + roses + tulips

if season == "Spring" or season == "Summer":
    chrys_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrys_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

bouquet_price = chrys_price * chrys + roses_price * roses + tulips_price * tulips

if holiday == "Y":
    bouquet_price *= 1.15

if season == "Spring" and tulips > 7:
    bouquet_price *= 0.95
elif season == "Winter" and roses >= 10:
    bouquet_price *= 0.9

if flowers > 20:
    bouquet_price *= 0.8

bouquet_total = bouquet_price + 2

print(f"{bouquet_total:.2f}")
