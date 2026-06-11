class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = [[] for _ in range(n+1)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count
        