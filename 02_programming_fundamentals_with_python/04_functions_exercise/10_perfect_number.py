def is_perfect(n):
    proper_divisors = []
    for num in range(1, n + 1):
        if n % num == 0:
            proper_divisors.append(num)
    if sum(proper_divisors) / 2 == n:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))
