import sys


def check_farm_of_strings(list_of_string_sorted, current_string_in_function):
    count = 0
    for string in list_of_string_sorted:
        if current_string_in_function in string:
            count += 1
            current_string_in_function = string
    return count


for line in sys.stdin:
    N = int(line.strip())

    if N == 0:
        break

    list_of_string = [input().strip() for _ in range(N)]

    sorted_list = sorted(list_of_string, key=len)
    max_count = 0
    for current_string in sorted_list:
        max_count = max(max_count, check_farm_of_strings(sorted_list, current_string))

    print(max_count)

