import string

def alphabet_position(letter):
    u_alphabet= string.ascii_uppercase
    l_alphabet= string.ascii_lowercase
    if letter in u_alphabet:
        offset= (u_alphabet.find(letter) % 26)
    if letter in l_alphabet:
        offset= (l_alphabet.find(letter) % 26)
    return offset

def rotate_character(char, rot):
    u_alphabet= string.ascii_uppercase
    l_alphabet= string.ascii_lowercase
    if char in u_alphabet or char in l_alphabet:
        current_position = alphabet_position(char)
        new_position = (current_position + rot) % 26
        if char in u_alphabet:
            new_char = string.ascii_uppercase[new_position]
        if char in l_alphabet:
            new_char = string.ascii_lowercase[new_position]
        return new_char
    else:
        return char

def encrypt(text, rot):
    encrypted_text = ''
    for letter in text:
        encrypted_letter = rotate_character(letter, rot)
        encrypted_text += encrypted_letter
    return encrypted_text
