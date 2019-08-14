"""
    This program is supposed to reduce amount of typos.
    It takes text from clipboard and "translates" it (changes layout) to russian or english (if it was in english or
    russian respectively).
    It gives you ability to change keyboard layout postfactum.

    This is Linux version. It could be cross-platform and simpler using clipboard library
    but this is done via Linux cmd to avoid dependencies (to easily bind this script to a keyboard shortcut)
"""
# import clipboard
import subprocess
import os


eng_rus_map = {
    'f': 'а', ',': 'б', 'd': 'в', 'u': 'г', 'l': 'д', 't': 'е', '`': 'ё', ';': 'ж', 'p': 'з', 'b': 'и', 'q': 'й',
    'r': 'к', 'k': 'л', 'v': 'м', 'y': 'н', 'j': 'о', 'g': 'п', 'h': 'р', 'c': 'с', 'n': 'т', 'e': 'у', 'a': 'ф',
    '[': 'х', 'w': 'ц', 'x': 'ч', 'i': 'ш', 'o': 'щ', ']': 'ъ', 's': 'ы', 'm': 'ь', '\'': 'э', '.': 'ю', 'z': 'я',
    '?': ',', '/': '.', '^': ':', '$': ';', ':': 'Ж', '"': 'Э', '~': 'Ё', '{': 'Х', '}': 'Ъ', '<': 'Б', '>': 'Ю',
    '&': '?', '@': '"', ' ': ' '
}

rus_eng_map = dict(map(reversed, eng_rus_map.items()))
russian_alphabet = set(rus_eng_map.keys()) - {',', '?', '.', '"', ':', ';', '', ' '}


# Get text from clipboard
# text = clipboard.paste()
text = subprocess.check_output("xclip -o | awk '{print}'", shell=True).decode()[:-1]
result = []


# Define text language to decide which map to use
map_ = rus_eng_map if set(text) & russian_alphabet else eng_rus_map

for letter in text:
    try:
        if letter.isupper() and letter not in ('Ж', 'Э', 'Ё', 'Х', 'Ъ', 'Б', 'Ю'):
            result.append(map_[letter.lower()].upper())
        else:
            result.append(map_[letter])
    except KeyError:
        result.append(letter)


# Paste result to clipboard
# clipboard.copy("".join(result))
os.system("echo '{data}' | xclip -selection c".format(data="".join(result)))
