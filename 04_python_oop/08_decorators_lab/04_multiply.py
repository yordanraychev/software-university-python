def multiply(times):
    def decorator(function):
        def wrapper(params):
            return times * function(params)
        return wrapper
    return decorator


@multiply(3)
def add_ten(num):
    return num + 10


# print(add_ten(3))
