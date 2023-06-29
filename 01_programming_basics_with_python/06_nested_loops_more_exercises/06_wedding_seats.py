last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())
total_seats = 0

for index1 in range(ord("A"), ord(last_sector) + 1):
    rows_first_sector += 1
    for index2 in range(1, rows_first_sector):
        if index2 % 2 == 0:
            for index3 in range(ord("a"), ord("a") + seats_odd_row + 2):
                print(f"{chr(index1)}{index2}{chr(index3)}")
                total_seats += 1
        elif index2 % 2 != 0:
            for index3 in range(ord("a"), ord("a") + seats_odd_row):
                print(f"{chr(index1)}{index2}{chr(index3)}")
                total_seats += 1
print(total_seats)
