n = int(input())
for _ in range(n):
    word = input()
    if "," in word or "." in word or "_" in word:
        is_pure = False
    else:
        is_pure = True
    if not is_pure:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")
