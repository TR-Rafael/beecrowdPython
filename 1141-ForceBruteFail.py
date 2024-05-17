# Forca Bruta que nao funcionou... Deu time limit exceeded. 6 segundos de runtime...
import sys


def check_farm_of_strings(list_of_string_sorted, current_string):
    count_aux_list = []
    index_of_aux_list = 0
    count_aux_list.append(current_string)
    for current_string in list_of_string_sorted:
        if count_aux_list[index_of_aux_list] in current_string:
            index_of_aux_list += 1
            count_aux_list.append(current_string)

    return len(count_aux_list) - 1


for line in sys.stdin:
    N = line.strip()

    if N == "0":
        break

    list_of_string = []
    for i in range(int(N)):
        list_of_string.append(input())

    sorted_list = sorted(list_of_string, key=len)
    answer = max([check_farm_of_strings(sorted_list, current_string) for current_string in sorted_list])
    print(answer)
