def even_odd(*args):
    args, even_or_odd = args[:-1], args[-1]

    if even_or_odd == "even":
        return [num for num in args if num % 2 == 0]

    elif even_or_odd == "odd":
        return [num for num in args if num % 2 != 0]
