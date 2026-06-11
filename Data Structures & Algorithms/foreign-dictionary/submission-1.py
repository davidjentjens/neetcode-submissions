class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        if n == 0: return ""
        if n == 1: return words[0]
        
        alphabet = []
        letters = set()
        graph = defaultdict(list)

        for i in range(n-1):
            word = words[i]
            compare_word = words[i+1]

            min_len = min(len(word), len(compare_word))
            for letter in word:
                letters.add(letter)
            for letter in compare_word:
                letters.add(letter)

            if len(word) > len(compare_word) and compare_word in word: 
                return ""
                
            pointer = 0
            while pointer < min_len and word[pointer] == compare_word[pointer]:
                pointer += 1

            if pointer < min_len:
                graph[word[pointer]].append(compare_word[pointer])

        visited = set()
        path_visited = set()
        def dfs(node):
            if node in path_visited: return False
            if node in visited: return True
            visited.add(node)
            path_visited.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor) == False: return False
            path_visited.remove(node)
            alphabet.append(node)
            return True
        
        for letter in letters:
            if not dfs(letter):
                return ""
        
        return "".join(reversed(alphabet))