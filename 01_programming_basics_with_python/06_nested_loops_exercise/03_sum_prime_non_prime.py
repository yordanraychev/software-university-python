sum_prime = 0
sum_nonprime = 0
command = input()
while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    current_number_is_prime = True
    for check in range(2, number):
        if number % check == 0:
            current_number_is_prime = False
            break
    if current_number_is_prime:
        sum_prime += number
    else:
        sum_nonprime += number
    command = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_nonprime}")
