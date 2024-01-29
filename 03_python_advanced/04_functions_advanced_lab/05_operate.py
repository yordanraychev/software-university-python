def operate(operation, *args):
    result = args[0]

    if operation == "+":
        result = sum(args)
    elif operation == "-":
        for num in args[1:]:
            result -= num
    elif operation == "/":
        for num in args[1:]:
            result /= num
    elif operation == "*":
        for num in args[1:]:
            result *= num

    return result
