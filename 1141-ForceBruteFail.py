import sys

def check_farm_of_strings(list_of_string_sorted):
    answer = 0
    for i in range(len(list_of_string_sorted)):
        aux = 0
        current_string = list_of_string_sorted[i]
        for string in list_of_string_sorted[i+1::]:
            if current_string in string and len(current_string) <= len(string):
                aux += 1
                current_string = string
        answer = max(aux, answer)

    return answer


for line in sys.stdin:
    N = line.strip()

    if N == "0":
        break

    list_of_string = []
    for i in range(int(N)):
        list_of_string.append(input())
    sorted_list = sorted(list_of_string, key=len)
    print(check_farm_of_strings(sorted_list) + 1)
