from sys import maxsize

initial_numbers = [int(i) for i in input().split()]
command = input().split()

while command[0] != "end":

    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(initial_numbers):
            split_numbers_left = initial_numbers[: index + 1]
            split_numbers_right = initial_numbers[index + 1:]
            initial_numbers = split_numbers_right + split_numbers_left
        else:
            print("Invalid index")

    elif command[0] == 'max':
        if command[1] == 'even':
            max_even = -maxsize
            index_max_even = None
            for index, number in enumerate(initial_numbers):
                if number % 2 == 0 and number >= max_even:
                    max_even = number
                    index_max_even = index
            if max_even == -maxsize:
                print('No matches')
            else:
                print(index_max_even)
        else:
            max_odd = -maxsize
            index_max_odd = None
            for index, number in enumerate(initial_numbers):
                if number % 2 == 1 and number >= max_odd:
                    max_odd = number
                    index_max_odd = index
            if max_odd == -maxsize:
                print('No matches')
            else:
                print(index_max_odd)

    elif command[0] == 'min':
        if command[1] == 'even':
            min_even = maxsize
            index_min_even = None
            for index, number in enumerate(initial_numbers):
                if number % 2 == 0 and number <= min_even:
                    min_even = number
                    index_min_even = index
            if min_even == maxsize:
                print('No matches')
            else:
                print(index_min_even)
        else:
            min_odd = maxsize
            index_min_odd = None
            for index, number in enumerate(initial_numbers):
                if number % 2 == 1 and number <= min_odd:
                    min_odd = number
                    index_min_odd = index
            if min_odd == maxsize:
                print('No matches')
            else:
                print(index_min_odd)

    elif command[0] in ("first", "last"):
        count = int(command[1])
        parity = command[2]
        if count > len(initial_numbers):
            print("Invalid count")
        else:
            numbers_to_select = []
            for num in initial_numbers:
                if (num % 2 == 0 and parity == "even") or (num % 2 != 0 and parity == "odd"):
                    numbers_to_select.append(num)
            if command[0] == "last":
                numbers_to_select = numbers_to_select[-count:]
            else:
                numbers_to_select = numbers_to_select[:count]
            print(numbers_to_select)

    command = input().split()

print(f"[{', '.join(map(str, initial_numbers))}]")
