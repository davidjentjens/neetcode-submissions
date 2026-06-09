class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()     

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(start_index, node):
            if start_index == len(word):
                return node.end_of_word

            char = word[start_index]

            if char == '.':
                for child_char in node.children:
                    if dfs(start_index + 1, node.children[child_char]):
                        return True

            if char not in node.children:
                return False
            return dfs(start_index + 1, node.children[char])

        return dfs(0, self.root)