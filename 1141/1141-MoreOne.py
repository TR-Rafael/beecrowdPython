def check_all_substrings(target_string, string_list):
    # Verifica se target_string é substring de todos os elementos da lista
    return all(target_string in item for item in string_list)

test_case_1 = ('6', ['plant', 'ant', 'cant', 'decant', 'deca', 'an']) # 4

for line in [test_case_1]:
    N = line[0]

    if N == "0":
        break

    list_of_string = line[1]
    aux = []
    index_aux = 0
    for current_string in list_of_string:
        if len(aux) == 0:
            aux.append([current_string])
        else:
            found = False  # Flag para controlar se encontramos uma correspondência válida
            for string in aux:
                for string_2 in string:
                    if string_2 in current_string or current_string in string_2:
                        if current_string < string_2:
                            if check_all_substrings(current_string, string):
                                string.insert(0, current_string)
                                found = True  # Indicamos que encontramos uma correspondência válida
                                break  # Interrompemos o loop interno
                        elif current_string > string_2:
                            if check_all_substrings(string[0], string + [current_string]):
                                string.append(current_string)
                                found = True  # Indicamos que encontramos uma correspondência válida
                                break  # Interrompemos o loop interno
                if found:
                    break  # Interrompemos o loop externo se encontrarmos uma correspondência válida
            else:
                aux.append([current_string])  # Adiciona current_string se não encontramos uma correspondência válida

    print(max(aux, key=len))
    print(aux)
