def is_palindrome(n: str) -> bool:
    return n == n[::-1]


numbers = input().split(", ")
for number in numbers:
    print(is_palindrome(number))
