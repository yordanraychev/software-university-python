def todo_notes():
    notes = []

    while True:
        note = input()
        if note == "End":
            break
        notes.append(note)

    notes_sorted = sorted(notes, key=lambda x: int(x.split("-")[0]))
    return [note.split("-")[1] for note in notes_sorted]


result = todo_notes()
print(result)
