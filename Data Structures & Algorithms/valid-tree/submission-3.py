class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        dfs(0)

        return len(visited) == n 