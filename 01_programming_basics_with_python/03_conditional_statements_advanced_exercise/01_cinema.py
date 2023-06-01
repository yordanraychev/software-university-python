movie_type = input()
rows = int(input())
columns = int(input())
seats = rows * columns
ticket_price = 0

if movie_type == "Premiere":
    ticket_price = 12
elif movie_type == "Normal":
    ticket_price = 7.5
elif movie_type == "Discount":
    ticket_price = 5

total_income = seats * ticket_price
print(f"{total_income:.2f} leva")
