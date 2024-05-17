import sys


def remove_characters_at_indexes(text, indexes):
    sorted_indexes = sorted(indexes, reverse=True)

    for index in sorted_indexes:
        if 0 <= index < len(text):
            text = text[:index] + text[index + 1:]

    return text


def remove_leading_zeros(text):
    if not text:
        return "0"
    non_zero_index = 0
    while non_zero_index < len(text) and text[non_zero_index] == '0':
        non_zero_index += 1
    return text[non_zero_index:] if non_zero_index < len(text) else "0"


for line in sys.stdin:
    D, N = line.split()
    if D == "0" and N == "0":
        break
    indices = [i for i, c in enumerate(N) if c == D]
    print(remove_leading_zeros(remove_characters_at_indexes(N, indices)))

