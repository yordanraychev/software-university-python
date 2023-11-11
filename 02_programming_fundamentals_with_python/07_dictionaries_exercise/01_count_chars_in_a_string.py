symbols = [char for char in input() if char != " "]
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for symbol, occurrence in letters.items():
    print(f"{symbol} -> {occurrence}")
