def logged(func):
    def wrapper(*args, **kwargs):
        return f"you called {func.__name__}{args}\n" \
               f"it returned {func(*args, **kwargs)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


# print(func(4, 4, 4))
