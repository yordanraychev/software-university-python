def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):
            wrapper.log[num] = func(num)
        return wrapper.log[num]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(3)
# print(fibonacci.log)
