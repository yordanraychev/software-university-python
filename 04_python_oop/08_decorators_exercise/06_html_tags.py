def tags(tag: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator


@tags("p")
def join_strings(*args):
    return "".join(args)


# print(join_strings("Hello", " you!"))
