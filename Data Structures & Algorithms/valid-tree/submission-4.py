class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        stack = [0]
        visited = set()
        while len(stack):
            node = stack.pop()
            if node in visited: continue
            visited.add(node)
            for neighbor in adj[node]:
                stack.append(neighbor)

        return len(visited) == n 