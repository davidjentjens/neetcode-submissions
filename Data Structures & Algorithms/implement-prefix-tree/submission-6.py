class TreeNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        def dfs(start_index, node):
            # If the length of the word part is 0, it means we're done adding the word
            # and we may return
            if start_index == len(word):
                # We are going to state that this node is the end of a word here
                node.end_of_word = True
                return

            char = word[start_index]

            # Check if the letter is found within the children. If it isn't, create a new
            # node for the letter and continue the recursion from there
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]

            dfs(start_index + 1, node)

        dfs(0, self.root)

    def search(self, word: str) -> bool:
        def dfs(start_index, node):
            if start_index == len(word):
                return node.end_of_word
            char = word[start_index]
            if char in node.children:
                return dfs(start_index + 1, node.children[char])
            return False
        return dfs(0, self.root)

    def startsWith(self, prefix: str) -> bool:
        def dfs(start_index, node):
            if start_index == len(prefix):
                return True
            char = prefix[start_index]
            if char in node.children:
                return dfs(start_index + 1, node.children[char])
            return False
        return dfs(0, self.root)
        