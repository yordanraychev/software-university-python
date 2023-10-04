deck = input().split()
shuffles = int(input())
for shuffle in range(shuffles):
    middle = len(deck) // 2
    left_part = deck[:middle]
    right_part = deck[middle:]
    deck_after_shuffle = []
    for card_index in range(len(left_part)):
        deck_after_shuffle.append(left_part[card_index])
        deck_after_shuffle.append(right_part[card_index])
    deck = deck_after_shuffle
print(deck)
