def tribonacci_sequence(n, initial_numbers=[1, 1, 2]):
    sums = initial_numbers[:]
    while len(sums) < n:
        sums.append(sum(sums[-3:]))
    return ' '.join(map(str, sums[:n]))


given_number = int(input())
print(tribonacci_sequence(given_number))
