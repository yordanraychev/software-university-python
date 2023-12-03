morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}


def morse_to_english(morse_code):
    words = morse_code.split(' | ')
    translated_words = []
    for word in words:
        letters = word.split(' ')
        translated_word = ''.join([morse_code_dict[letter] for letter in letters if letter])
        translated_words.append(translated_word)
    return ' '.join(translated_words)


message = input()
english_output = morse_to_english(message)
print(english_output)
