def first_cipher(text):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            encrypted_char = chr(ord(char) + 3)
        else:
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text

def second_cipher(text):
    encrypted_text = ''
    text_len = len(text)

    for i, char in enumerate(text[::-1]):
        if i >= text_len // 2:
            encrypted_char = chr(ord(char) - 1)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text



number_of_lines = int(input())

for idx in range(number_of_lines):
    line = input()
    first_encrypted_text = first_cipher(line)
    second_encrypted_text = second_cipher(first_encrypted_text)
    print(second_encrypted_text)
