class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def max_depth(self):
        def dfs(node, depth):
            max_depth = depth
            for child in node.children.values():
                max_depth = max(max_depth, dfs(child, depth + 1))
            return max_depth

        return dfs(self.root, 0)


import sys


def process_input(input_lines):
    results = []
    for line in input_lines:
        N = line.strip()

        if N == "0":
            break

        list_of_string = [input().strip() for _ in range(int(N))]

        trie = Trie()
        for string in list_of_string:
            trie.insert(string)

        max_depth = trie.max_depth()
        results.append(max_depth)
    return results


# Example usage with input directly given as test cases (for illustration)
test_cases = [
    '6\nplant\nant\ncant\ndecant\ndeca\nan\n',
    '2\nsupercalifragilisticexpialidocious\nrag\n',
    '9\nabcdefgh\nabcde\nabcd\nabc\na\nab\nabcdef\nabcdefghi\nabcdefghijk\n',
    '4\nabcd\nabcdef\nab\na\n',
    '3\naaaaaaa\naaaaaaaaaaaaaabbbbbbb\nbbbb\n',
]

for test in test_cases:
    input_lines = test.strip().split('\n')
    results = process_input(input_lines)
    for result in results:
        print(result)
