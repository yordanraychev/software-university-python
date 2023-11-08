stock_data = input().split()
stock_dictionary = {}
for i in range(0, len(stock_data), 2):
    product = stock_data[i]
    quantity = int(stock_data[i + 1])
    stock_dictionary[product] = quantity

to_search = input().split()
for current_product in to_search:
    if current_product in stock_dictionary:
        print(f"We have {stock_dictionary[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
