class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


class Student(Person):
    def say_something(self):
        return f"{self.__name}"
