import sys


def check_farm_of_strings(list_of_string_sorted):
    max_count = 0
    for i in range(len(list_of_string_sorted)):
        count = 1
        current_string = list_of_string_sorted[i]
        for j in range(i + 1, len(list_of_string_sorted)):
            if list_of_string_sorted[j].startswith(current_string):
                count += 1
                current_string = list_of_string_sorted[j]
            else:
                break
        max_count = max(max_count, count)
    return max_count

test_case_1 = ('6', ['plant', 'ant', 'cant', 'decant', 'deca', 'an'])
test_case_2 = ('2', ['supercalifragilisticexpialidocious', 'rag'])
test_case_3 = ('9', ['abcdefgh', 'abcde', 'abcd', 'abc', 'a', 'ab', 'abcdef', 'abcdefghi', 'abcdefghijk'])
test_case_4 = ('4', ['abcd', 'abcdef', 'ab', 'a'])
test_case_5 = ('3', ['aaaaaaa', 'aaaaaaaaaaaaaabbbbbbb', 'bbbb'])










def main():
    for line in sys.stdin:
        N = int(line.strip())

        if N == 0:
            break

        list_of_string = [input().strip() for _ in range(N)]

        sorted_list = sorted(list_of_string)
        max_count = check_farm_of_strings(sorted_list)

        print(max_count)


if __name__ == "__main__":
    main()
