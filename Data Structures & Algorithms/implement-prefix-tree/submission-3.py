class TreeNode:
    def __init__(self, val, children, end_of_word):
        self.val = val
        self.children = children
        self.end_of_word = end_of_word

class PrefixTree:

    def __init__(self):
        self.root = TreeNode('', [], True)

    def printTree(self):
        def dfs(node):
            for node in node.children:
                print(node.val)
                dfs(node)
        for root_node in self.root.children:
            print(root_node.val)
            dfs(root_node)
            print('\n')

    def insert(self, word: str) -> None:
        n = len(word)
        def dfs(start_index, node, prev_word_found):
            # If the length of the word part is 0, it means we're done adding the word
            # and we may return
            if start_index == n:
                # We are going to state that this node is the end of a word here
                node.end_of_word = True
                return

            # If the word was not found earlier in the recursion, we don't need to
            # continue checking anything. We may simply create a node and move on
            if not prev_word_found:
                new_node = TreeNode(word[start_index], [], False)
                node.children.append(new_node)
                dfs(start_index + 1, new_node, False)
                return

            # If the previous word was found, then we need to check if the current part
            # of the word is found within its children
            found_node = None
            for iterate_node in node.children:
                if word[start_index] == iterate_node.val:
                    found_node = iterate_node

            # If it is found, we pass that node down the recursion, with the next
            # slice of the word
            if found_node:
                dfs(start_index + 1, found_node, True)
            # Otherwise, we create a new node and pass it down the recursion, with
            # the next slice of the word
            else:
                new_node = TreeNode(word[start_index], [], False)
                node.children.append(new_node)
                dfs(start_index + 1, new_node, False)

        dfs(0, self.root, True)

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(start_index, node):
            if start_index == n:
                return node.end_of_word
            
            found_node = None
            for node in node.children:
                if word[start_index] == node.val:
                    found_node = node

            if found_node:
                return dfs(start_index + 1, found_node)
            return False
        return dfs(0, self.root)
        

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        def dfs(start_index, node):
            if start_index == n:
                return True
            
            found_node = None
            for iterate_node in node.children:
                if prefix[start_index] == iterate_node.val:
                    found_node = iterate_node

            if found_node:
                return dfs(start_index + 1, found_node)
            return False
        return dfs(0, self.root)
        