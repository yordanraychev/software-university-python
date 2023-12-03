start_char = input()
end_char = input()
random_string = input()

start_ascii = ord(start_char)
end_ascii = ord(end_char)

if start_ascii > end_ascii:
    start_ascii, end_ascii = end_ascii, start_ascii

sum_ascii = sum(ord(char) for char in random_string if start_ascii < ord(char) < end_ascii)
print(sum_ascii)
