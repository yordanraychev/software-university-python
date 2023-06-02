month = input()
nights = int(input())
ap_price = 0
st_price = 0

if month == "May" or month == "October":
    ap_price = 65
    st_price = 50
    if 7 < nights <= 14:
        st_price *= 0.95
        ap_price = 65
    elif nights > 14:
        st_price *= 0.7
        ap_price *= 0.9
elif month == "June" or month == "September":
    ap_price = 68.7
    st_price = 75.2
    if nights > 14:
        st_price *= 0.8
        ap_price *= 0.9
elif month == "July" or month == "August":
    ap_price = 77
    st_price = 76
    if nights > 14:
        st_price = 76
        ap_price *= 0.9

total_sum_ap = nights * ap_price
total_sum_st = nights * st_price

print(f"Apartment: {total_sum_ap:.2f} lv.")
print(f"Studio: {total_sum_st:.2f} lv.")
