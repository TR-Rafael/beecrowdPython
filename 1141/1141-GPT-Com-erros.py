import sys


def check_farm_of_strings(list_of_string_sorted):
    n = len(list_of_string_sorted)
    dp = [1] * n  # dp[i] will store the length of the longest chain ending with list_of_string_sorted[i]

    for i in range(n):
        for j in range(i):
            if list_of_string_sorted[j] in list_of_string_sorted[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


for line in sys.stdin:
    N = line.strip()

    if N == "0":
        break

    list_of_string = []
    for i in range(int(N)):
        list_of_string.append(input())
    sorted_list = sorted(list_of_string, key=len)
    print(check_farm_of_strings(sorted_list))

# For local testing (comment this part for online submission)
# if __name__ == "__main__":
#     test_cases = [
#         ('6', ['plant', 'ant', 'cant', 'decant', 'deca', 'an']),  # 4
#         ('2', ['supercalifragilisticexpialidocious', 'rag']),  # 2
#         ('9', ['abcdefgh', 'abcde', 'abcd', 'abc', 'a', 'ab', 'abcdef', 'abcdefghi', 'abcdefghijk']),  # 9
#         ('4', ['abcd', 'abcdef', 'ab', 'a']),  # 4
#         ('3', ['aaaaaaa', 'aaaaaaaaaaaaaabbbbbbb', 'bbbb'])  # 2
#     ]
#
#     for n, strings in test_cases:
#         sorted_list = sorted(strings, key=len)
#         result = check_farm_of_strings(sorted_list)
#         print(result)

# Uncomment the main() call for running on an online judge
# main()
