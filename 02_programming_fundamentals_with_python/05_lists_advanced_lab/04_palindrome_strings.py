def is_palindrome(word):
    if word == word[::-1]:
        return word


words = input().split()
palindrome_to_find = input()

palindromes = [word for word in words if is_palindrome(word)]
times_found = palindromes.count(palindrome_to_find)

print(palindromes)
print(f"Found palindrome {times_found} times")
