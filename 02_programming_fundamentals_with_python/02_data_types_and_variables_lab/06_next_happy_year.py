start_year = int(input())
while True:
    start_year += 1
    year_str = str(start_year)
    is_happy_year = True
    for i in range(len(year_str)):
        if year_str[i] in year_str[i+1:]:
            is_happy_year = False
            break
    if is_happy_year:
        print(start_year)
        break
