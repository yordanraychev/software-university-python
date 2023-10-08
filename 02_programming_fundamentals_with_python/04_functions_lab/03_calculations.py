def calculation(operator: str, first: int, second: int) -> int:
    if operator == "multiply":
        return first * second
    if operator == "divide":
        return int(first / second)
    if operator == "add":
        return first + second
    if operator == "subtract":
        return first - second


operation = input()
first_number = int(input())
second_number = int(input())
result = calculation(operation, first_number, second_number)
print(result)
