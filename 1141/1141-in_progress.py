# Forca Bruta que nao funcionou... Deu time limit exceeded. 6 segundos de runtime...
import sys


# def check_farm_of_strings(list_of_string_sorted, current_string):
#     count_aux_list = []
#     index_of_aux_list = 0
#     count_aux_list.append(current_string)
#     for current_string in list_of_string_sorted:
#         if count_aux_list[index_of_aux_list] in current_string:
#             index_of_aux_list += 1
#             count_aux_list.append(current_string)
#
#     return len(count_aux_list) - 1

def check_farm_of_strings(list_of_string_sorted):
    current_array = list_of_string_sorted
    answer = 0
    for i in range(len(list_of_string_sorted)):
        aux = 0
        current_string = current_array[i]
        # print(f'current_string: {current_string}')
        # print(f'current_array[i+1::]: {current_array[i+1::]}')
        for string in current_array[i+1::]:
            # print(f'string: {string}')
            if current_string in string and len(current_string) <= len(string):
                aux += 1
                current_string = string
        # print(f'aux: {aux}')
        answer = max(aux, answer)

    return answer


test_case_1 = ('6', ['plant', 'ant', 'cant', 'decant', 'deca', 'an']) # 4
test_case_2 = ('2', ['supercalifragilisticexpialidocious', 'rag']) # 2
test_case_3 = ('9', ['abcdefgh', 'abcde', 'abcd', 'abc', 'a', 'ab', 'abcdef', 'abcdefghi', 'abcdefghijk']) # 9
test_case_4 = ('4', ['abcd', 'abcdef', 'ab', 'a']) # 4
test_case_5 = ('3', ['aaaaaaa', 'aaaaaaaaaaaaaabbbbbbb', 'bbbb']) # 2

def is_substring_in_list(target_substring, string_list):
    return any(target_substring in string for string in string_list)


def find_items_with_substring(target_substring, string_list):
    # Filtra os itens da lista que contêm a substring
    items_with_substring = [item for item in string_list if target_substring in item]
    return items_with_substring

def check_all_substrings(target_string, string_list):
    # Verifica se target_string é substring de todos os elementos da lista
    return all(target_string in item for item in string_list)

for line in [test_case_1]:
# for line in [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5]:
    # N = line.strip()
    N = line[0]

    if N == "0":
        break

    list_of_string = line[1]
    aux = []
    index_aux = 0
    for current_string in line[1]:
        if len(aux) == 0:
            aux.append([current_string])
        else:
            for string in aux:
                print(f'aux : {aux}')
                for string_2 in string:
                    if string_2 in current_string or current_string in string_2:
                        print(f'current_string: {current_string}')
                        print(f'string_2: {string_2}')
                        print(f'=======================================')
                        if current_string < string_2:
                            if check_all_substrings(current_string, string):
                                string.insert(0,current_string)
                                break
                        elif current_string > string_2:
                            if check_all_substrings(string[0], string + [current_string]):
                                string.append(current_string)
                                break
                else:
                    aux.append([current_string])

    print(max(aux, key=len))
    print(aux)
        # largest_subarray =
    # return len(largest_subarray)
    # list_of_string = []
    # for i in range(int(N)):
    #     list_of_string.append(input())
    # sorted_list = sorted(list_of_string, key=len)
    # print(check_farm_of_strings(sorted_list) + 1)
    # answer = max([check_farm_of_strings(sorted_list, current_string) for current_string in sorted_list])
    # print(answer)
