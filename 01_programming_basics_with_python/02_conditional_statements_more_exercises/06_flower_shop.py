from math import ceil, floor

magnolias_pieces = int(input())
hyacinths_pieces = int(input())
roses_pieces = int(input())
catci_pieces = int(input())
gift_price = float(input())

magnolias_price = magnolias_pieces * 3.25
hyacinths_price = hyacinths_pieces * 4.00
roses_price = roses_pieces * 3.50
cacti_price = catci_pieces * 8.00

total_price = magnolias_price + hyacinths_price + roses_price + cacti_price
total_price_net = total_price * 0.95
difference = abs(total_price_net - gift_price)

if total_price_net >= gift_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
