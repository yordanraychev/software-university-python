def kwargs_length(**kwargs) -> int:
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))
print(kwargs_length(name="Peter", age=25))
