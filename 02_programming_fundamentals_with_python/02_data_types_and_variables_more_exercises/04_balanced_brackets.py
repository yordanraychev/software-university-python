n = int(input())
balance = 0
for brackets in range(n):
    line = input()
    if "(" in line:
        balance += 1
    elif ")" in line:
        balance -= 1
    if balance != 0 and balance != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")
