sequence_of_integers = [int(s) for s in input().split()]
removed_elements = []
while sequence_of_integers:
    index = int(input())
    if index < 0:
        index = 0
        removed_element = sequence_of_integers.pop(index)
        sequence_of_integers.insert(sequence_of_integers[0], sequence_of_integers[-1])
    elif index > len(sequence_of_integers) - 1:
        index = len(sequence_of_integers) - 1
        removed_element = sequence_of_integers.pop()
        sequence_of_integers.insert(sequence_of_integers[-1], sequence_of_integers[0])
    else:
        removed_element = sequence_of_integers.pop(index)
    for i, digit in enumerate(sequence_of_integers):
        if removed_element < digit:
            digit -= removed_element
        else:
            digit += removed_element
        sequence_of_integers[i] = digit
    removed_elements.append(removed_element)
print(sum(removed_elements))
