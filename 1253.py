def caesar_cipher(text, shift_value, translate=True):
    encrypted_text = ''
    aux = -shift_value if translate else shift_value
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + aux) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


number_of_lines = int(input())

for idx in range(number_of_lines):
    line = input()
    shift = int(input())
    first_encrypted_text = caesar_cipher(line, shift)
    print(first_encrypted_text)
