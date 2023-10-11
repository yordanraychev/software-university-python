def loading_bar(n):
    if n == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    progress_bar = n // 10
    return f"{n}% [{'%' * progress_bar}{'.' * (10 - progress_bar)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
