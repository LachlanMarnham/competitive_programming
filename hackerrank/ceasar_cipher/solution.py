from string import ascii_lowercase, ascii_uppercase


def build_cipher_map(cipher_map, char_set, k):
    for idx, letter in enumerate(char_set):
        cipher_map[letter] = char_set[(idx + k) % 26]


def ceasar_cipher(s, k):
    cipher_map = {}
    build_cipher_map(cipher_map, ascii_lowercase, k)
    build_cipher_map(cipher_map, ascii_lowercase, k)
    for idx, letter in enumerate(ascii_lowercase):
        cipher_map[letter] = ascii_lowercase[(idx + k) % 26]
    for idx, letter in enumerate(ascii_uppercase):
        cipher_map[letter] = ascii_uppercase[(idx + k) % 26]
    trans = []
    for letter in s:
        if letter.lower() in ascii_lowercase:
            trans.append(cipher_map[letter])
        else:
            trans.append(letter)
    return "".join(trans)
