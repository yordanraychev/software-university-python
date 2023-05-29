budget = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())
gpu_price = number_gpu * 250
price_per_cpu = gpu_price * 0.35
price_per_ram = gpu_price * 0.10
needed_expenses = gpu_price\
+ number_cpu * price_per_cpu\
+ number_ram * price_per_ram

if number_gpu > number_cpu:
    needed_expenses *= 0.85

difference = abs(budget - needed_expenses)

if budget >= needed_expenses:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
