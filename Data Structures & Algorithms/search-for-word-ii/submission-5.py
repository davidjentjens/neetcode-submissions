class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.word = None

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        board_height, board_width = len(board), len(board[0])

        def get_valid_neighbors(start_pos):
            i, j = start_pos
            valid_neighbors = []
            for pos in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= pos[0] < board_height and 0 <= pos[1] < board_width:
                    valid_neighbors.append(pos)
            return valid_neighbors

        trie = PrefixTree()
        for word in words:
            trie.addWord(word)

        found_words = set()

        def dfs(start_pos, node):
            i, j = start_pos
            char = board[i][j]

            # If a path has been visited, or it is not in the Trie, we can prune it
            if char == '*' or char not in node.children:
                return

            # If it is, and the current node is at the end of the word, we append it to
            # the found words
            if node.children[char].end_of_word:
                found_words.add(node.children[char].word)

            # Then we mark the current position as visited, and continue the dfs on all
            # the valid neighbors of the current position
            board[i][j] = '*'
            for neighbor in get_valid_neighbors(start_pos):
                dfs(neighbor, node.children[char])

            # After doing that, we reset the original value of the cell
            board[i][j] = char

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs((i, j), trie.root)

        return list(found_words)

        