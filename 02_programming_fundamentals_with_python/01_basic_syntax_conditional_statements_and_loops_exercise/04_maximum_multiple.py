divisor = int(input())
boundary = int(input())
largest_num = boundary
for num in range(divisor, boundary + 1):
    if num % divisor == 0 and boundary >= num > 0:
        largest_num = num
print(largest_num)
